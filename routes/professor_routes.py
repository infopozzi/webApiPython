from model.professor_model import listar, obter, salvar, alterar, excluir, ProfessorNaoEncontrado
from flask import Blueprint, jsonify, request
from config import db

professor_blueprint = Blueprint("professor", __name__)

@professor_blueprint.route("/obter/<int:id>", methods= ["GET"])
def obter_professor(id):
    try:
        professor = obter(id)
        return jsonify(professor), 200
    except ProfessorNaoEncontrado as e:
        return jsonify({ "message": str(e)} ), 404

@professor_blueprint.route("/listar", methods= ["GET"])
def listar_professor():
    return jsonify(listar()), 200

@professor_blueprint.route("/salvar", methods= ["PUT","POST"])
def salvar_professor():
    try:
        professor = request.json
        if (professor["id"] > 0):
            alterar(professor)
            return jsonify({ "message": "Professor alterado com sucesso."}), 200
        else: 
            salvar(professor)
            return jsonify({ "message": "Professor cadastrado com sucesso." }), 200
    except ProfessorNaoEncontrado as e:
        return jsonify({ "message": str(e) }), 404
    
@professor_blueprint.route("/excluir", methods= ["DELETE","POST"])
def excluir_professor():
    try:
        professor = request.json
        excluir(professor["id"])
        return jsonify({ "message": "Professor excluído com sucesso." }), 200
    except ProfessorNaoEncontrado as e:
        return jsonify({ "message": str(e) }), 404


