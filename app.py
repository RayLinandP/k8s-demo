#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 12:09:32 2022

@author: ray.lin
"""
#test
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
@app.route('/', methods=['GET']) 

def foo():
    
    data = request.args.get('username')

    bot_message = data
    bot_token = '5044424464:AAGf4sOHNo23hcxiNTiRJ_gU2bSd2J-vhg8'
    bot_chatID = '-719732397'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)

    t = "以下訊息已發送："
    return t + data

if __name__ == "__main__":
# Port 監聽8088，並啟動除錯模式。test
    app.run(debug=True)
    
    