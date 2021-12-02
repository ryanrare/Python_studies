class Humano:
    def __init__(self, nome):
        self.nome = nome


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome =  nome

    @property
    def sobrenome(self):
        return 'Victor'

h1 = Humano('Ryan')
print(h1.nome)
print(h1.sobrenome)