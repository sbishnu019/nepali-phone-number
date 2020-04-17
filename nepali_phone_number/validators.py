from nepali_phone_number.datasets import english_encodes, nepali_encodes
from nepali_phone_number.config import config


def is_english_number(number: str):
    if all(n.encode(encoding=config['encoding']) in english_encodes for n in number):
        return True
    return False


def is_nepali_number(number: str):
    if all(n.encode(encoding=config['encoding']) in nepali_encodes for n in number):
        return True
    return False
