from config import db

class Professor(db.Model):
    __tablename__ = 'professor'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    idade = db.Column(db.Integer)
    materia = db.Column(db.String(100))
    observacao = db.Column(db.String(200))
    turmas = db.relationship('Turma', backref='professor', lazy=True)

    def __init__(self, nome, idade, materia, observacao):
        self.nome = nome
        self.idade = idade
        self.materia = materia
        self.observacao = observacao

    def to_dic(self):
        return {"id": self.id, "nome": self.nome, "idade": self.idade, "materia": self.materia, "observacao": self.observacao}
    
class ProfessorNaoEncontrado(Exception):
    pass
    
def obter(id):
    professor = Professor.query.get(id)
    if not professor:
        raise ProfessorNaoEncontrado(f"Professor com ID {id} não foi encontrado.")
    return professor.to_dic()

def listar():
    professores = Professor.query.all()
    return [professor.to_dic() for professor in professores]

def salvar(dic):
    professor = Professor(nome = dic["nome"], idade = dic["idade"], materia = dic["materia"], observacao = dic["observacao"] )
    db.session.add(professor)
    db.session.commit()

def alterar(dic):
    professor = Professor.query.get(dic["id"])
    if not professor:
        raise ProfessorNaoEncontrado(f"Professor com ID {id} não foi encontrado.")
    professor.nome = dic["nome"]
    professor.idade = dic["idade"]
    professor.materia = dic["materia"]
    professor.observacao = dic["observacao"]
    db.session.commit()

def excluir(id):
    professor = Professor.query.get(id)
    if not professor:
        raise ProfessorNaoEncontrado(f"Professor com ID {id} não foi encontrado.")
    db.session.delete(professor)
    db.session.commit()