import random
import time
import string

from jsonpath_ng import parse
from passlib import hash
from sshaolin.client import SSHClient
from Config import config as cfg


def md5_encrypt(password, salt):
    """
    Description: Using md5 encryption to generator Password hash
    """
    return hash.md5_crypt.hash(password, salt=salt)


def random_requestID():
    """
    Description:
    """

    return random.randint(1, 20000)

def random_sessionID(size):
    """
    Description:
    """
    # generating random strings
    res = ''.join(random.choices(string.ascii_lowercase + string.digits, k=size))
    return res

def random_salt(size):
    """
    Description:
    """
    # generating random strings
    res = ''.join(random.choices(string.ascii_lowercase + string.digits, k=size))
    return res

def search_nodes_using_json_path(jsonVal, jsonPath):
    jsonpath_expr = parse(jsonPath)
    for match in jsonpath_expr.find(jsonVal):
        return match.value
