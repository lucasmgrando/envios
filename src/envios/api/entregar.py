import boto3
import json
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', endpoint_url='http://dynamodb:8000')

def lambda_handler(event, context):
    table = dynamodb.Table('envios')

    table.update_item(
        Key=dict(id=event['pathParameters']['id']),
        AttributeUpdates=dict(pendiente=dict(
            Action='DELETE')))

    return dict(statusCode=200)
