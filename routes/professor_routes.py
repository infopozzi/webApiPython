from model.professor_model import listar, obter, salvar, alterar, excluir
from flask import Blueprint, jsonify, request
from config import db

professor_blueprint = Blueprint("professor", __name__)

@professor_blueprint.route("/obter/<int:id>")
def obter_professor(id):
    return jsonify(obter(id)), 200

@professor_blueprint.route("/listar", methods= ["GET"])
def listar_professor():
    return jsonify(listar()), 200

@professor_blueprint.route("/salvar", methods= ["POST"])
def salvar_professor():
    professor = request.json
    if (professor["id"] > 0):
        alterar(professor)
        return jsonify({ "message": "Professor alterado com sucesso."}), 200
    else: 
        salvar(professor)
        return jsonify({ "message": "Professor salvo com sucesso." }), 200
    
@professor_blueprint.route("/excluir", methods= ["POST"])
def excluir_professor():
    professor = request.json
    excluir(professor["id"])
    return jsonify({ "message": "Professor excluído com sucesso." }), 200