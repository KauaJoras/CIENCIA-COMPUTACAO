
class Montadora:
    def __init__(self, codigo, estado, razao_social):
        self.codigo = codigo
        self.estado = estado
        self.razao_social = razao_social


class Modelo:
    def __init__(self, codigo, nome, montadora):
        self.codigo = codigo
        self.nome = nome
        self.montadora = montadora


class Carro:
    def __init__(self, placa, modelo, ano):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano



montadoras = {}
modelos = {}
carros = {}



def cadastrar_montadora():
    print("\n CADASTRAR MONTADORA \n")

    codigo = int(input("Código: "))
    estado = input("Estado: ")
    razao_social = input("Razão social: ")

    montadoras[codigo] = Montadora(codigo, estado, razao_social)

    print("✔ Montadora cadastrada!\n")


def cadastrar_modelo():
    print("\n CADASTRAR MODELO \n")

    if not montadoras:
        print("Nenhuma montadora cadastrada.\n")
        return

    listar_montadoras()

    codigo_montadora = int(input("Código da montadora: "))

    if codigo_montadora not in montadoras:
        print("❌ Montadora não encontrada.\n")
        return

    codigo = int(input("Código do modelo: "))
    nome = input("Nome do modelo: ")

    modelos[codigo] = Modelo(codigo, nome, montadoras[codigo_montadora])

    print("✔ Modelo cadastrado!\n")


def cadastrar_carro():
    print("\n CADASTRAR CARRO \n")

    if not modelos:
        print("Nenhum modelo cadastrado.\n")
        return

    listar_modelos()

    codigo_modelo = int(input("Código do modelo: "))

    if codigo_modelo not in modelos:
        print("❌ Modelo não encontrado.\n")
        return

    placa = input("Placa: ")
    ano = int(input("Ano de fabricação: "))

    carros[placa] = Carro(placa, modelos[codigo_modelo], ano)

    print("✔ Carro cadastrado!\n")



def listar_montadoras():
    print("\n LISTA DE MONTADORAS \n")

    for m in montadoras.values():
        print(f"Código: {m.codigo} | Estado: {m.estado} | Nome: {m.razao_social}")


def listar_modelos():
    print("\n LISTA DE MODELOS \n")

    for m in modelos.values():
        print(f"Código: {m.codigo} | Nome: {m.nome} | Montadora: {m.montadora.razao_social}")


def listar_carros():
    print("\n LISTA DE CARROS \n")

    for c in carros.values():
        print(f"Placa: {c.placa} | Modelo: {c.modelo.nome} | Ano: {c.ano}")



def menu():
    print("""
----------------------------
1 - Cadastrar montadora
2 - Cadastrar modelo
3 - Cadastrar carro
4 - Listar montadoras
5 - Listar modelos
6 - Listar carros
7 - Sair
----------------------------
""")


def executar():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                cadastrar_montadora()
            case "2":
                cadastrar_modelo()
            case "3":
                cadastrar_carro()
            case "4":
                listar_montadoras()
            case "5":
                listar_modelos()
            case "6":
                listar_carros()
            case "7":
                print("Saindo...")
                break
            case _:
                print("Opção inválida!\n")


# ================== MAIN ==================

if __name__ == "__main__":
    executar()