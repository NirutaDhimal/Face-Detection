import boto3
#import json

client = boto3.client('rekognition')

collection_id = input("Enter the CollectionId of collection whose face_list you want: ")


try: 
    response = client.list_faces(
        CollectionId = collection_id
    )
    #print(json.dumps(response, indent = 4, sort_keys= True))
    for face in response["Faces"]:
        print("\n")
        print("Face Id: {}".format(face['FaceId']))
        print("Image Id: {}".format(face['ImageId']))


except:
    print("operation failed!")