# Breweries Data Analysis
This project aims to create a data pipeline consuming data from Breweries API, transform and persist it into a data lake following the medallion architecture.

## Table of contents

- [Breweries Data Analysis]()
  - [Table of contents](#table-of-contents)
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

### Prod environment
For prod environment, the chosen stack is AWS Glue with Step Functions for orchestration.
1. Install [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
2. Configure the CLI with the desired AWS user and save it to a profile
```
aws configure --profile <profile>
```
3. Terraform will use the credentials saved in *<user_home>/.aws/credentials* to do AWS operations
4. Run script setup.sh to provision the environment on AWS
```
source setup.sh -e prod
```

## Contributors
- [Adriano C. Lima](mailto:adrianocardoso1991@gmail.com)