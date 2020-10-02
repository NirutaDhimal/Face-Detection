import boto3
#import json

p = "y"

client = boto3.client('rekognition')

collection_id = input("Enter the CollectionId of the collection where you want to add photos: ")

while (p == "y"):
    photo = input("Enter the path and file name of the image you want to add: ")

    file_name = open(photo , 'rb').read()
    try:
        response = client.index_faces(
            CollectionId=collection_id,
            Image={
            'Bytes': file_name,
            },
            ExternalImageId=collection_id,
            DetectionAttributes=['ALL',],
            QualityFilter='NONE'
        )

        print("face is added to {} collection.".format(collection_id))
        for face in response["FaceRecords"]:
            print("Face Id: {}".format(face['Face']['FaceId']))
            print("Image Id: {}".format(face['Face']['ImageId']))
        #print(json.dumps(response, indent= 4, sort_keys= True))
    except:
        print("Operation failed!")

    p = input("Do you want to add more faces to the collection? (y/n)")
    


