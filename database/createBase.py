import sqlite3
import json


_tableName_ = 'mytable2'

class Coluna:
    tupla = []
    def __init__(self, var=None, *args):
        self.var = var
        self.args = args
        self.num = 0
        
    def __get__(self, instance, owner):
        if instance is None: return self
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value
    
    def __set_name__(self, owner, name):
        if self.var == 'FOREIGN KEY':
            relationships = self.var + ' '+ f'({self.args[0]})' +' '+self.args[1]

            idTable = self.args[2].split('.')
            relationships += ' '+idTable[0]+ ' '+ f'({idTable[1]})'
            self.tupla.append(relationships)

        else:
            if not self.args:
                self.name = name + ' '+ self.var
                self.tupla.append(self.name)
                
            else:
                self.name = name + ' '+ self.var+' '+self.args[0]
                self.tupla.append(self.name)

        vir = ', '
        t = (tuple(self.tupla))
        st = vir.join(t)
                
        read = {f"{_tableName_}":f'({st});'}
        with open('database/createTable.json', 'w') as json_file:
            json.dump(read, json_file, indent=4)
            
        print(self.tupla)
        
        self.num +=1 
  

def createBase(var):
    conn = sqlite3.connect(f'{var}.db')
    dados = {'name':var}
    with open('database/nameBase.json', 'w') as json_file:
        json.dump(dados, json_file, indent=4)


class Base:
   
    def __init_subclass__(cls, **args):
        cls._tableName_ = cls._tableName_

        cls.clear_()

        with open('database/nameBase.json', 'r') as json_file:
            read = json.load(json_file)
        name = read['name']
        cls.conn = sqlite3.connect(f'{name}.db')

        cls.cursor = cls.conn.cursor()        
    
    def createTable(cls=None):
        with open('database/nameBase.json', 'r') as json_file:
            read = json.load(json_file)
        name = read['name']
        conn = sqlite3.connect(f'{name}.db')
        
        with open('database/createTable.json', 'r') as json_file:
            colunas = json.load(json_file)
        colunm = colunas['mytable2']
        
        
        conn.execute(f"CREATE TABLE if not exists {cls._tableName_}{colunm}")

        conn.close()
        print('PRONTO')
        Coluna().tupla.clear()
    
    def clear_():
        Coluna().tupla.clear()
        print('FUNCIONA')
    def dataBase(cls, **kwargs):

        vir = ', '
        t = (tuple(kwargs.keys()))
        colunmName = vir.join(t)

        values = tuple(kwargs.values())

        cls.conn.execute(f"INSERT INTO {cls._tableName_}({colunmName}) VALUES {values}")

        cls.conn.commit()
        Coluna().tupla.clear()

    def update(cls, var, **kwargs):
         key = (tuple(kwargs.keys()))
         colunm = key[0]
         value = tuple(kwargs.values())[0]
         
         cls.cursor.execute(f'UPDATE {cls._tableName_} SET {colunm}=? WHERE {colunm} = "{var}";', (value,))
         cls.conn.commit()
         Coluna().tupla.clear()         

    def delete(cls, **kwargs):
         key = (tuple(kwargs.keys()))
         colunm = key[0]
         value = tuple(kwargs.values())[0]
         
         cls.cursor.execute(f"DELETE FROM {cls._tableName_} WHERE {colunm} = ?", (value,))
         cls.conn.commit()
         Coluna().tupla.clear()

    def newColunm(cls, **kwargs):
         key = (tuple(kwargs.keys()))
         colunm = key[0]
         value = tuple(kwargs.values())[0]
         
         cls.cursor.execute(f"ALTER TABLE {cls._tableName_} ADD COLUNM {colunm} {value};")
         cls.conn.commit()
         Coluna().tupla.clear()

    def __str__(cls) -> str:
        Coluna().tupla.clear()
        #cls.cursor.execute(f'SELECT * FROM {cls._tableName_}')
        #names = list(map(lambda x: x[0], cls.cursor.description))
        return cls._tableName_
    
    def __call__(self):
        print("Instance is called via special method")



if __name__ == "__main__":
    pass