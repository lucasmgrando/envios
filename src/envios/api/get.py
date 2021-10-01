import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', endpoint_url='http://dynamodb:8000')

def lambda_handler(event, context):
    table = dynamodb.Table('envios')

    response = table.get_item(
        Key=dict(id=event['pathParameters']['id']))

    if not 'Item' in response:
        return dict(statusCode=404)

    return dict(
        statusCode=200, body=response['Item'])
