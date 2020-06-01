from pymongo import MongoClient           
from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient('localhost', 27017) 
db = client.dbsparta                     

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/memo', methods=['GET'])
def listing():

    orders_result = list(db.orders.find({},{'_id':0}))

    return jsonify({'result': 'success', 'orders': orders_result})


@app.route('/memo', methods=['POST'])
def saving():
    
    name_receive = request.form['name_give']
    number_receive = request.form['number_give']
    address_receive = request.form['address_give']
    phonenum_receive = request.form['phonenum_give']

    order = {'name': name_receive, 'number': number_receive, "address": address_receive, "phonenum": phonenum_receive}

    db.orders.insert_one(order)

    return jsonify({'result': 'success', 'msg': '주문 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)