dict_produtos = {}
class Produto:
    def __init__(self, produto, descricao, preco, custo):
        self.produto = int (produto)
        self.descricao = descricao
        self.preco = float (preco)
        self.custo = float (custo)

    def setProduto (self, produto):
        self.produto = produto
    def setDescricao (self, descricao):
        self.descricao = descricao
    def setPreco (self, preco):
        if preco <= self.preco * 1.1 and preco >= self.preco * 0.9:
            self.preco = preco
        else:
            print("preço invalido")

    def setCusto (self, custo):
        self.custo = custo

    def getProduto (self):
        return self.produto
    def getDescricao (self):
        return self.descricao
    def getPreco (self):
        return self.preco
    def getCusto (self):
        return self.custo
    
    def margemProduto(self):
        margem = (self.preco - self.custo) / self.preco * 100
        return margem



def menu():
    print("-----------------------------------------")
    print("Digite o que deseja:")
    print("1 - Cadastrar produto.")
    print("2 - Listar produtos.")
    print("3 - Calcular margem de um produto.")
    print("4 - Alterar dados de um produto.")
    print("5 - Sair.")
    print("-----------------------------------------")

while True:
    menu()
    opcao = input("\nDigite o número da opção desejada: ")
    
    match opcao:
        case "1":
            
            produto = int(input (f"\nDigite o codigo do produto: "))
            descricao = (input(f"Digite a descrição do produto: "))
            preco = float(input(f"Digite o preço do produto: "))
            custo = float(input(f"Digite o custo do produto: "))

            var_produto = Produto(produto, descricao, preco, custo)

            dict_produtos[produto] = var_produto
        
            print("Cadastrado!\n")

        case "2":

            for i in dict_produtos:
                codigo = dict_produtos[i].getProduto()
                descricao = dict_produtos[i].getDescricao()     
                preco = dict_produtos[i].getPreco()
                custo = dict_produtos[i].getCusto()
                print(f"Produto: {codigo}, Descrição: {descricao}, Preço: {preco}, Custo: {custo}")

        case "3":
            var_codigo = input("\nDigite o código do produto:\n")
            if int(var_codigo) in dict_produtos:
                margem = dict_produtos[var_codigo].margemProduto()
                print(f"A margem do produto é: {margem:.2f}%\n")
            else:
                print("Produto não encontrado.\n")

        case "4":
            print("---------------------------------------")
            print("1 - Alterar descrição do produto.")
            print("2 - Alterar preço do produto.")
            print("3 - Alterar custo do produto.")
            print("---------------------------------------")
            opcao_alterar = input("\nDigite o número da opção desejada: ")
