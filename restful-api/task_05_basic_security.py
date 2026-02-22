#!/usr/bin/env python3
from flask import Flask, jsonify, abort, request
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
import requests as rq
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity


app = Flask(__name__)
users = {
    "user1": {"username": "user1", "password": generate_password_hash("1234"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("12345"), "role": "admin"}
}
basic_auth = HTTPBasicAuth()
jwt_auth = HTTPTokenAuth(scheme='Bearer')
app.config["JWT_SECRET_KEY"] = "secret"
jwt = JWTManager(app)


@app.route("/test/user")
def test1():
    r = rq.post('http://localhost:5000/login', json={"username": "user1", "password": "1234"})
    return "connection", 200


@app.route("/test/admin")
def test2():
    r = rq.post('http://localhost:5000/login', json={"username": "admin1", "password": "12345"})
    return "connection", 200


@app.route("/test/none")
def test3():
    r = rq.post('http://localhost:5000/login', json={})
    return "connection", 200


@app.route("/test/false")
def test4():
    r = rq.post('http://localhost:5000/login', json={"username": "admin1", "password": "1234"})
    return "connection", 200


@basic_auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    password_user = None
    if user is not None:
        password_user = user.get("password")
    if username in users and check_password_hash(password_user, password):
        return username


@app.get("/basic-protected")
@basic_auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


@app.post("/login")
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    valid = False
    if username is not None or password is not None:
        user = users.get(username)
        if user is not None:
            valid = check_password_hash(user.get("password"), password)
    if valid:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    abort(401)


@app.get("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.get("/admin-only")
@jwt_required()
def admin_only():
    username = get_jwt_identity()
    user = users.get(username)
    if user is not None and user.get("role") == "admin":
        return "Admin Access: Granted"
    return ({"error": "Admin access required"}), 403


@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"error": "User not found"}), 404


if __name__ == "__main__": app.run()
