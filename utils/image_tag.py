import os
from pymongo import MongoClient


def get_image_tag_from_mongodb():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.framework_test
    col = db.framework
    for doc in col.find():
        if not "tag" in doc:
            continue
        tag = doc["tag"]
        os.environ['IMAGE_TAG'] = tag
        return tag


if __name__ == "__main__":
    get_image_tag_from_mongodb()
