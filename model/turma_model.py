from config import db

class Turma(db.Model):
    __tablename__ = 'turmas'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    endereco = db.Column(db.String(200))
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'))
    alunos = db.relationship('Aluno', backref='turma', lazy=True)

    def __init__(self, nome, endereco, professor_id):
        self.nome = nome
        self.endereco = endereco
        self.professor_id = professor_id

    def to_dic(self):
        return {"id": self.id, "nome": self.nome, "endereco": self.endereco, "professor_nome": self.professor.nome if self.professor else None}
    

def obter(id):
    turma = Turma.query.get(id)
    return turma.to_dic()

def listar():
    turmas = Turma.query.all()
    return [turma.to_dic() for turma in turmas]

def salvar(dic_turma):
    turma = Turma(nome = dic_turma["nome"], endereco = dic_turma["endereco"], professor_id = dic_turma["professor_id"] )
    db.session.add(turma)
    db.session.commit()

def alterar(dic_turma):
    turma = Turma.query.get(dic_turma["id"])
    turma.nome = dic_turma["nome"]
    turma.endereco = dic_turma["endereco"]
    turma.professor_id = dic_turma["professor_id"]
    db.session.commit()

def excluir(id):
    turma = Turma.query.get(id)
    db.session.delete(turma)
    db.session.commit()