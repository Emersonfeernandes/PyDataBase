from database.createBase import Base, Coluna, createBase
from database.data_var import PRIMARY_KEY, NOTNULL, FOREIGN_KEY, REFERENCES, declarative_base
from database.relation import relationships_create

createBase('mybanco')
base = declarative_base
class mytest(Base):
    _tableName_ = 'tabela'
    id = Coluna(PRIMARY_KEY)
    minhaVariavel = Coluna('TEXT', NOTNULL)
    minhaVariavel2 = Coluna('TEXT', NOTNULL)
    
    


#mytest().dataBase(minhaVariavel='NOVO', minhaVariavel2='TESTE')
#mytest().createTable()

class User(Base):
    _tableName_ = 'NOVA_tabela'
    id = Coluna(PRIMARY_KEY)
    nome = Coluna('TEXT', NOTNULL)
    sobrenome = Coluna('TEXT', NOTNULL)

#User().dataBase(nome='Marcos',sobrenome='Lima')

class Inform(Base):
    _tableName_ = 'TABELAO'
    id = Coluna(PRIMARY_KEY)
    idade = Coluna('TEXT', NOTNULL)
    email = Coluna('TEXT', NOTNULL)
    #user = Coluna(FOREIGN_KEY,('id'), REFERENCES, ('NOVA_tabela.id'))
    #relationships_create(FOREIGN_KEY,('id'), REFERENCES, ('NOVA_tabela.id'))
#Inform().dataBase(idade='19',email='carlos_@email.com')

if __name__ == "__main__":
    pass
