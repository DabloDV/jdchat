from flask import Blueprint, jsonify, redirect, request, url_for
import uuid
import re
#Entities
from models.entities.Usuario import Usuario
from routes.Usuario import nombre

#Modelos
from models.UsuarioModel import UsuarioModel

main=Blueprint('opciones_blueprint',__name__)

@main.route('/')
def camino():
    
    
    mensaje = "Oh. Así que tu nombre es "+nombre()+"..."
    return jsonify({'message': mensaje})

@main.route('/1')
def c1():
    mensaje = "Nada. Nada en lo absoluto... "+nombre()+"."
    return jsonify({'message': mensaje})
