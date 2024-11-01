from model.turma_model import listar, obter, salvar, alterar, excluir, TurmaNaoEncontado
from flask import Blueprint, jsonify, request
from config import db

turma_blueprint = Blueprint("turma", __name__)

@turma_blueprint.route("/obter/<int:id>", methods= ["GET"])
def obter_turma(id):
    try:
        turma = obter(id)
        return jsonify(turma), 200
    except TurmaNaoEncontado as e:
        return jsonify({ "message": str(e) }), 404

@turma_blueprint.route("/listar", methods= ["GET"])
def listar_turma():
    return jsonify(listar()), 200

@turma_blueprint.route("/salvar", methods= ["PUT","POST"])
def salvar_turma():
    try:
        turma = request.json
        if (turma["id"] > 0):
            alterar(turma)
            return jsonify({ "message": "Turma alterado com sucesso."}), 200
        else: 
            salvar(turma)
            return jsonify({ "message": "Turma cadastrada com sucesso." }), 200
    except TurmaNaoEncontado as e:
        return jsonify({ "message":str(e) }), 404
    
@turma_blueprint.route("/excluir", methods= ["DELETE","POST"])
def excluir_turma():
    try:
        turma = request.json
        excluir(turma["id"])
        return jsonify({ "message": "Turma excluído com sucesso." }), 200
    except TurmaNaoEncontado as e:
        return jsonify({ "message": str(e) }), 404