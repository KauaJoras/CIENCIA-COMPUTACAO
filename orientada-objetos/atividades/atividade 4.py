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
                print(f"Produto: {codigo}, Descrição: {descricao}, Preço: R${preco:.2f}, Custo: R${custo:.2f}")

        case "3":
            var_codigo = input("\nDigite o código do produto:\n")
            codigo_int = int(var_codigo)
            if codigo_int in dict_produtos:
                margem = dict_produtos[codigo_int].margemProduto()
                print(f"A margem do produto é: {margem:.2f}%\n")
            else:
                print("Produto não encontrado.\n")

        case "4":
            produto_alt = int(input("Digite o código do produto que deseja alterar:\n"))
            while True:
                print("\n---------------------------------------")
                print("1 - Alterar descrição do produto.")
                print("2 - Alterar preço do produto.")
                print("3 - Alterar custo do produto.")
                print("4 - Voltar ao menu principal.")
                print("---------------------------------------")
                opcao_alterar = input("\nDigite o número da opção desejada: ")

                match opcao_alterar:
                    case "1":
                        print(f"Digite a nova descrição do produto: {dict_produtos[produto_alt].getProduto()}")
                        print(f"A descrição atual é: {dict_produtos[produto_alt].getDescricao()}")
                        nova_descricao = input("")
                        dict_produtos[produto_alt].setDescricao(nova_descricao)
                        print("Descrição alterada!\n")
                    case "2":
                        print(f"Digite o novo preço do produto: {dict_produtos[produto_alt].getProduto()}")
                        print(f"O preço atual é: R${dict_produtos[produto_alt].getPreco():.2f}")
                        novo_preco = float(input(""))
                        dict_produtos[produto_alt].setPreco(novo_preco)
                        print("Preço alterado!\n")
                    case "3":
                        print(f"Digite o novo custo do produto: {dict_produtos[produto_alt].getProduto()}")
                        print(f"O custo atual é: R${dict_produtos[produto_alt].getCusto():.2f}")
                        novo_custo = float(input(""))
                        dict_produtos[produto_alt].setCusto(novo_custo)
                        print("Custo alterado!\n")
                    case "4":
                        break

        case "5":
            print("Saindo...")
            break
