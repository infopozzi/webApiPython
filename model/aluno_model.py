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
        self.nota_primeiro_semestre = nota_primeiro_semestre if nota_primeiro_semestre else 0 
        self.nota_segundo_semestre = nota_segundo_semestre if nota_segundo_semestre else 0

    @property
    def idade(self):        
        hoje = datetime.today()
        idade_ = hoje.year - self.data_nascimento.year
        # Ajusta a idade se o aniversário ainda não ocorreu este ano
        if (hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day):
            idade_ -= 1
        return idade_
    
    @property
    def data_nascimento_en_us(self):
        return self.data_nascimento.strftime("%Y-%m-%d")

    @property
    def data_nascimento_pt_br(self):
        return self.data_nascimento.strftime("%d/%m/%Y")
    
    @property
    def turma_descricao(self):
        if (self.turma != None):
            return self.turma.descricao
        else:
            return ""
    
    @property
    def media_final(self):
        return (self.nota_primeiro_semestre + self.nota_segundo_semestre) /2

    def to_dic(self):
        return {"id": self.id, "nome": self.nome, "idade": self.idade, "data_nascimento_pt_br": self.data_nascimento_pt_br, "data_nascimento_en_us": self.data_nascimento_en_us,"turma_id": self.turma_id, "turma_nome":  self.turma_descricao, "nota_primeiro_semestre": self.nota_primeiro_semestre, "nota_segundo_semestre": self.nota_segundo_semestre, "media_final": self.media_final}

class AlunoNaoEncontrado(Exception):
    pass

def obter(id):
    aluno = Aluno.query.get(id)
    if not aluno:
        raise AlunoNaoEncontrado(f"Aluno com ID {id} não foi encontrado.")
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
        raise AlunoNaoEncontrado(f"Aluno com ID {id} não foi encontrado.")
    aluno.nome = dic["nome"]
    data_formatada = datetime.strptime(dic["data_nascimento"], "%Y-%m-%d").date()
    aluno.data_nascimento = data_formatada
    aluno.turma_id = dic["turma_id"]
    aluno.nota_primeiro_semestre = dic["nota_primeiro_semestre"] if dic["nota_primeiro_semestre"] else 0
    aluno.nota_segundo_semestre = dic["nota_segundo_semestre"] if dic["nota_segundo_semestre"] else 0
    db.session.commit()

def excluir(id):
    aluno = Aluno.query.get(id)
    if not aluno:
        raise AlunoNaoEncontrado(f"Aluno com ID {id} não foi encontrado.")
    db.session.delete(aluno)
    db.session.commit()