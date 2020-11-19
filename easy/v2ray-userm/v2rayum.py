import argparse
import json
from db import Database
import time

db = Database()


# 更改配置文件
def config():
    config_dict = {
        "inbounds": [
            {
                "port": 10086,
                "protocol": "vmess",
                "settings": {
                    "clients": list(map(lambda user: {'id': str(user['id'])}, db.find()))
                }
            }
        ],
        "outbounds": [
            {
                "protocol": "freedom"
            }
        ]
    }
    config_json = json.dumps(config_dict)
    file = open('/usr/local/etc/v2ray/config.json', 'w')
    file.write(config_json)
    file.close()


def add_one(time, name):
    db.add({'time': time, 'name': name})
    config()


def add_many(user):
    user_str = user.replace('\'', '\"')
    user_dict = json.loads(user_str)
    db.add(user_dict)
    config()


def remove(user):
    db.remove(user)
    config()


def find():
    for user in db.find():
        print(user)


parser = argparse.ArgumentParser(description='v2ray用户管理程序')
parser.add_argument('-a', dest='add_one', action='store_const', const=add_one, help='添加一个用户')
parser.add_argument('-ad', dest='add_many', action='store_const', const=add_many, help='添加多个用户')
parser.add_argument('-rm', dest='remove', action='store_const', const=remove, help='删除用户')
parser.add_argument('-fd', dest='find', action='store_const', const=find, help='查看所有的用户')
parser.add_argument('user', metavar='{\'time\': 1, \'name\': \'username\'}', type=str, nargs='?',
                    help='用户的json格式数据，time表示授予用户的时间（月），name是用户的名字')
parser.add_argument('time', metavar='1', type=int, nargs='?', help='时间单位是月')

args = parser.parse_args()
if args.add_one is not None:
    args.add_one(args.time, args.user)
if args.add_many is not None:
    args.add_many(args.user)
if args.remove is not None:
    args.remove(args.user)
if args.find is not None:
    args.find()

if args.add_one is None and args.add_many is None and args.remove is None and args.find is None:
    # 不停的执行
    while True:
        # 自动删除到期的用户
        db.remove_expiration()
        # 并更新配置文件
        config()
        # 每天执行一次
        time.sleep(24 * 60 * 60)
