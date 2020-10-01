import  boto3

client = boto3.client('rekognition')

collection_id = input("Enter the name of collection you want to create: ")

try:
    response = client.create_collection(
        CollectionId = collection_id
    )
    print(response['CollectionArn'].split('/')[1] + " collection has been successfully created.")

except:
    print("Collection already exists.")
