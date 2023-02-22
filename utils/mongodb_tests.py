from pymongo import MongoClient
import docker
import os


def push_image():
    password = os.environ.get('password')
    client = docker.from_env()

    client.login(username='dazeforlife', password=password)

    image_tag = 'dazeforlife/myimage:latest'
    image = client.images.get('myimage')
    image.tag(image_tag)

    client.images.push(image_tag)


def check_mongodb_documents():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.framework_test
    col = db.framework
    print("\nReturn every document:")
    for doc in col.find():
        print(doc)
        if doc['result'] == 'FAILED' and doc['count'] > 0:
            print("Error, not all test are PASSED")
        elif doc['result'] == 'PASSED' and doc['count'] > 0:
            print("Pushing image to dockerhub")
            push_image()


if __name__ == "__main__":
    check_mongodb_documents()
