from flask import Flask,request
from flask_restful import  Api, Resource
import mongo_client
import json
app = Flask(__name__)
api = Api(app)
class api_new(Resource):
        def post(self):
               data = json.load(request.get_data())#获取body中的数据，降json格式转化为字典格式
               num = ['aaa','bbb','ccc']
               '''
                    
               {
           "aaa": "111111", // 必需参数
           "bbb": "222222", // 必需参数
           "ccc": "333333", // 必需参数
           "ddd": "444444" // 可选参数
               }
              
               '''
               for x in num:
                   if data.get(x) == None:#检验传入的参数是否存在以上的必须字段
                      return '该参数不存在必须在段{}'.format(x),404
               db = mongo_client.client['foo']
               account = db['bar']
               for x in data:
                   account.update_one({x:data.get(x)})#采用字典更新的方法，防止存在通用的aaa字段
api.add_resource(api_new,'/api/database/foo/bar')#注册路由