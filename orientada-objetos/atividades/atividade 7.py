class Funcionario:
    def __init__(self, nome, cpf, salario, departamento):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.departamento = departamento

    def bonificar(self):
        self.salario += self.salario * 0.10
        print(f"Bonificação de 10% aplicada. Novo salário de {self.nome}: R$ {self.salario:.2f}")

    def __str__(self):
        return (f"Nome: {self.nome} | CPF: {self.cpf} | "
                f"Salário: R$ {self.salario:.2f} | Departamento: {self.departamento}")


class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, departamento, senha, num_funcionarios_gerenciados):
        super().__init__(nome, cpf, salario, departamento)
        self.senha = senha
        self.num_funcionarios_gerenciados = num_funcionarios_gerenciados

    def autenticarSenha(self, senha):
        return self.senha == senha

    def bonificar(self):
        self.salario += self.salario * 0.15
        print(f"Bonificação de 15% aplicada. Novo salário de {self.nome}: R$ {self.salario:.2f}")

    def __str__(self):
        return (super().__str__() +
                f" | Funcionários Gerenciados: {self.num_funcionarios_gerenciados}")


class Vendedor(Funcionario):
    def __init__(self, nome, cpf, salario, departamento, quantidade_vendas, comissao):
        super().__init__(nome, cpf, salario, departamento)
        self.quantidade_vendas = quantidade_vendas
        self.comissao = comissao

    def atualizaQuantidadeVendas(self, quantidade):
        self.quantidade_vendas += quantidade
        print(f"Quantidade de vendas atualizada. Total de vendas de {self.nome}: {self.quantidade_vendas}")

    def calculaSalario(self):
        salario_total = self.salario + self.comissao
        print(f"Salário de {self.nome}: R$ {self.salario:.2f} + Comissão: R$ {self.comissao:.2f} = R$ {salario_total:.2f}")
        return salario_total

    def __str__(self):
        return (super().__str__() +
                f" | Qtd. Vendas: {self.quantidade_vendas} | Comissão: R$ {self.comissao:.2f}")


funcionarios = []
gerentes = []
vendedores = []


def cadastrar_funcionario():
    print("\n--- Cadastrar Funcionário ---")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    salario = float(input("Salário: R$ "))
    departamento = input("Departamento: ")
    f = Funcionario(nome, cpf, salario, departamento)
    funcionarios.append(f)
    print("Funcionário cadastrado com sucesso!")


def cadastrar_gerente():
    print("\n--- Cadastrar Gerente ---")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    salario = float(input("Salário: R$ "))
    departamento = input("Departamento: ")
    senha = input("Senha: ")
    num_func = int(input("Número de funcionários gerenciados: "))
    g = Gerente(nome, cpf, salario, departamento, senha, num_func)
    gerentes.append(g)
    print("Gerente cadastrado com sucesso!")


def cadastrar_vendedor():
    print("\n--- Cadastrar Vendedor ---")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    salario = float(input("Salário: R$ "))
    departamento = input("Departamento: ")
    qtd_vendas = int(input("Quantidade de vendas: "))
    comissao = float(input("Comissão: R$ "))
    v = Vendedor(nome, cpf, salario, departamento, qtd_vendas, comissao)
    vendedores.append(v)
    print("Vendedor cadastrado com sucesso!")


def selecionar_funcionario():
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        return None
    print("\nFuncionários disponíveis:")
    for i, f in enumerate(funcionarios):
        print(f"  {i + 1} - {f.nome}")
    idx = int(input("Selecione o número do funcionário: ")) - 1
    if 0 <= idx < len(funcionarios):
        return funcionarios[idx]
    print("Opção inválida.")
    return None


def selecionar_gerente():
    if not gerentes:
        print("Nenhum gerente cadastrado.")
        return None
    print("\nGerentes disponíveis:")
    for i, g in enumerate(gerentes):
        print(f"  {i + 1} - {g.nome}")
    idx = int(input("Selecione o número do gerente: ")) - 1
    if 0 <= idx < len(gerentes):
        return gerentes[idx]
    print("Opção inválida.")
    return None


def selecionar_vendedor():
    if not vendedores:
        print("Nenhum vendedor cadastrado.")
        return None
    print("\nVendedores disponíveis:")
    for i, v in enumerate(vendedores):
        print(f"  {i + 1} - {v.nome}")
    idx = int(input("Selecione o número do vendedor: ")) - 1
    if 0 <= idx < len(vendedores):
        return vendedores[idx]
    print("Opção inválida.")
    return None


def bonificar_funcionario():
    print("\n--- Bonificar Funcionário ---")
    f = selecionar_funcionario()
    if f:
        f.bonificar()


def bonificar_gerente():
    print("\n--- Bonificar Gerente ---")
    g = selecionar_gerente()
    if g:
        g.bonificar()


def autenticar_senha_gerente():
    print("\n--- Autenticar Senha do Gerente ---")
    g = selecionar_gerente()
    if g:
        senha = input("Digite a senha: ")
        if g.autenticarSenha(senha):
            print("Senha autenticada com sucesso!")
        else:
            print("Senha incorreta.")


def atualizar_quantidade_vendas():
    print("\n--- Atualizar Quantidade de Vendas ---")
    v = selecionar_vendedor()
    if v:
        qtd = int(input("Quantidade de vendas a adicionar: "))
        v.atualizaQuantidadeVendas(qtd)


def calcular_salario_vendedor():
    print("\n--- Calcular Salário do Vendedor ---")
    v = selecionar_vendedor()
    if v:
        v.calculaSalario()


def listar_funcionarios():
    print("\n--- Listar Funcionários ---")
    nome = input("Nome do funcionário (deixe em branco para listar todos): ").strip()
    encontrados = [f for f in funcionarios if nome.lower() in f.nome.lower()] if nome else funcionarios
    if not encontrados:
        print("Nenhum funcionário encontrado.")
    for f in encontrados:
        print(f)


def listar_gerentes():
    print("\n--- Listar Gerentes ---")
    nome = input("Nome do gerente (deixe em branco para listar todos): ").strip()
    encontrados = [g for g in gerentes if nome.lower() in g.nome.lower()] if nome else gerentes
    if not encontrados:
        print("Nenhum gerente encontrado.")
    for g in encontrados:
        print(g)


def listar_vendedores():
    print("\n--- Listar Vendedores ---")
    nome = input("Nome do vendedor (deixe em branco para listar todos): ").strip()
    encontrados = [v for v in vendedores if nome.lower() in v.nome.lower()] if nome else vendedores
    if not encontrados:
        print("Nenhum vendedor encontrado.")
    for v in encontrados:
        print(v)


def menu():
    opcoes = {
        "1": cadastrar_funcionario,
        "2": cadastrar_gerente,
        "3": cadastrar_vendedor,
        "4": bonificar_funcionario,
        "5": bonificar_gerente,
        "6": autenticar_senha_gerente,
        "7": atualizar_quantidade_vendas,
        "8": calcular_salario_vendedor,
        "9": listar_funcionarios,
        "10": listar_gerentes,
        "11": listar_vendedores,
    }

    while True:
        print("\n========== MENU ==========")
        print("1  - Cadastrar Funcionário")
        print("2  - Cadastrar Gerente")
        print("3  - Cadastrar Vendedor")
        print("4  - Bonificar Funcionário")
        print("5  - Bonificar Gerente")
        print("6  - Autenticar Senha do Gerente")
        print("7  - Atualizar Quantidade de Vendas do Vendedor")
        print("8  - Calcular Salário do Vendedor")
        print("9  - Listar Funcionários")
        print("10 - Listar Gerentes")
        print("11 - Listar Vendedores")
        print("0  - Sair")
        print("==========================")

        escolha = input("Escolha uma opção: ").strip()

        if escolha == "0":
            print("Encerrando o sistema. Até logo!")
            break
        elif escolha in opcoes:
            opcoes[escolha]()
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
