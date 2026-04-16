class Montadora:
    def __init__(self, codigo_montadora, estado, razao_social):
        self.codigo_montadora = codigo_montadora
        self.estado = estado
        self.razao_social = razao_social
    
    def setCodigoMontadora(self, codigo_montadora):
        self.codigo_montadora = codigo_montadora

    def setEstado(self, estado):
        self.estado = estado

    def setRazaoSocial(self, razao_social):
        self.RazaoSocial = razao_social

    def getCodigoMontadora(self):
        return self.codigo_montadora
    
    def getEstado(self):
        return self.estado
    
    def getRazaoSocial(self):
        return self.razao_social
    
class Modelo:
    def __init__(self, codigo_modelo, nome_modelo, montadora):
        self.codigo_modelo = codigo_modelo
        self.nome_modelo = nome_modelo
        self.montadora = montadora

    def setCodigoModelo(self, codigo_modelo):
        self.codigo_modelo = codigo_modelo

    def setNomeModelo(self, nome_modelo):
        self.nome_modelo = nome_modelo
    
    def setMontadora(self, montadora):
        self.montadora = montadora

    def getCodigoModelo(self):
        return self.codigo_modelo
    
    def getNomeModelo(self):
        return self.nome_modelo
    
    def getMontadora(self):
        return self.montadora
    
class Carro:
    def __init__(self, placa_carro, modelo, ano_fabricacao):
        self.placa_carro = placa_carro
        self.modelo = modelo
        self.ano_fabricacao = ano_fabricacao

    def setPlacaCarro(self, placa_carro):
        self.placa_carro = placa_carro
    
    def setModelo(self, modelo):
        self.modelo = modelo
    
    def setAnoFabricacao(self, ano_fabricacao):
        self.ano_fabricacao = ano_fabricacao
    
    def getPlacaCarro(self):
        return self.placa_carro

    def getModelo(self):
        return self.modelo
    
    def getAnoFabricacao(self):
        return self.ano_fabricacao
    

dict_montadora = {}
dict_modelo = {}
dict_carro = {}


def menu():
    print("-----------------------------------------")
    print("Digite o que deseja:")
    print("1 - Cadastrar montadora.")
    print("2 - Cadastrar modelo.")
    print("3 - Cadastrar carro.")
    print("4 - listar montadoras.")
    print("5 - listar modelos.")
    print("6 - listar carros.")
    print("7 - Sair.")
    print("-----------------------------------------")

while True:
    menu()
    opcao_menu = input("\nDigite o número da opção desejada: ")
    print("\n------------------------------------------\n")

    match opcao_menu:
        case "1":
            print("\n CADASTRAR MONTADORA \n")
            codigo_montadora = int(input("digite o código da montadora: "))
            estado = input("digite o estado da montadora: ")
            razao_social = input("digite a razão social da montadora: ")

            var_montadora = Montadora(codigo_montadora, estado, razao_social)
            dict_montadora[codigo_montadora] = var_montadora

            print("\nCadastrado!\n")

        case "2":
            print("\n CADASTRAR MODELO \n")
            for i in dict_montadora:
                codigo_montadora = dict_montadora[i].getCodigoMontadora()
                estado = dict_montadora[i].getEstado()
                razao_social = dict_montadora[i].getRazaoSocial()
                print(f"montadora: {codigo_montadora}, estado: {estado}, razão social: {razao_social}")
            
            montadora_escolhida = input("digite o codigo da montadora: ")

            if int(montadora_escolhida) in dict_montadora:
                codigo_modelo = int(input("digite o código do modelo: "))
                nome_modelo = input("digite o nome do modelo: ")

                var_modelo = Modelo(codigo_modelo, nome_modelo, dict_montadora[int(montadora_escolhida)])
                dict_modelo[codigo_modelo] = var_modelo

                print("\nCadastrado!\n")
            
            else:
                print("\nMontadora não encontrada, tente novamente.\n")

        case "3":
            print("\n CADASTRAR CARRO \n")
            for i in dict_modelo:
                codigo_modelo = dict_modelo[i].getCodigoModelo()
                nome_modelo = dict_modelo[i].getNomeModelo()
                montadora = dict_modelo[i].getMontadora().getRazaoSocial()
                print(f"modelo: {codigo_modelo}, nome do modelo: {nome_modelo}, montadora: {montadora}")

            modelo_escolhido = input("digite o codigo do modelo: ")

            if int(modelo_escolhido) in dict_modelo:
                placa = input("digite a placa do carro: ")
                ano_fabricacao =  int(input("digite o ano de fabricação do carro: "))

                var_carro = Carro(placa, dict_modelo[int(modelo_escolhido)], ano_fabricacao)
                dict_carro[placa] = var_carro

                print("\nCadastrado!\n")

            else:
                print("\nModelo não encontrado, tente novamente.\n")

        case "4":
            print("\n LISTAR MONTADORAS \n")
            for i in dict_montadora:
                codigo_montadora = dict_montadora[i].getCodigoMontadora()
                estado = dict_montadora[i].getEstado()
                razao_social = dict_montadora[i].getRazaoSocial()
                print(f"montadora: {codigo_montadora}, estado: {estado}, razão social: {razao_social}")
                
        case "5":
            print("\n LISTAR MODELOS \n")
            for i in dict_modelo:
                codigo_modelo = dict_modelo[i].getCodigoModelo()
                nome_modelo = dict_modelo[i].getNomeModelo()
                montadora = dict_modelo[i].getMontadora().getRazaoSocial()
                print(f"modelo: {codigo_modelo}, nome do modelo: {nome_modelo}, montadora: {montadora}")

        case "6":
            print("\n LISTAR CARROS \n")
            for i in dict_carro:
                placa = dict_carro[i].getPlacaCarro()
                modelo = dict_carro[i].getModelo().getNomeModelo()
                ano_fabricacao = dict_carro[i].getAnoFabricacao()
                print(f"carro: {placa}, modelo: {modelo}, ano de fabricação: {ano_fabricacao}")

        case "7":
            print("\nSaindo do programa, até mais!\n")
            break

print("\nPrograma encerrado.\n")