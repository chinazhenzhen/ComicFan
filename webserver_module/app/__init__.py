# app.py 主要是路由的分配。以及一些配置相关的文件
# 项目初期未使用蓝图，model层也写入到app.py中

from flask import Flask
from flask_restful import Api
from flask_mongoengine import MongoEngine
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

app.config['MONGODB_SETTINGS']={
    'host':'127.0.0.1',
    'port':27017,
    'db':'manhua',
}
app.config['JSON_AS_ASCII'] = False
db = MongoEngine(app)

api = Api(app)


#  整个app需要加载完db等配置后，才能加载资源。
from resources.demo import Demo

api.add_resource(Demo, '/demo')

