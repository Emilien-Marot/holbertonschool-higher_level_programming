#!/usr/bin/env python3
from flask import Flask, jsonify, abort, request
import requests as rq


app = Flask(__name__)
users = {}


@app.route("/test/1")
def test1():
    r = rq.post('http://localhost:5000/add_user', data ={"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"})
    return jsonify(r.text), 200


@app.route("/test/2")
def test2():
    r = rq.post('http://localhost:5000/add_user', data ={"username": "john", "name": "John", "age": 30, "city": "New York"})
    return jsonify(r.text), 200


@app.route("/test/3")
def test3():
    r = rq.post('http://localhost:5000/add_user', data ={"name": "John", "age": 30, "city": "New York"})
    return jsonify(r.text), 200


@app.route("/test/4")
def test4():
    r = rq.post('http://localhost:5000/add_user', data ={"username": "john", "age": 30, "city": "New York"})
    return jsonify(r.text), 200


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    return jsonify(list(users.keys()))


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
    list_key_dict = dict_res.keys()
    print(dict_res)
    if not set(list_key_req).issubset(list_key_dict):
        if 'username' not in list_key_dict:
            return jsonify({"error": "Username is required"}), 400
        return jsonify({"error": "Invalid JSON"}), 400
    print(dict_res["username"], users.keys())
    if dict_res["username"] in users.keys():
        return jsonify({"error": "Username already exists"}), 409
    new_user = {
            "username": dict_res["username"],
            "name": dict_res["name"],
            "age": int(dict_res["age"]),
            "city": dict_res["city"]}
    users.update(
        {dict_res["username"]: new_user})
    return jsonify({"message": "User added", "user": new_user}), 201


@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"error": "User not found"}), 404


if __name__ == "__main__": app.run()
