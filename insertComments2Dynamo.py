import boto3
import json
import decimal
from botocore.exceptions import ClientError

def makeTable(dynamodb, TableName):
    table = dynamodb.create_table(TableName=TableName,
        KeySchema=[
            {
                'AttributeName': 'time',
                'KeyType': 'HASH'  #Partition_key
            },
            {
                'AttributeName': 'event',
                'KeyType': 'RANGE'  #Sort_key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'time',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'event',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )

    print("Table status:", table.table_status)


dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000",
                                #aws_access_key_id=akey,
                                #aws_secret_access_key=skey,
                                region_name="us-east-2", )

commentJson = "VanDrive_Comments_10-18-23_BLUEROUTE_AUTONOMY.json"
TableName = 'testComments'

table = dynamodb.Table(TableName)

createTable = False
try:
    is_table_existing = table.table_status in ("CREATING", "UPDATING",
                                                "DELETING", "ACTIVE")
except ClientError:
    createTable = True

if createTable:
    makeTable(dynamodb, TableName)

with open(commentJson) as json_file:
    comments = json.load(json_file, parse_float = decimal.Decimal)
    for comment in comments['comments']:

        print(comment)

        table.put_item(
           Item={
               'time': comment['timestampSec'],
               'event': comment['event'],
               'groupID': comment['groupID'],
               'gnssPosition':comment['gnssPosition']
            }
        )