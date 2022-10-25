import json
import boto3
import uuid

# To use Boto3, you must first import it and indicate which service or services you're going to use:
dynamodb = boto3.resource('dynamodb', region_name='eu-west-2')
table = dynamodb.Table('made_up_users')

def lambda_handler(event, context):
    print(event)
    print(context)
    data = json.loads(event['body'])
    
    try:
        response = table.put_item(
            Item={
                'id': str(uuid.uuid4()),
                'username': data['username'],
                'email': data['email'],
                'password': data['password']
            }
        )
        return {
            'statusCode': 200,
            'body': json.dumps("Successfully added a user")
        }

    except Exception as e:
        print (e)
        return {
            'statusCode': 500,
            'body': json.dumps("error when adding a user")
        }
