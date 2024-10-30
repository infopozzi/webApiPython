from config import db

class Turma(db.Model):
    __tablename__ = 'turmas'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(200))
    ativo = db.Column(db.Boolean)    
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'))
    alunos = db.relationship('Aluno', backref='turma', lazy=True)

    def __init__(self, descricao, professor_id, ativo):
        self.descricao = descricao
        self.professor_id = professor_id
        self.ativo = ativo
        
    def to_dic(self):
        return {"id": self.id, "descricao": self.descricao, "ativo": self.ativo, "professor_nome": self.professor.nome if self.professor else None}

class TurmaNaoEncontado(Exception):
    pass

def obter(id):
    turma = Turma.query.get(id)
    if not turma:
        raise TurmaNaoEncontado
    return turma.to_dic()

def listar():
    turmas = Turma.query.all()
    return [turma.to_dic() for turma in turmas]

def salvar(dic):
    turma = Turma(descricao = dic["descricao"], ativo = dic["ativo"], professor_id = dic["professor_id"])
    if not turma:
        raise TurmaNaoEncontado
    db.session.add(turma)
    db.session.commit()

def alterar(dic):
    turma = Turma.query.get(dic["id"])
    if not turma:
        raise TurmaNaoEncontado
    turma.descricao = dic["descricao"]
    turma.ativo = dic["ativo"]
    turma.professor_id = dic["professor_id"]
    db.session.commit()

def excluir(id):
    turma = Turma.query.get(id)
    if not turma:
        raise TurmaNaoEncontado
    db.session.delete(turma)
    db.session.commit()