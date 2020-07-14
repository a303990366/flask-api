from flask import Flask
from flask_restful import Api, Resource,reqparse
import pandas as pd
import numpy as np
import sqlite3

app = Flask(__name__)
api = Api(app)

#element for post: qurey_time
#繼承
reqparse = reqparse.RequestParser()
reqparse.add_argument('query_time', type = str, required = True,
            help = 'No time provided', location = 'json')
#寫一個連接資料庫並且抓出我們要的資料的函式
#注意:因為不同表格所以需要額外指出連接的表格
def return_data(query_time,table_name):
    conn = sqlite3.connect('flask.db')
    c=conn.cursor()
    content=c.execute("SELECT *  from {0} Where 年月日 LIKE '{1}%'".format(table_name,query_time) )
    table=content.fetchall()
    indx=c.execute("PRAGMA table_info(%s)" % table_name) 
    index=indx.fetchall()
    indx=list(np.array(index)[:,1])
    data_list=[]
    for i in table:
        data_list.append(dict(zip(indx,i)))
    conn.commit()
    conn.close()
    return data_list

class model1(Resource):
    def __init__(self):
        self.parse=reqparse.copy()
        self.args = self.parse.parse_args()
    def post(self):
        query_time=self.args['query_time']
        model='model1'
        data_list=return_data(query_time,model)
        return {'data':data_list}

class model2(Resource):
    def __init__(self):
        self.parse=reqparse.copy()
        self.args = self.parse.parse_args()
    def post(self):
        query_time=self.args['query_time']
        model='model2'
        data_list=return_data(query_time,model)
        return {'data':data_list}
class model3(Resource):
    def __init__(self):
        self.parse=reqparse.copy()
        self.args = self.parse.parse_args()
    def post(self):
        query_time=self.args['query_time']
        model='model3'
        data_list=return_data(query_time,model)
        return {'data':data_list}
class model4(Resource):
    def __init__(self):
        self.parse=reqparse.copy()
        self.args = self.parse.parse_args()
    def post(self):
        query_time=self.args['query_time']
        model='model4'
        data_list=return_data(query_time,model)
        return {'data':data_list}
class model5(Resource):
    def __init__(self):
        self.parse=reqparse.copy()
        self.args = self.parse.parse_args()
    def post(self):
        query_time=self.args['query_time']
        model='model5'
        data_list=return_data(query_time,model)
        return {'data':data_list}
api.add_resource(model1, '/api/model1', endpoint = 'model1')
api.add_resource(model2, '/api/model2', endpoint = 'model2')
api.add_resource(model3, '/api/model3', endpoint = 'model3')
api.add_resource(model4, '/api/model4', endpoint = 'model4')
api.add_resource(model5, '/api/model5', endpoint = 'model5')
if __name__ == '__main__':
    app.run(debug=True)
