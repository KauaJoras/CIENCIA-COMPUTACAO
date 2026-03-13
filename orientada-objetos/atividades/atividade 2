class Pessoa: 
        def __init__(self, nome, idade, endereco, sexo): 
            self.nome = nome 
            self.idade = idade 
            self.endereco = endereco
            self.sexo = sexo
        def setNome(self, nome): 
            self.nome = nome 
        def setIdade(self, idade):
            if idade >= self.idade:
                self.idade = idade
            else:
                print(f"a idade {idade} é menor do que a idade original de {self.nome}, ação inválida, tente novamente")
        def setEndereco(self, endereco): 
            self.endereco = endereco 
        def setSexo(self, sexo): 
            self.sexo = sexo 
        def getNome(self): 
            return self.nome 
        def getIdade(self): 
            return self.idade
        def getEndereco(self): 
            return self.endereco 
        def getSexo(self): 
            return self.sexo      
    
usuarios = []  

for i in range(3):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    endereco = input("Digite o endereço da pessoa: ")
    sexo = input("Digite o sexo da pessoa: ")
    pessoa = Pessoa(nome, idade, endereco, sexo)
    usuarios.append(pessoa)



print (p1.getNome())
print (p1.getIdade())
p1.setIdade(20)
print (p1.getIdade())
print (p2.getEndereco())
print (p3.getSexo())
