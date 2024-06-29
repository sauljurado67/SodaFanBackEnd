from flask import jsonify, request
from app.modUser import UserFan


def index_user():
    response = {'message': 'Hola UserFan API-REST Flask 🐍'}
    return jsonify(response)


def get_all_users():
    users = UserFan.get_all_user()
    return jsonify([user.serialize() for user in users])


def get_user(id):
    user = UserFan.get_by_idUser(id)
    if not user:
        return jsonify({'message': 'User not found!'})
    return jsonify(user.serialize())


def create_user():
    # obtengo los datos enviados en formato json - convierte en un diccionario python
    if request.method == 'POST':
        data = request.json
        new_user = UserFan(None, data['nombre'],
                           data['email'], data['password'])
        new_user.saveUser()
        response = {'message': 'Registro de tema creado con exito'}
        return jsonify(response), 201
    elif request.method == 'GET':
        users = UserFan.get_all_user()
        return jsonify([user.serialize() for user in users])


def update_user(id):
    user = UserFan.get_by_idUser(id)
    if not user:
        return jsonify({'message': 'User no encontrado'}), 404
    data = request.json
    user.nombre = data['nombre']
    user.email = data['email']
    user.password = data['password']
    user.saveUser()
    return jsonify({'message': 'Tema updated successfully'})


def delete_user(id):
    user = UserFan.get_by_idUser(id)
    if not user:
        return jsonify({'message': 'User no encontrado'}), 404
    user.deleteUser()
    return jsonify({'message': 'User deleted seccessfully'})
