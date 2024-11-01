from model.aluno_model import listar, obter, salvar, alterar, excluir,AlunoNaoEncontrado
from flask import Blueprint, jsonify, request
from config import db

aluno_blueprint = Blueprint("aluno", __name__)

@aluno_blueprint.route("/obter/<int:id>", methods= ["GET"])
def obter_aluno(id):
    try: 
        aluno = obter(id)
        return jsonify(aluno), 200
    except AlunoNaoEncontrado as e: 
        return jsonify({'message': str(e)}), 404 

@aluno_blueprint.route("/listar", methods= ["GET"])
def listar_alunos():
    return jsonify(listar()), 200

@aluno_blueprint.route("/salvar", methods= ["POST"])
def cadastrar_aluno():
    try:
        aluno = request.json
        salvar(aluno)
        return jsonify({ "message": "Aluno cadastrado com sucesso." }), 200
    except AlunoNaoEncontrado as e:
        return jsonify({ "message": str(e) }), 404    

@aluno_blueprint.route("/alterar", methods= ["PUT","POST"])
def alterar_aluno():
    try:
        aluno = request.json
        if (aluno["id"] > 0):
            alterar(aluno)
            return jsonify({ "message": "Aluno alterado com sucesso."}), 200   
        else:
            return jsonify({ "message": "Id do Aluno inválido."}), 404   
    except AlunoNaoEncontrado as e:
        return jsonify({ "message": str(e) }), 404  
    
@aluno_blueprint.route("/excluir", methods= ["DELETE","POST"])
def excluir_aluno():
    try:
        aluno = request.json
        excluir(aluno["id"])
        return jsonify({ "message": "Aluno excluído com sucesso." }), 200
    except AlunoNaoEncontrado as e:
        return jsonify({ "message": str(e) }), 404    