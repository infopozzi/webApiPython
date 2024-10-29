from config import db

class Aluno(db.Model):
    __tablename__ = 'alunos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    endereco = db.Column(db.String(200))
    turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'))

    def __init__(self, nome, endereco, turma_id):
        self.nome = nome
        self.endereco = endereco
        self.turma_id = turma_id

    def to_dic(self):
        return {"id": self.id, "nome": self.nome, "endereco": self.endereco, "turma_id": self.turma_id, "turma_nome":  self.turma.nome if self.turma else None}
    
def obter(id):
    aluno = Aluno.query.get(id)
    return aluno.to_dic()

def listar():
    alunos = Aluno.query.all()
    return [aluno.to_dic() for aluno in alunos]

def salvar(dic_aluno):
    aluno = Aluno(nome = dic_aluno["nome"], endereco = dic_aluno["endereco"], turma_id = dic_aluno["turma_id"])
    db.session.add(aluno)
    db.session.commit()

def alterar(dic_aluno):
    aluno = Aluno.query.get(dic_aluno["id"])
    aluno.nome = dic_aluno["nome"]
    aluno.endereco = dic_aluno["endereco"]
    db.session.commit()

def excluir(id):
    aluno = Aluno.query.get(id)
    db.session.delete(aluno)
    db.session.commit()