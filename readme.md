This project detects whether an input face is in collection of faces or not 
using AWS Rekognition API. This is mainly useful in systems like employee
detection system, student detection system, etc

create_collection.py creates a collection of faces using AWS Rekognition API.
The collection could contain images of employees if you are buiding empployee
detection system.

add_face_to_collection.py adds faces to the given collection using AWS 
Rekognition API. If you are building an employee detection system then you 
can add faces of your employees to the employee collection using 
add_face_to_collection.py 

list_collection.py shows the list of collections you have.

delete_collection.py deletes the collection you specify.

