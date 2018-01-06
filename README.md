# Firestore Lambdas
Python AWS Lambda functions for interacting with firestore
This is currently a single lambda function that adds a document to Firestore. More specifically, it creates an `account` in the given db. 

### Language
Python 2.7

### Setup
You'll need Python, Docker and the AWS command-line client installed
```
virtualenv .env_py27
. .env_py27/bin/activate
pip install -r requirements.txt
```

### Configure
This project has two configuration files:
 - `firestore_service_account_private_key.json` that describes your Firestore DB
     + Create a Firestore project. Then create a firestore [service account](https://console.firebase.google.com/u/1/project/chinavasion-sync/settings/serviceaccounts/adminsdk) 
     + Then generate a new private key, and save it as `firestore_service_account_private_key.json`

 - `lambda.json` that configures `lambda-uploader`, to upload the function to AWS
     + Set the `role` by replacing `YOUR_LAMBDA_ROLE_ARN` with your ARN

### Deploy
`./deploy`

### Test
[ ] create test for lambda using pytest
