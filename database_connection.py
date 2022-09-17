import boto3
from boto3.dynamodb.conditions import Key


# function for uploading to the dynamodb weather info table
def database_Upload(data):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('weather-info')

    return table.put_item(Item=data)


# function to query for a specific locations most recent database record
def database_Query(location):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('weather-info')

    data = table.query(KeyConditionExpression=Key('location').eq(location), Limit=1,
                       ScanIndexForward=False)

    return data['Items'][0]
