#!/usr/bin/env python3
from flask import Flask, jsonify, abort, request
import requests as rq


app = Flask(__name__)
users = {}


@app.route("/test")
def home():
    r = rq.post('https://httpbin.org/ / post', data ={'key':'value'})
    return "test"


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    return jsonify(users)


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def user(username):
    if username in users.keys():
        return jsonify(users[username])
    abort(404)


@app.post("/add_user")
def add_user():
    dict_res = request.form
    list_key_req = ("username", "name", "age", "city")
    list_key_dict = request.form.keys()
    if not set(list_key_req).issubset(list_key_dict):
        if 'username' not in list_key_dict:
            return jsonify({"error": "Username is required"}), 400
        return jsonify({"error": "Invalid JSON"}), 401
    print(dict_res["username"], users.keys())
    if dict_res["username"] in users.keys():
        abort(409)
    users.update(
        {dict_res["username"]: {
            "username": dict_res["username"],
            "name": dict_res["name"],
            "age": int(dict_res["age"]),
            "city": dict_res["city"]}})
    return request.form


@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"error": "User not found"}), 404


@app.errorhandler(409)
def username_exist(error):
    return jsonify({"error": "Username already exists"}), 409


if __name__ == "__main__": app.run()
