import boto3
#import json

client = boto3.client('rekognition')

collection_id =input("Enter the CollectionId of collection from where you wan to delete faces: ")
faceid = []

p = "y"
while(p == "y"):
    id = input("Enter the FaceId of face you want to delete: ")
    faceid.append(id)
    p = input("Do you want to delete more faces from the collection?(y/n): ")

try:
    response = client.delete_faces(
        CollectionId = collection_id,
        FaceIds = faceid
    )
    #print(json.dumps(response, indent=4, sort_keys= True))
    print("FaceId of deleted faces are: \n")
    for face in response['DeletedFaces']:
        print(face)

except:
    print("Operation failed!")
