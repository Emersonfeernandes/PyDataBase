import asyncio
from .createBase import Coluna


def relationships_create(*args):
    if len(Coluna().tupla) == 0:
        
        pass
    else:
    #await asyncio.sleep(5)
        relationships = args[0] + ' '+ f'({args[1]})' +' '+args[2]

        idTable = args[3].split('.')
        relationships += ' '+idTable[0]+ ' '+ f'({idTable[1]})'
        
        print(args)
        Coluna().tupla.append(relationships)
        #return relationships

async def await_colunas():
    try:
        await asyncio.wait_for(relationships_create(), timeout=None)
    except TimeoutError:
        print('timeout!')

#asyncio.run(relationships_create())

if __name__ == "__main__":
    pass