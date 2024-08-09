import os
import pandas as pd
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from ...src import utils
from ...src import etl_transform
from ...src import utils
from ...src.modules.transformers import brewery_local


def load_bronze_raw_data(input_path: str = "/opt/airflow/data/bronze/breweries.json") -> pd.DataFrame:
    try:
        df = pd.read_json(input_path)
        return df

    except Exception as e:
        print(f"Load operation failed for {input_path}")

def transform_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    try:
        df.columns = [utils.snake_to_pascal(c) for c in df.columns]
        return df
    
    except Exception as e:
        print(f"Transformation operation failed: {e}")


default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}

dag = DAG(
    'transform_breweries_dataframe',
    default_args=default_args,
    schedule_interval=None,
)

load_task = PythonOperator(
    task_id='load_bronze_raw_data',
    python_callable=load_bronze_raw_data,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_dataframe,
    provide_context=True,
)

load_task >> transform_task #>> save_task