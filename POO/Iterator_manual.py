class Minha_lista:
    def __init__(self):
        self.__items = []
        self.__index = 0

    def add(self, valor):
        self.__items.append(valor)

    def __getitem__(self, index):
        return self.__items[index]

    def __setitem__(self, index, valor):
        if index >= len(self.__items):
            self.__items.append(valor)
        self.__items[index] = valor

