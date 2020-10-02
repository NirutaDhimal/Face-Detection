import boto3
#import json

collection_id = input("Enter the CollectionId of collection you want to delete: ")

client = boto3.client("rekognition")

try:
    response = client.delete_collection(
        CollectionId= collection_id
    )
    #print(json.dumps(response, indent = 4, sort_keys= True))
    print(collection_id + " is successfully delected.")
except:
    print("Deletion unsuccessful!")