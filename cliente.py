class cliente():

    def __init__(self, codigo, nome, idade, cpf, endereço, contato, email):
        self.__codigo = codigo
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf
        self.__endereço = endereço
        self.__contato = contato
        self.__email = email

    def imprimir(self):
        print(f"|Cliente: {self.__codigo} |nome: {self.__nome}|idade: {self.__idade}| cpf: {self.__cpf}| endereço: {self.__endereço} | contato: {self.__contato} | email: {self.__email}")
        print('❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄')