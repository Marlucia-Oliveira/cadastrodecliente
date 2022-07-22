#Nome: Marlucia Oliveira
#      Guilherme Costa
#Turma: Programador De Sistemas- Senac 2022

import cliente
opcao=5
clientes=[]
#Funcoes--------------------------------------------------
def pagina_inicial():
    print('❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄')
    print("Clique Na Opção Desejada")
    print('❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄')
    print('1- Cadastrar Cliente  '
          '2-Lista de Clientes Cadastrados '
          '3-Consultar Cliente')
    print('❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄')

def inserir():
        print("codigo:")
        codigo = input()
        print("Nome")
        nome = input()
        print("Idade")
        idade = input()
        print('CPF')
        cpf = input()
        print("Endereço")
        endereco = input()
        print("Contato")
        contato = input()
        print('Email')
        email = input()
        clienteOb = cliente.cliente(codigo, nome, idade, cpf, endereco, contato, email)
        print("Deseja salvar? s/n:")
        salv = input()
        if (salv == "s"):
            salvar(clienteOb)
def salvar(clienteOb):
    clientes.append(clienteOb)
    print("❄❄❄❄❄ Salvando....❄❄❄❄❄")
    print("❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄❄")
    print("❄❄❄❄❄ Salvo!  ❄❄❄❄❄\n")

def listar():
    print("❅❅❅❅❅❅❅❅Lista de Clientes Cadastrados❅❅❅❅❅❅❅❅\n")
    for i in range(0, len(clientes)):
        clientes[i].imprimir()
        print("voltar (aperte no enter)")
        retornar = input()

def consultar(cliente, self=None):
    identificador_desejado = input('codigo')
    for cliente in cliente:
        codigo, nome, idade, cpf, endereco, contato, email = cliente
        if codigo == identificador_desejado:
            print(f"|Cliente: {self.__codigo} |nome: {self.__nome}|idade: {self.__idade}| cpf: {self.__cpf}| endereço: {self.__endereço} | contato: {self.__contato} | email: {self.__email}")

while(opcao!=0):
    pagina_inicial()
    opcao=int(input())
    if opcao==1:
        inserir()
    elif opcao==2:
        listar()
    elif opcao==3:
        consultar(cliente)
    else:
        print('Opção inválida')












