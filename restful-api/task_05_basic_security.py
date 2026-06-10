#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

basic_auth = HTTPBasicAuth()

app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

@basic_auth.verify_password
def verify_password(username, password):

    if username in users:
    #compare le mot de passe tapé avec le hash enregistré
        if check_password_hash(users[username]["password"], password):
            return username
    return None

@app.route("/basic-protected", methods=["GET"])
@basic_auth.login_required
def get_status():
    return("Basic Auth: Access Granted")

@app.route("/login", methods=["POST"])
def login():
    username = basic_auth.current_user()
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == "__main__":    
    app.run()