from config import db
from datetime import datetime

class Aluno(db.Model):
    __tablename__ = 'alunos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))   
    data_nascimento = db.Column(db.Date)
    turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'))
    nota_primeiro_semestre = db.Column(db.Float)
    nota_segundo_semestre = db.Column(db.Float)

    def __init__(self, nome, data_nascimento, turma_id, nota_primeiro_semestre, nota_segundo_semestre):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.turma_id = turma_id
        self.nota_primeiro_semestre = nota_primeiro_semestre 
        self.nota_segundo_semestre = nota_segundo_semestre

    @property
    def idade(self):        
        hoje = datetime.today()
        idade_ = hoje.year - self.data_nascimento.year
        # Ajusta a idade se o aniversário ainda não ocorreu este ano
        if (hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day):
            idade_ -= 1
        return idade_
    
    @property
    def data_nascimento_(self):
        return self.data_nascimento.strftime("%Y-%m-%d") if self.data_nascimento else ""

    @property
    def media_final(self):
        return (self.nota_primeiro_semestre + self.nota_segundo_semestre) /2

    def to_dic(self):
        return {"id": self.id, "nome": self.nome, "idade": self.idade, "data_nascimento": self.data_nascimento.strftime("%d/%m/%Y"), "data_nascimento_": self.data_nascimento_,"turma_id": self.turma_id, "turma_nome":  self.turma.descricao, "nota_primeiro_semestre": self.nota_primeiro_semestre, "nota_segundo_semestre": self.nota_segundo_semestre, "media_final": self.media_final}

class AlunoNaoEncontrado(Exception):
    pass

def obter(id):
    aluno = Aluno.query.get(id)
    if not aluno:
        raise
    return aluno.to_dic()

def listar():
    alunos = Aluno.query.all()
    return [aluno.to_dic() for aluno in alunos]

def salvar(dic):
    data_formatada = datetime.strptime(dic["data_nascimento"], "%Y-%m-%d").date()
    aluno = Aluno(nome = dic["nome"], data_nascimento = data_formatada, turma_id = dic["turma_id"], nota_primeiro_semestre = dic["nota_primeiro_semestre"], nota_segundo_semestre = dic["nota_segundo_semestre"])
    db.session.add(aluno)
    db.session.commit()

def alterar(dic):
    aluno = Aluno.query.get(dic["id"])
    if not aluno:
        raise
    aluno.nome = dic["nome"]
    data_formatada = datetime.strptime(dic["data_nascimento"], "%Y-%m-%d").date()
    aluno.data_nascimento = data_formatada
    aluno.turma_id = dic["turma_id"]
    aluno.nota_primeiro_semestre = dic["nota_primeiro_semestre"]
    aluno.nota_segundo_semestre = dic["nota_segundo_semestre"]
    db.session.commit()

def excluir(id):
    aluno = Aluno.query.get(id)
    if not aluno:
        raise
    db.session.delete(aluno)
    db.session.commit()