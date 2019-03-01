import os
import json
from flask import Flask, render_template, request


app = Flask('simple login app')


app.route('/register', methods=['POST'])
def register():
    # get username & password from request
    # compare with database
    # add to database if not exist
    # return response

    # with open('users.json') as f:
    #     users = json.load(f)
    # # users['john'] = {'password': '123456'}
    # # users['dror'] = {'password': '123456'}
    # # users['domi'] = {'password': '123456'}
    # # users['sunn'] = {'password': '123456'}
    # #
    # # with open('users.json', 'w') as f:
    # #     json.dump(users, f)
    # print(users)
    pass


app.route('/login', methods=['POST'])
def login():
    # get username & password from request
    # compare with database
    # send authorized response
    pass
