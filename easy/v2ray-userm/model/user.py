from uuid import uuid4
from time import time


class User:
    # id
    id = None
    # 创建时间
    create_time = None
    # 过期时间
    expiration_time = None
    # 用户名用于区分用户
    name = None

    def __init__(self, authorization_time, name):
        self.id = uuid4()
        self.create_time = time()
        self.expiration_time = self.create_time + authorization_time
        self.name = name
