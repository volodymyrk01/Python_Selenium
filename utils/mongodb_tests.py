from pymongo import MongoClient
import docker
import argparse


def push_image():
    parser = argparse.ArgumentParser()
    parser.add_argument('image_tag', type=str)
    args = parser.parse_args()

    client = docker.from_env()

    image_tag = args.image_tag
    image = client.images.get('myimage')
    image.tag(image_tag)

    client.images.push(image_tag)
    return image_tag


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
            tag = push_image()
            db.image_tag.drop()
            db.image_tag.insert_one({'tag': tag})
            break


if __name__ == "__main__":
    check_mongodb_documents()
