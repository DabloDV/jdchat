from flask import Blueprint, jsonify, request
import uuid
#Entities
from models.entities.Usuario import Usuario

#Modelos
from models.UsuarioModel import UsuarioModel

main=Blueprint('usuario_blueprint',__name__)

@main.route('/')
def get_usuarios():
    try:
        usuarios= UsuarioModel.get_usuarios()
        return jsonify(usuarios)
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
        
        pais=  request.json['pais']
        id = uuid.uuid4() 
        usuario = Usuario(str(id), pais) 
        affected_rows =  UsuarioModel.add_usuario(usuario)
        print(usuario.id)
        if affected_rows == 1:
            return jsonify(usuario.id)
        else:
            return jsonify({'message': "Error al crear"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}),500

@main.route('/update/<id>',methods=['PUT'])
def update_usuario(id):
    try:
        
        pais=  request.json['pais'] 
        usuario = Usuario(id, pais) 
        affected_rows =  UsuarioModel.update_usuario(usuario)
        print(usuario.id)
        if affected_rows == 1:
            return jsonify(usuario.id)
        else:
            return jsonify({'message': "Error al actualizar país."}), 500

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