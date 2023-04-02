from asyncio import coroutine, get_event_loop

import asyncio

declarative_base = type('declarative_base', (), {'name':'Emerson'})
class Teste:

    def __init_subclass__(cls, **args):
        cls._name_ = cls._name_
        print(cls._name_)
    


class Nova(Teste):
    _name_ = 'OLÁ'
    def __init__(self):
        self.name = 'OI'
        #print("Instance Created")
      
    def test(self):
        print('TESTE')
    def __call__(self):
        print("Instance is called via special method")

class Nova1(Teste):
    _name_ = 'OLÁ_oi'
    def __init__(self):
        self.name = 'OI'
        #print("Instance Created")
      
    def test(self):
        print('TESTE')
    def __call__(self):
        print("Instance is called via special method")
#print(t.__dict__.keys())
#print(t.__dict__.values())
#print(t.__dict__)
l = [Nova1(), Nova()]
for i in l:
    i()