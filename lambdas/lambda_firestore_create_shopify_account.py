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
