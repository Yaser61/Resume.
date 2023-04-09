import json
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('kafayiyedim')
def lambda_handler(event, context):
    cevap = table.get_item(Key={
        'id' : '0'
    })
    ziyaretci = cevap['Item']['ziyaretci']
    ziyaretci = ziyaretci + 1
    print(ziyaretci)
    cevap =  table.put_item(Item={
        'id' : '0',
        'ziyaretci' : ziyaretci
    })
    return ziyaretci