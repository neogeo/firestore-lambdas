#!/bin/bash

# builds the python libraries in a linux environment, creates a zip, and uploads it to lambda
# *assumes .env_py27 has been setup. see Setup of README

# delete build dir
rm -r -f build
# make build dir
mkdir build

# cp everything (except .env's and lambda) to build dir
rsync -av --progress . build/ \
    --exclude .env_py27 \
    --exclude .lambda_uploader_env_py27/ \
    --exclude *.zip

# run dockerfile
CONTAINER_NAME='python-lambda-builder'
docker build -t "$CONTAINER_NAME" .
# mount the 'build' directory, docker will use the WORKINGDIR 'build'
docker run -v $PWD/build:/build "$CONTAINER_NAME"

# get new zip file
cp build/lambda_function.zip .

# upload lambda_function.zip using lambda_uploader env
# create new lambda-uploader env, if it does not already exist. we don't want to include these libs in our zip, because it uses 'boto3' which is already in the AWS envirnoment, and its around 60MB
if [ ! -d .lambda_uploader_env_py27 ]; then
    virtualenv .lambda_uploader_env_py27
    . .lambda_uploader_env_py27/bin/activate
    pip install -r lambda_uploader_requirements.txt
    deactivate
fi

# upload to AWS
. .lambda_uploader_env_py27/bin/activate
lambda-uploader --no-build
deactivate

# reactivate local env
. .env_py27/bin/activate
