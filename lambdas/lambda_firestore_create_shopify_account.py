from config import config
import json

from google.cloud import firestore


def handler(event, context):
    '''Create a new account in db/accounts.
    event: An SNS message
        {
            shop_url: string,
            access_token: string,
            test: boolean,
            active: boolean
       }
    '''
    sns_message = json.loads(event['Records'][0]['Sns']['Message'])

    shop_url = sns_message['shop_url']
    access_token = sns_message['access_token']
    test = sns_message['test']
    active = sns_message['active']

    # Add a new document (creates or updates using 'set()')
    print('creating document')
    db = firestore.Client.from_service_account_json(config.FIRESTORE_SERVICE_ACCOUNT_PRIVATE_KEY)
    account_ref = db.collection('accounts').document(shop_url)
    account_ref.set({
        'access_token': access_token,
        'shop_url': shop_url,
        'test': test,
        'active': active
    })

    print('done')
    return True

if __name__ == '__main__':
    event = {
        "Records": [
            {
                "EventVersion": "1.0",
                "EventSubscriptionArn": "arn:aws:sns:EXAMPLE",
                "EventSource": "aws:sns",
                "Sns": {
                    "Message": "{\"shop_url\":\"PYTHON-lambda-test.shopify.com\",\"access_token\":\"12345\",\"test\":true,\"active\":true}",
                    "SignatureVersion": "1",
                    "Timestamp": "1970-01-01T00:00:00.000Z",
                    "Signature": "EXAMPLE",
                    "SigningCertUrl": "EXAMPLE",
                    "MessageId": "95df01b4-ee98-5cb9-9903-4c221d41eb5e",
                    "MessageAttributes": {
                        "Test": {
                            "Type": "String",
                            "Value": "TestString"
                        },
                        "TestBinary": {
                            "Type": "Binary",
                            "Value": "TestBinary"
                        }
                    },
                    "Type": "Notification",
                    "UnsubscribeUrl": "EXAMPLE",
                    "TopicArn": "arn:aws:sns:EXAMPLE",
                    "Subject": "TestInvoke"
                }
            }
        ]
    }
    handler(event, {})
