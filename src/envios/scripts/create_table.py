import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

table = dynamodb.create_table(
    TableName='envios',
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'pendiente',
            'AttributeType': 'S'
        }
    ],
    GlobalSecondaryIndexes=[
        {
            'IndexName': 'pendientes',
            'KeySchema': [
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'pendiente',
                    'KeyType': 'RANGE'
                }
            ],
            'Projection': {
                'ProjectionType': 'INCLUDE',
                'NonKeyAttributes': [
                    'pendiente'
                ]
            },
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 123,
                'WriteCapacityUnits': 123
            }
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)
table.meta.client.get_waiter('table_exists').wait(TableName='envios')

print(table.item_count)
