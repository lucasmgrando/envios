import boto3

dynamodb = boto3.resource('dynamodb', endpoint_url='http://dynamodb:8000')

def lambda_handler(event, context):
    table = dynamodb.Table('envios')

    response = table.scan(IndexName='pendientes')

    return dict(
        statusCode=200,
        body=response['Items'])
