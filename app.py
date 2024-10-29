import os

from config import app,db

from routes.professor_routes import professor_blueprint
from routes.turma_routes import turma_blueprint
from routes.aluno_routes import aluno_blueprint

app.register_blueprint(professor_blueprint, url_prefix = "/professor")
app.register_blueprint(turma_blueprint, url_prefix = "/turma")
app.register_blueprint(aluno_blueprint, url_prefix = "/aluno")

#instanciar tabelas na ordem correta para não dar problema nas chaves
from model.professor_model import Professor
from model.turma_model import Turma
from model.aluno_model import Aluno 

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=app.config["DEBUG"], port=app.config["PORT"])

