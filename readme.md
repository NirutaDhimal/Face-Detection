This project detects whether an input face is in collection of faces or not using AWS Rekognition API. This is mainly useful in systems like employee detection system, student detection system, etc.

create_collection.py creates a collection of faces using AWS Rekognition API. The collection could contain images of employees if you are buiding empployee detection system.

add_face_to_collection.py adds faces to the given collection using AWS Rekognition API and shows faceid and imageid of face added to the collection. If you are building an employee
detection system then you can add faces of your employees to the employee collection using add_face_to_collection.py 

list_collection.py shows the list of collections you have.

delete_collection.py deletes the collection you specify.

delete_face_from_collection.py deletes the face with specified faceid from specified collection.

face_list.py shows the faceid and imageid of the faces in the specified collection.

compare_faces_in_collection.py compares the given face with the faces in the collection and shows whether the given face matches any face in the collection or not.



