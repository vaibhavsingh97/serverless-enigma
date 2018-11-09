import json
from dictionary import word_list
from faker import Faker


def impsum_generator(event, context):

    fake = Faker()
    response = {
        "statusCode": 200,
        "body": str(fake.sentence(210, ext_word_list=word_list))
    }

    return response
