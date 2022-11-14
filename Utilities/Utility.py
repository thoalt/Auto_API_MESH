import copy
import random
import time
import string

from jsonpath_ng import parse
from passlib import hash
from sshaolin.client import SSHClient
from Config import config as cfg
from collections import defaultdict

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

class MapDict(defaultdict):
    def __init__(self):
        super(MapDict, self).__init__(MapDict)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)

    def __setattr__(self, key, value):
        self[key] = value