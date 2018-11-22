# demo.py 是flask restful开发的相关演示，使用学习时提供参考
# resources文件夹主要是资源
from flask_restful import Resource
from flask import jsonify,Response
import json


from models.db_demo import Cmad


class Demo(Resource):
    # demo api 用来测试mongo-web-scrapy之间正常的连接
    def get(self):
        db_get = Cmad.objects().all()
        print (db_get)
        #return jsonify('Demo')
        return jsonify(db_get)

