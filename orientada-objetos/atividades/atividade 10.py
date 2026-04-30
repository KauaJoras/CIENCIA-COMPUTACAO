class Empregado:
    def __init__(self,nome):
        self.nome = nome

    def retornaPagamento():
        pass

class Assalariado(Empregado):
    def __init__(self, salario):
        self.salario = salario

    def retornaPagamento(self):
        return self.salario
        
class Horista(Empregado):
    def __init__(self, valor_hora, horas_trabalhadas):
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas

    def retornaPagamento(self):
        return self.valor_hora * self.horas_trabalhadas
    
dict_empregados = {}
dict_assalariados = {}
dict_horistas = {}

def cadastrar_assalariado():
    nome = input("Digite o nome do assalariado: ")
    salario = float(input("Digite o salário do assalariado: "))
    assalariado = Assalariado(salario)
    dict_assalariados[nome] = assalariado
    dict_empregados[nome] = assalariado

def cadastrar_horista():
    nome = input("Digite o nome do horista: ")
    valor_hora = float(input("Digite o valor da hora do horista: "))
    horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas pelo horista: "))
    horista = Horista(valor_hora, horas_trabalhadas)
    dict_horistas[nome] = horista
    dict_empregados[nome] = horista

def calcular_pagamento():
    nome = input("Digite o nome do empregado para calcular o pagamento: ")
    if nome in dict_empregados:
        pagamento = dict_empregados[nome].retornaPagamento()
        print(f"O pagamento de {nome} é: {pagamento}")
    else:
        print("Empregado não encontrado.")

def gasto_total():
    total = 0
    for empregado in dict_empregados.values():
        total += empregado.retornaPagamento()
    print(f"O gasto total com salários é: {total}")
def main():
    while True:
        print("1. Cadastrar Assalariado")
        print("2. Cadastrar Horista")
        print("3. Calcular Pagamento")
        print("4. Gasto Total")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cadastrar_assalariado()
        elif escolha == '2':
            cadastrar_horista()
        elif escolha == '3':
            calcular_pagamento()
        elif escolha == '4':
            gasto_total()
        elif escolha == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")
if __name__ == "__main__":    
    main()
