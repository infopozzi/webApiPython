import os

from config import app,db

from professor.professor_routes import professor_blueprint
from turma.turma_routes import turma_blueprint
from alunos.aluno_routes import aluno_blueprint

app.register_blueprint(professor_blueprint, url_prefix = "/professor")
app.register_blueprint(turma_blueprint, url_prefix = "/turma")
app.register_blueprint(aluno_blueprint, url_prefix = "/aluno")

#instanciar tabelas na ordem correta para não dar problema nas chaves
from professor.professor_model import Professor
from turma.turma_model import Turma
from alunos.aluno_model import Aluno 

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=app.config["DEBUG"], port=app.config["PORT"])

