from flask import jsonify, request
from app.models import SodaFan


def index():
    response = {'message': 'Hola SodaFan API-REST Flask 🐍'}
    return jsonify(response)


def get_all_temas():
    temas = SodaFan.get_all()
    return jsonify([tema.serialize() for tema in temas])


def get_tema(idtemas):
    tema = SodaFan.get_by_id(idtemas)
    if not tema:
        return jsonify({'message': 'TEMA not found!'})
    return jsonify(tema.serialize())


def create_tema():
    # obtengo los datos enviados en formato json - convierte en un diccionario python
    data = request.json
    new_tema = SodaFan(None, data['nombre'], data['albun'], data['creditos'])
    new_tema.save()
    response = {'message': 'Registro de Tema creado con exito'}
    return jsonify(response), 201


def update_tema(idtemas):
    tema = SodaFan.get_by_id(idtemas)
    if not tema:
        return jsonify({'message': 'Tema no encontrado'}), 404
    data = request.json
    tema.nombre = data['nombre']
    tema.albun = data['albun']
    tema.creditos = data['creditos']
    tema.save()
    return jsonify({'message': 'Tema updated successfully'})


def delete_tema(idtemas):
    tema = SodaFan.get_by_id(idtemas)
    if not tema:
        return jsonify({'message': 'Tema no encontrado'}), 404
    tema.delete()
    return jsonify({'message': 'Tema deleted successfully'})
