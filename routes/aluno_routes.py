from model.aluno_model import listar, obter, salvar, alterar, excluir
from flask import Blueprint, jsonify, request
from config import db

aluno_blueprint = Blueprint("aluno", __name__)

@aluno_blueprint.route("/obter/<int:id>")
def obter_aluno(id):
    return jsonify(obter(id)), 200

@aluno_blueprint.route("/listar", methods= ["GET"])
def listar_alunos():
    return jsonify(listar()), 200

@aluno_blueprint.route("/salvar", methods= ["POST"])
def salvar_aluno():
    aluno = request.json
    if (aluno["id"] > 0):
        alterar(aluno)
        return jsonify({ "message": "Aluno alterado com sucesso."}), 200
    else: 
        salvar(aluno)
        return jsonify({ "message": "Aluno salvo com sucesso." }), 200
    
@aluno_blueprint.route("/excluir", methods= ["POST"])
def excluir_aluno():
    aluno = request.json
    excluir(aluno["id"])
    return jsonify({ "message": "Aluno excluído com sucesso." }), 200