from config import db

class Professor(db.Model):
    __tablename__ = 'professores'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    endereco = db.Column(db.String(200))
    turmas = db.relationship('Turma', backref='professor', lazy=True)

    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def to_dic(self):
        return {"id": self.id, "nome": self.nome, "endereco": self.endereco}
    
def obter(id):
    professor = Professor.query.get(id)
    return professor.to_dic()

def listar():
    professores = Professor.query.all()
    return [professor.to_dic() for professor in professores]

def salvar(dic_professor):
    professor = Professor(nome = dic_professor["nome"], endereco = dic_professor["endereco"] )
    db.session.add(professor)
    db.session.commit()

def alterar(dic_professor):
    professor = Professor.query.get(dic_professor["id"])
    professor.nome = dic_professor["nome"]
    professor.endereco = dic_professor["endereco"]
    db.session.commit()

def excluir(id):
    professor = Professor.query.get(id)
    db.session.delete(professor)
    db.session.commit()