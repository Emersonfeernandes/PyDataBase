PRIMARY_KEY = 'INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT'

STRING = 'TEX' # Esta coluna captura todos os dados para NULL, TEXT ou BLOB.

INTERGER = 'INTEGER'

FLOAT = 'REAL' #é um valor de ponto flutuante, armazenado como um número flutuante de 8 bytes.

BLOB = 'BLOB' #É um conjunto de dados, armazenado exatamente como foi inserido.


NULL = 'NULL' #é um valor NULL

NOTNULL = 'NOT NULL' #Not Null Constraint é usado para indicar que a coluna nãopermitirá armazenar valores NULL

BOOLEAN = 'BOOLEAN'


FOREIGN_KEY = 'FOREIGN KEY'

REFERENCES = 'REFERENCES'

declarative_base = type('declarative_base', (), {})