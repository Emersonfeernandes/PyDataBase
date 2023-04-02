import sqlite3
import json


class select:
      
    def __init__(self, var) -> None:
        self.var = var

        with open('database/nameBase.json', 'r') as json_file:
                read = json.load(json_file)
        name = read['name']
        conn = sqlite3.connect(f'{name}.db')
        self.cursor = conn.cursor()

    def all(self):
        self.cursor.execute(f'SELECT * FROM {self.var}')
        all_var = self.cursor.fetchall()
        
        return all_var
    
    def filtrar(self, *args):
        colunm = []
        for i in args:
            colunm.append(i)
        vir = ', '
        tupla = tuple(colunm)
        colunmName = vir.join(tupla)
        
        self.cursor.execute(f'SELECT {colunmName} FROM {self.var}')
        filtro = self.cursor.fetchall()
        
        return filtro
    
    def single(self, *args):
        colunm = []
        for i in args:
            colunm.append(i)
        vir = ', '
        tupla = tuple(colunm)
        colunmName = vir.join(tupla)
        
        self.cursor.execute(f'SELECT {colunmName} FROM {self.var}')
        single = self.cursor.fetchone()[0]
        
        return single
        