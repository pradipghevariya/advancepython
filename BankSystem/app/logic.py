from app import app
from BankSystem.config import client
from flask import request, jsonify, make_response

db = client["BankSystem"]
collection = db["BankData"]


@app.route("/createuser", methods=['post'])
def create_user():
    data = request.get_json()
    if data:
        collection.insert_many(data)
        return make_response(jsonify({"msg": "Your information is stored in database"}))
    else:
        return jsonify({"error": "please provide the data"})


@app.route("/getuser/<id>", methods=['get'])
def get_user(id):
    user_result = collection.find_one({"_id": int(id)})
    if user_result:
        return make_response(jsonify(user_result), 200)
    else:
        return make_response(jsonify({"error": "User not found"}))


@app.route("/updateuser/<id>", methods=["put"])
def update_user(id):
    data = request.get_json()
    user_result = collection.find_one({"_id": int(id)})
    if user_result:
        collection.update_many({"_id": int(id)}, {"$set": data})
        return make_response(jsonify({"msg": "User information updated successfully!"}))
    else:
        return make_response(jsonify({"error": "User not found"}))


@app.route("/deleteuser/<id>", methods=["delete"])
def delete_user(id):
    user_result = collection.find_one({"_id": int(id)})
    if user_result:
        collection.delete_one({"_id": int(id)})
        return make_response(jsonify({"msg": "User deleted successfully"}))
    else:
        return make_response(jsonify({"error": "User not found"}))
