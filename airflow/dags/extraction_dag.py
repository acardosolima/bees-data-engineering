import os
import json
from datetime import datetime
from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from ...src import utils
from ...src import etl_extraction
from ...src.modules.sources import extract_bees_brewery_api

def save_content_to_file(ti):

    filename = "brewery.json"
    path = "/opt/airflow/data/bronze/" + str(datetime.now().strftime("%Y%m%d%H%m%S"))
    #path = "/opt/airflow/data"
    file_path = os.path.join(path, filename)

    utils.validate_directory(path)

    response = ti.xcom_pull(task_ids='download_content')
    
    with open(file_path, 'w') as json_file:
        json.dump(response, json_file, indent=4)

    print(f"Attempting to create file {file_path}")

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}

with DAG(
    dag_id='breweries_api_download',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
) as dag:

    download_content = SimpleHttpOperator(
        task_id='download_content',
        method='GET',
        http_conn_id='http_default',
        endpoint='breweries',
        headers={"Content-Type": "application/json"},
        response_filter=lambda response: json.loads(response.text),
        log_response=True,
        dag=dag,
    )

    save_to_file = PythonOperator(
        
        task_id='save_content_to_file',
        python_callable=save_content_to_file,
        dag=dag,
    )

    download_content >> save_to_file
