#!/bin/bash

# Show error message regard environment parameter
usage_error_message() {
    echo "Invalid argument $1. Correct script call: $0 {dev|prod}"
    return 1
}

dev_statements(){
    docker compose build
    docker compose up
}

prod_statements(){
    TERRAFORM_DIR="terraform/"

    terraform -chdir=$TERRAFORM_DIR init 
    terraform -chdir=$TERRAFORM_DIR validate 
    terraform -chdir=$TERRAFORM_DIR fmt -recursive
    terraform -chdir=$TERRAFORM_DIR plan
    terraform -chdir=$TERRAFORM_DIR apply
}

# Checks if the program received any parameters
if [ $# -eq 0 ]; then
    usage_error_message
fi

environment=$1

case $environment in
    dev)
        echo "Creating local development environment using Docker"
        dev_statements
        ;;
    prod)
        echo "Creating production environment in AWS using Terraform"
        prod_statements
        ;;
    *)
        usage_error_message
        ;;
esac


