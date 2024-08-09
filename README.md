# Breweries Data Analysis
This project aims to create a data pipeline consuming data from Breweries API, transform and persist it into a data lake following the medallion architecture.

## Table of contents

- [Breweries Data Analysis]()
  - [Table of contents](#table-of-contents)
  - [Setting up](#setting-up)
    - [Dev environment](#dev-environment)
  - [Process Architecture](#process-architecture)
  - [To Do](#to-do)
  - [Contributors](#contributors)

## Setting up

### Dev environment
For dev environment, the chosen stack is docker with pyspark enabled.

1. Install [Docker Engine](https://docs.docker.com/engine/install/)
2. Confirm if Docker Compose is enabled, otherwise install it [here](https://docs.docker.com/compose/install/)
```
docker compose version
```
3. Run script setup.sh to build the image and deploy the environment
```
source setup.sh -e dev
```

<!-- ### Prod environment
For prod environment, the chosen stack is AWS Glue Jobs for execution and orchestration.
1. Install [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
2. Configure the CLI with the desired AWS user and save it to a profile
```
aws configure --profile <profile>
```
3. Terraform will use the credentials saved in *<user_home>/.aws/credentials* to do AWS operations
4. Run script setup.sh to provision the environment on AWS
```
source setup.sh -e prod 
```-->

## Process architecture
1. Creation of three modules to extract, transform and do business analyzis of data
   1. src\etl_extraction.py
   2. src\etl_transform.py
   3. src\etl_analysis.py
2. Each module receives an adapter responsible to deal with a specific datasource, data sink or transformation
3. Information are stored in a volume and it's accessible to all other containers
4. File src\main.py is the orchestrator, passing the correct functions to the three modules
5. Inside src\modules, each directory contains files describing which actions should be done in each step
6. Directory airflow\dags contains the dags responsible for each step of the process
7. Each dag will call the respective module passing parameters if necessary
8. Data are created inside the shared volume, under /opt/airflow/data

### Bronze file
![1](https://github.com/user-attachments/assets/83955acb-96cd-4845-8877-9eaac7fcd759)
### Silver file
![2](https://github.com/user-attachments/assets/6a1412cc-ca3f-4ae5-9258-aafaeb22ccd3)
### Gold file
![3](https://github.com/user-attachments/assets/e3ab1a37-4376-495c-bf9c-a19c4e9f3032)


### TO DO
- Call the modules files in DAGs functions 
- Process transformations as spark-submit jobs
- Create prod environment in aws using terraform
<!-- - Refactor transformers and loaders modules to reuse sinks methods. Parametrizing the sink files should enable to use them for various locations and file extensions
- Enable changing file name in analysis step. Could consider the *module name.parquet* -->

## Contributors
- [Adriano C. Lima](mailto:adrianocardoso1991@gmail.com)
