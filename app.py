from flask import Flask,request,make_response,render_template
from flask_restful import  Api, Resource
import mongo_client_two
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
               db = mongo_client_two.client['foo']
               account = db['bar']
               ac = account.find_one({'aaa': data.get('aaa')})
               if ac:
                   if data.get('aaa') == account.find_one({'aaa': data.get('aaa')})['aaa']:
                       print(1)
                       account.update_one(account.find_one({'aaa': data.get('aaa')}), {"$set": data})
                   else:
                       account.insert_one(data)
               else:
                   account.insert_one(data)
        def get(self):
            return make_response(render_template('hello.html'))
api.add_resource(api_new,'/api/database/foo/bar/')#注册路由
if __name__ =='__main__':
    app.run(debug=True)
