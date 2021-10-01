import boto3
import json
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', endpoint_url='http://dynamodb:8000')

def lambda_handler(event, context):
    table = dynamodb.Table('envios')

    try:
        body = json.loads(event['body'])
    except json.decoder.JSONDecoderError as e:
        print(e)
        return dict(statusCode=400)

    attribute_updates = dict()
    for key, val in zip(body.keys(), body.values()):
        attribute_updates[key] = dict(Value=val, Action='PUT')

    table.update_item(
        Key=dict(id=event['pathParameters']['id']),
        AttributeUpdates=attribute_updates)

    return dict(statusCode=200)
