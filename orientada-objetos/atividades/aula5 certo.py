dict_editora = {}
dict_livro = {}

class Editora:
    
    def __init__(self, codigo_editora, razao_social, nome_contato, telefone):
        self.codigo_editora = codigo_editora
        self.razao_social = razao_social
        self.nome_contato = nome_contato
        self.telefone = telefone
    
    def getCodigoEditora(self):
        return self.codigo_editora
    
    def setCodigoEditora(self, codigo_editora):
        self.codigo_editora = codigo_editora
    
    def getRazaoSocial(self):
        return self.razao_social
    
    def setRazaoSocial(self, razao_social):
        self.razao_social = razao_social
    
    def getNomeContato(self):
        return self.nome_contato
    
    def setNomeContato(self, nome_contato):
        self.nome_contato = nome_contato
    
    def getTelefone(self):
        return self.telefone
    
    def setTelefone(self, telefone):
        self.telefone = telefone


class Livro:
    
    def __init__(self, codigo_livro, titulo_livro, isbn, editora):
        self.codigo_livro = codigo_livro
        self.titulo_livro = titulo_livro
        self.isbn = isbn
        self.editora = editora
    
    def getCodigoLivro(self):
        return self.codigo_livro
    
    def setCodigoLivro(self, codigo_livro):
        self.codigo_livro = codigo_livro
    
    def getTituloLivro(self):
        return self.titulo_livro
    
    def setTituloLivro(self, titulo_livro):
        self.titulo_livro = titulo_livro
    
    def getIsbn(self):
        return self.isbn
    
    def setIsbn(self, isbn):
        self.isbn = isbn
    
    def getEditora(self):
        return self.editora
    
    def setEditora(self, editora):
        self.editora = editora


def menu():
    print("-----------------------------------------")
    print("Digite o que deseja:")
    print("1 - Cadastrar editora.")
    print("2 - Cadastrar livro.")
    print("3 - pesquisar editora")
    print("4 - pesquisar livro.")
    print("5 - Sair.")
    print("-----------------------------------------")

while True:
    menu()
    opcao_menu = input("\nDigite o número da opção desejada: ")
    
    match opcao_menu:
        case "1":
            codigo_editora = int(input("digite o código da editora: "))
            razao_social = input("digite a razão social da editora: ")
            nome_contato = input("digite o nome do contato da editora: ")
            telefone = input("digite o telefone da editora: ")

            var_editora = Editora(codigo_editora, razao_social, nome_contato, telefone)
            dict_editora[codigo_editora] = var_editora

            print("\nCadastrado!\n")

        case "2":
            for i in dict_editora:
                codigo_editora = dict_editora[i].getCodigoEditora()
                razao_social = dict_editora[i].getRazaoSocial()
                telefone = dict_editora[i].getTelefone()
                nome_contato = dict_editora[i].getNomeContato()
                print(f"editora: {codigo_editora}, razão social: {razao_social}, nome do contato: {nome_contato}, telefone: {telefone}")

            editora_escolhida = input("digite o codigo")
                
            if int(editora_escolhida) in dict_editora:
                codigo_livro = int(input("digite o código do livro: "))
                titulo_livro = input("digite o título do livro: ")
                isbn = input("digite o ISBN do livro: ")
                var_livro = Livro(codigo_livro, titulo_livro, isbn, editora_escolhida)
                dict_livro[codigo_livro] = var_livro
            else:
                    print("editora não encontrada")