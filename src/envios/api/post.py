from boto3.dynamodb.conditions import Key, Attr
import boto3
import json
import uuid

dynamodb = boto3.resource('dynamodb', endpoint_url='http://dynamodb:8000')

def lambda_handler(event, context):

    try:
        body = json.loads(event['body'])
    except json.decoder.JSONDecoderError as e:
        print(e)
        return dict(statusCode=400)

    email = body.get('email')
    if email is None or email == '':
        return dict(statusCode=400)

    destino = body.get('destino')
    if destino is None or destino == '':
        return dict(statusCode=400)

    requestContext = event['requestContext']

    item = dict(
        id=str(uuid.uuid4()),
        fechaAlta=requestContext['requestTime'],
        pendiente=requestContext['requestTime'],
        email=email,
        destino=destino)

    table = dynamodb.Table('envios')
    table.put_item(Item=item)

    return dict(
        statusCode=201,
        body=item)
