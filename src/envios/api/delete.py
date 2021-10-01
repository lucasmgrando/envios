import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', endpoint_url='http://dynamodb:8000')

def lambda_handler(event, context):
    table = dynamodb.Table('envios')

    response = table.delete_item(
        Key=dict(id=event['pathParameters']['id']))

    return dict(statusCode=200)
