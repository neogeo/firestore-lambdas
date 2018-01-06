#!/bin/bash

echo "$PWD"

# install requirements to this directory
pip install -t . -r requirements.txt

# create zip file, excluding any env's
zip -r lambda_function.zip . -x \.env_py27/\* -x \.lambda_uploader_env_py27/\*

