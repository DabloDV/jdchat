from flask import Blueprint, jsonify, redirect, request, url_for
import uuid
import re
#Entities
from models.entities.Usuario import Usuario

#Modelos
from models.UsuarioModel import UsuarioModel

main=Blueprint('usuario_blueprint',__name__)

@main.route('/')
def inicio():
    try:
        usuarios= UsuarioModel.get_usuarios()
        este= usuarios[0]
        nombre = este.get('nombre')
        nombre= re.sub(' +', '', nombre)
        if len(usuarios) < 1:
            return jsonify({'message': '¡Hola! Parece que eres nuev@ por aquí. ¿Por qué no comienzas por decirnos tu nombre?'}) #Si no hay un usuario, se crea uno de inmediato. Esto deberá coordinarse desde el frontend
        else:
            return jsonify({'message': '¡Bienvenid@, '+nombre+'!'})

    except Exception as ex:
        return jsonify({'message': str(ex)}),500


@main.route('/<id>')
def get_usuario(id):
    try:
        usuario= UsuarioModel.get_usuario(id)
        if usuario != None:
            return jsonify(usuario)
        else: 
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500



@main.route('/add',methods=['POST'])
def add_usuario():
    try:
        
        nombre=  request.json['nombre']
        id = uuid.uuid4() 
        usuario = Usuario(str(id), nombre) 
        affected_rows =  UsuarioModel.add_usuario(usuario)
        print(usuario.id)
        if affected_rows == 1:
            return jsonify({'message': "¿En serio? Ese nombre... Está muy bien, supongo..."})
        else:
            return jsonify({'message': "Hubo un error al crear tu nombre."}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}),500

@main.route('/update/<id>',methods=['PUT'])
def update_usuario(id):
    try:
        
        nombre=  request.json['nombre'] 
        usuario = Usuario(id, nombre) 
        affected_rows =  UsuarioModel.update_usuario(usuario)
        print(usuario.id)
        if affected_rows == 1:
            return jsonify(usuario.id)
        else:
            return jsonify({'message': "Error al actualizar nombre."}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}),500

@main.route('/delete/<id>',methods=['DELETE'])
def delete_usuario(id):
    try:
        usuario=Usuario(id)

        affected_rows=UsuarioModel.delete_usuario(usuario)

        if affected_rows == 1:
            return jsonify(usuario.id)
        else:
            return jsonify({'message': "No se pudo eliminar el usuario."}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}),500