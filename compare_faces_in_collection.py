import boto3
#import json

collection_id = input("Enter the CollectionId of collection with which you want to compare face: ")
photo = input("Enter the path and file name of image you want to compare: ")

file = open(photo,'rb').read()

client = boto3.client('rekognition')

response = client.detect_faces(
    Image={
        'Bytes': file
    },
    Attributes = ['ALL']
)
#print(json.dumps(response, indent=4, sort_keys= True))

if(len(response['FaceDetails']) > 0):
    res = client.search_faces_by_image(
        CollectionId = collection_id,
        Image={
            'Bytes': file
        }
    )
    faceMatches = res['FaceMatches']
    #print(json.dumps(faceMatches, indent= 4, sort_keys= True))
    if not faceMatches:
        print("Given face is not in the collection.")
    else:
        similarity = str(faceMatches[0]['Similarity'])
        print("Given face matches the collection with {} similarity .".format(similarity))
else:
    print("The image doesnot contain a face.")