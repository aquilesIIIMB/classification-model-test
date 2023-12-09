#!/bin/bash

while getopts ":m:p:" opt; do
    echo ${getopts}
    case ${opt} in
        m)
            MODEL_NAME=${OPTARG}
            ;;
        p)
            PYTHON_VERSION=${OPTARG}
            ;;
        \?)
            echo "Usage: cmd "
            exit 1
            ;;
        :)
            echo "Invalid option: $OPTARG requires an argument" 1>&2
            exit 1
            ;;
    esac
done

repository=us-central1-docker.pkg.dev
project=ml-framework-maas
app_prefix=$(basename "$(dirname "$(dirname "$PWD")")")
project_prefix=$(basename "$(dirname "$(dirname "$(dirname "$(dirname "$PWD")")")")")
img_name=preprocessing
version=latest

gcloud artifacts repositories create $project_prefix --repository-format=docker --location=us-central1 --description="Descripción del repositorio"
docker build --tag $repository/$project/$project_prefix/$app_prefix/$MODEL_NAME/$img_name:$version --build-arg PYTHON_VERSION=$PYTHON_VERSION .
docker image prune --force
docker push $repository/$project/$project_prefix/$app_prefix/$MODEL_NAME/$img_name:$version
