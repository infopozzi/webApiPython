from model.turma_model import listar, obter, salvar, alterar, excluir
from flask import Blueprint, jsonify, request
from config import db

turma_blueprint = Blueprint("turma", __name__)

@turma_blueprint.route("/obter/<int:id>")
def obter_turma(id):
    return jsonify(obter(id)), 200

@turma_blueprint.route("/listar", methods= ["GET"])
def listar_turma():
    return jsonify(listar()), 200

@turma_blueprint.route("/salvar", methods= ["POST"])
def salvar_turma():
    turma = request.json
    if (turma["id"] > 0):
        alterar(turma)
        return jsonify({ "message": "Turma alterado com sucesso."}), 200
    else: 
        salvar(turma)
        return jsonify({ "message": "Turma salvo com sucesso." }), 200
    
@turma_blueprint.route("/excluir", methods= ["POST"])
def excluir_turma():
    turma = request.json
    excluir(turma["id"])
    return jsonify({ "message": "Turma excluído com sucesso." }), 200