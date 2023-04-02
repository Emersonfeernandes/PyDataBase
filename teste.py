from database.dataAcess import select
from testando import mytest, User, Inform


#var = select(Inform()).all()
#var = select(User()).filtrar('nome')
var1 = Inform().update('19', idade='ALTERANDO')
#print(mytest())

#print(select(mytest()).all())

print(select(Inform()).all())


