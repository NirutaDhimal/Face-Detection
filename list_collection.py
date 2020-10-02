import boto3
import json

client = boto3.client('rekognition')

response = client.list_collections()

print("The collections are:")
for id in response["CollectionIds"]:
    print(id)
