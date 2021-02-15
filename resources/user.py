import sqlite3
from flask_restful import Resource
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='Username is a required field')
    parser.add_argument('password', type=str, required=True, help='Password is a required field')

    def post(self):
        data = UserRegister.parser.parse_args(request)
        username = data['username']

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        check_user_exists = UserModel.find_by_username(username)
        print(check_user_exists)
        if check_user_exists:
            return {'message': f'Username {username} is already used'}, 400
        else:
            user = UserModel(data['username'], data['password'])
            user.save_to_db()

            return {'message': 'User created successfully'}, 201
            
