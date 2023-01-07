from flask import Blueprint, jsonify, redirect, request, url_for
import uuid
import re
#Entities
from models.entities.Usuario import Usuario

#Modelos
from models.UsuarioModel import UsuarioModel

main=Blueprint('opciones_blueprint',__name__)

usuarios= UsuarioModel.get_usuarios()
este= usuarios[0]
nombre = este.get('nombre')
nombre= re.sub(' +', '', nombre)

@main.route('/')
def camino():
    
    
    mensaje = "Oh. Así que tu nombre es "+nombre+"..."
    return jsonify({'message': mensaje})

@main.route('/1')
def c1():
    mensaje = "Nada. Nada en lo absoluto... "+nombre+"."
    return jsonify({'message': mensaje})
