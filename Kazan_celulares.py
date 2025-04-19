import time
import os
#Definindo as funções:
class Organizar_codigo:
    def load():
        a = ["carregando.",".","."]
        for i in range(len(a)):
            print(a[i], end="", flush = True) #Dá um print em cada elemento na mesma linha depois de um tempo determinado
            time.sleep(0.5)
        os.system("cls") #Limpa o terminal após dar um print na lista
    #Mesmo esquema do load
    def inicio():
        a = ["Iniciando.",".","."] 
        for i in range(len(a)):
            print(a[i], end="", flush = True)
            time.sleep(0.5)
        os.system("cls")
    #Mesmo esquema do load
    def final():
        a = ["encerrando.",".","."] 
        for i in range(len(a)):
            print(a[i], end = "", flush = True)
            time.sleep(0.5)
        os.system("cls")
    #Cria um menu simples
    def menu():
        print("=======MENU=======")
        time.sleep(0.5)
        print(""">Registrar
>Imprimir
>Buscar
>Eliminar
>Sair\n""")

class Registro:
    #A lista com os registros
    def __init__(self):
        self.Registro = []
    #Adicionando os valores de cada chave do registro
    def criar_registro(self, nome, codigo, marca, preco):
        produto = {
            'nome' : nome,
            'código' : codigo,
            'marca' : marca,
            'preço' : preco
        }
        self.Registro.append(produto)
    #Dá um print em todos os registros que tem na lista
    def imprimir_tudo(self):
        print(">Todos os registros:")
        for registro in self.Registro:
            print(f"Celular: {registro['nome']}\nCódigo: {registro['código']}\nMarca: {registro['marca']}\nPreço: {registro['preço']}\n")
    #Dá um print em uma parte da lista
    def imprimir_trecho(self, inicio, fim):
        print(f">Do {inicio+1}º até o {fim}º registro:")
        for produto in self.Registro[inicio:fim]:
            print(f"Celular: {produto['nome']}\nCódigo: {produto['código']}\nMarca: {produto['marca']}\nPreço: {produto['preço']}\n")
    #Procura um valor específico dentro dos registros
    def buscar_registro(self, busca, teste = True):
        for registro in self.Registro:
            for produto in registro:
                if busca.lower() == str(registro[produto]).lower():
                    print(">Aqui está(ão) o(s) produto(s) que você buscou:")
                    print(f"Celular: {registro['nome']}\nCódigo: {registro['código']}\nMarca: {registro['marca']}\nPreço: {registro['preço']}\n")
                    teste =  False
        if teste:
            print(">Produto não cadastrado")
    #Apaga todos os registros da lista
    def eliminar_registro(self):
        self.Registro.clear()
    #Apaga apenas o registro que o usuário deseja
    def eliminar_produto(self, eliminar):
        elimina = []
        for registro in self.Registro:
            for produto in registro:
                if eliminar.lower() == str(registro[produto]).lower():
                    elimina.append(registro)
        else:
            for registro in elimina:
                self.Registro.remove(registro)
#Definindo as variáveis:
escolha = ""
meu_registro = Registro()
#Rodando o código
Organizar_codigo.inicio()
while escolha != "sair":
    Organizar_codigo.menu()
    escolha = input(">").lower()
    #Testando as opções
    if escolha == "registrar":
        Organizar_codigo.load()
        if len(meu_registro.Registro) == 50:
            print('''>Registro cheio
>Não é possível registrar mais produtos''')
        else:
            teste = True
            while teste:
                try:
                    #Usamos o estrutura try para fazer o tratamento de exceção
                    print(f">Há {len(meu_registro.Registro)} produtos cadastrados na lista")
                    print(">Quantos itens você quer inserir?\n>Escreva 0 para retornar ao menu\n")
                    n = int(input(">"))
                    teste = False
                except (ValueError):
                    #O código informando ao usuário seu erro
                    print("==============!!ERRO!!===============")
                    print(">Não pode escrever número por extenso")
                    print("=====================================")
                    teste = True
            if n == 0:
                teste = False
            elif n > 50:
                print(">\nO número máximos de elementos no registro é de 50")
                print(f">Inserindo {50 - len(meu_registro.Registro)} elementos no registro")
                n = 50 - len(meu_registro.Registro)
            for i in range(n):
                teste = True
                while teste:
                    try:
                        nome = input("\n>Nome do produto: ")
                        codigo = int(input(">Código do produto: "))
                        marca = input(">Marca do produto: ")
                        preco = float(input(">Preço do produto: "))
                        meu_registro.criar_registro(nome, codigo, marca, preco)
                        teste = False
                    except (ValueError):
                        #O código informando ao usuário seu erro
                        print("================!!ERRO!!=================")
                        print(">Não pode escrever número por extenso")
                        print(">Caso precise usar vírugula, use o ponto")
                        print("=========================================")
                        teste = True
        Organizar_codigo.load()
    elif escolha == "imprimir":
        Organizar_codigo.load()
        outra_escolha = input(">Escolha uma opção:\n>Imprimir tudo\n>Imprimir trecho\n>Voltar\n\n>")
        if outra_escolha.lower() == "imprimir tudo":
            Organizar_codigo.load()
            meu_registro.imprimir_tudo()
        elif outra_escolha.lower() == "imprimir trecho":
            Organizar_codigo.load()
            teste = True
            while teste:
                print(">Digite o trecho que deseja imprimir\n>Digite 0 para sair")
                inicio = int(input(">Começo do trecho:\n>"))
                final = int(input(">Final do trecho:\n>"))
                if inicio > final:
                    final, inicio = inicio, final
                    Organizar_codigo.load()
                    meu_registro.imprimir_trecho((inicio-1), final)
                    teste = False
                elif final > len(meu_registro.Registro):
                    print("\n>O trecho que você digitou é maior que o registro")
                    print(f">Há {len(meu_registro.Registro)} produtos registrados")
                    teste = True
                elif inicio == 0 or final == 0:
                    Organizar_codigo.final()
                    teste = False
                else:
                    Organizar_codigo.load()
                    meu_registro.imprimir_trecho((inicio-1), final)
                    teste = False
        elif outra_escolha.lower() == "voltar":
            Organizar_codigo.load()
        else:
            print(">Funcionalidade não definida\n")
    elif escolha == "buscar":
        Organizar_codigo.load()
        print(">Qual produto você quer encontrar?")
        bus = input(">")
        meu_registro.buscar_registro(bus)
    elif escolha == "eliminar":
        Organizar_codigo.load()
        apagar = input(">Escolha uma opção:\n>Apagar tudo\n>Apagar produto\n>Voltar\n\n>")
        if apagar.lower() == "apagar tudo":
            meu_registro.eliminar_registro()
        elif apagar.lower() == "apagar produto":
            Organizar_codigo.load()
            meu_registro.imprimir_tudo()
            elim = input(">Qual produto você deseja apagar?\n\n>").lower()
            meu_registro.eliminar_produto(elim)
        elif apagar.lower() == "voltar":
            Organizar_codigo.load()
        else:
            print(">Funcionalidade não definida\n")
    elif escolha == "sair":
        Organizar_codigo.final()
    else:
        print(">Funcionalidade não definida\n")
