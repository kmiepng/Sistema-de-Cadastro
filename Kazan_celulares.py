#Codigo da dupla Gian Victor e Kamila Sofia

#Importaremos as bibliotecas time e os
import time
import os
#Definimos a função esp() para printar espaços vazios
#E assim, consequentemente pular uma linha, deixando mais organizado

def esp():
    #O Flush = True serve para evitar erros e bugs no código
    print("\n ", flush = True)

#Definimos a função load() para simular uma tela de carregando
def load():
    a = ["carregando.",".","."]
    for i in range(len(a)):
        #O Flush = True serve para evitar erros e bugs no código
        print(a[i], end="", flush = True)
        #Colocmaos o time.sleep() Para que a simulação seja mais realistas
        time.sleep(0.75)
    #Colocamos os.system("cls") para limpar o terminal e deixar mais agradável visualmente
    os.system("cls")

#Definimos a função inicio() para simular uma tela de inicialização
def inicio():
    a = ["Iniciando.",".","."]
    for i in range(len(a)):
        print(a[i], end="", flush = True)
        time.sleep(0.75)
    os.system("cls")

#Definimos a função final() para simular uma tela de encerramento
def final():
    a = ["encerrando.",".","."]
    for i in range(len(a)):
        print(a[i], end = "", flush = True)
        time.sleep(0.75)
    os.system("cls")
    
#Primeiro, iniciomos com a função incio
inicio()
#Definimos a variável choise e c para usarmos mais tarde
#O choice será usado para o usuário escolher qual funcionalidade acessar
choice = " "
#A variável registro será onde armzenaremos os dicionários
#Como o próprio nome sugere, será o nosso registro
registro = []

#Colocamos a estrutura while para criar um código infinito
#E deixarmos ele junto de choice, para que o usuário pode encerrar o código a vontade
while choice != "sair":
    #Criamos um Menu minimalista, mais claro, óbvio e funcional
    print("===Menu===")
    time.sleep(0.5)
    print('''\nRegistrar
Eliminar
Imprimir tudo
Imprimir trecho 
Buscar
Sair\n''')
    #Pedimos para o usuário escolher entre 
    #registrar, imprimir tudo, imprimir trecho, buscar ou sair
    choice = input("").lower()
    #Definimos o choice como minusculo 
    # para evitar que o código não entenda letras maiúsculas
    
    #Colocamos os.system("cls") para limpar o terminal 
    #e deixar mais agradável visualmente
    os.system("cls")
    if choice == "registrar":
        #Usamos o load para carregar a escolha do usuário
        load()
        if len(registro) == 50:
            #Caso o registro esteja cheio, informe ao usuário
            print('''Registro cheio
Não possível registrar mais produtos''')
        teste = True
        #Definimos uma variável teste
        #Essa variável é de suma importância
        #Com ela, conseguimos saber se o usuário acabou digitando dados 
        #que acabam gerando erro no código
        #Como por exemplo, o código pedir um float e o usuário digitar um string
        #Usando tratamento de erro o código informará o usuário seu erro
        #E usando a estrutura while, o código recomeça do erro
        #Evitando do usuário ter que recomeçar o início
        while teste:
            try:
                #Usamos o estrutura try para fazer o tratamento de exceção
                print(f"Há {len(registro)} produtos cadastrados na lista")
                print("Quantos itens você quer inserir? (Escreva 0 para retornar ao menu)")
                n = int(input(""))
                teste = False
            except (ValueError):
                #O código informando ao usuário seu erro
                print("--------------------------------")
                print("!!ERRO!!")
                print("Escreva em números indo-arábicos")
                print("Exemplo: 2")
                print("--------------------------------")
                teste = True
        if n==0:
            #Caso o usuário tenha escrito "registrar" por acidente
            #Basta ele colocar 0 e o código voltará ao início
            #Pois ao fazer um for i in range(0)
            #O código irá de 0 até 0 excluindo o 0
            #Ou seja, não resultará em nada
            #Colocamos o teste = False para evitar bug 
            #e o código voltar ao início sem problemas
            teste = False
        if (len(registro)+n) <= 50:
            #Como o trabalho exigia que 
            # deveria possuir capacidade limitada a 50 posições
            #Criamos um verificador
            n = n
        else:
             #Caso o usuário tente colocar mais de 50 produtos
            #Ou que ele queira adicionar mais produtos ao registro já preenchido
            #O código irá informar que não é possível, mas não vai parar
            #Ao invés disso, irá continuar até que a lista tenha 50 produtos
            #Então aí irá parar
            print("O número máximos de elementos no registro é de 50")
            print(f"Inserindo {50 - len(registro)} elementos no registro")
            n = 50 - len(registro)
        for i in range(n):
            teste = True
            #Colocamos outro teste= True para utilizar mais um teste de exceção
            while teste:
                try:
                    #A variável produto, será um dicionário 
                    #contendo as informações do produto
                    produto = {
                        #As informações sobre o produto serão
                        #Nome, código, Marcar e preço
                        "nome" : (input("Nome do produto: ")),
                        "código" : int(input("Código do produto: ")),
                        "marca" : input("Marca responsável pelo produto: "),
                        "preço" : float(input("preço do produto: "))
                    }
                    registro.append(produto)
                    teste = False
                    esp()
                except (ValueError):
                    #O código informando ao usuário seu erro
                    print("-------------------------------------------------")
                    print("!!ERRO!!")
                    print("Escreva em números indo-arábicos")
                    print("Exemplo: 2")
                    print("Caso precise usar vírugula, use o ponto")
                    print("-------------------------------------------------")
                    teste = True
    elif choice == "imprimir tudo":
        #A funcionalidade de imprimir tudo servirá para inprimir
        load()
        print(registro)
        esp()
    elif choice == "imprimir trecho":
        #A funcionalidade que permite imprimir uma parte o registro
        load()
        #Utilizo a variável teste para o tratamento de exceção
        teste = True
        while teste:
            try: 
                #explico para o usuário como ele deve escrever o trecho
                #Ele escreve qual item deve começar e qual deve terminar
                #Parecido como o python lê, mas colocamos de forma mais intuitiva
                print("Indique o trecho a ser imprimido")
                print("exemplo: 1:3 (do primeiro até o terceiro produto)")
                print("exemplo: 1:1 (só o primeiro)")
                trecho = input("")
                if trecho.count(" ") > 0:
                    #Tratamento de exceção caso o usuário não formate 
                    #do jeito que eu quero
                    print("----------------------------------------------")
                    print("!!ERROR!!")
                    print("Não pode haver espeços entre os número e o ':'")
                    print("----------------------------------------------")
                    esp()
                else:
                    #Depois eu crio uma lista de transição 
                    #onde vai ficar o incio e o fim do trecho
                    transition = trecho.split(":")
                    #Determino as variáveis primeior e ultimo como sendo 
                    #o inicio e o fim do trecho
                    #Porém, eu determinei da forma que o python lê
                    pri = (int(transition[0]) - 1)
                    ult = int(transition[1])
                    esp()
            except (ValueError):
                #Tratamento de exceção para caso o usuário esqueça de colocar :
                #Ou esqueça de colocar um número
                print("----------------------------------------------")
                print("!!ERROR!!")
                print("Não esqueça que precisa dos ':' para funcionar")
                print("E que precisam ser número positivos")
                print("----------------------------------------------")
                esp()
            if pri < -1 or ult <0:
            #Tratamento de exceção para caso o usuário coloque números negativos
                print("-----------------------------------")
                print("!!ERROR!!")
                print("Não pode trecho com número negativo")
                print("-----------------------------------")
                esp()
            elif pri == -1 or ult == 0:
            #Tratamento de exceção para caso o usuário coloque zero
                print("---------------------")
                print("!!ERROR!!")
                print("Não pode colocar zero")
                print("---------------------")
                esp()
            elif pri > ult:
            #Tratamento de exceção para caso o usuário coloque 
            #um trecho com o primeiro termo maior que o segundo
                trans = pri
                pri = ult
                ult = trans
                os.system("cls")
                print(registro[pri:ult])
                teste = False
            elif ult > len(registro):
            #Tratamento de exceção para caso o usuário coloque 
            #um trecho maior que o tamanho do registro
                print("--------------------------------------------------------------")
                print("!!ERROR!!")
                print("trecho maior que o registro")
                print(f"O registro possui apenas {len(registro)} produtos cadastrados")
                print("--------------------------------------------------------------")
            else:
            #Imprimir trecho
                os.system("cls")
                print(registro[pri:ult])
                esp()
                teste = False
    elif choice == "buscar":
        #Funcionalidade para buscar um produto específico
        #Ou produtos de uma marca específica
        load()
        #Pedimos ao usuário informar qual o produto a ser procurado
        print("Qual produto você quer encontrar?")
        bus = input("")
        #Dessa vez a variável teste está aqui para testar ser há o produto ou não
        teste = True
        for i in range(len(registro)):
            for j in (registro[i]):
                #Utilizamos dois for para procurar em cada item dentro de cada dicionário na lista
                #Se houver item equivalente, então imprime o dicionário a qual pertence
                #Colocamos um o parâmetro lower 
                #para evitar confusões de letras maiúsculas e minúsculas
                if bus.lower() == str(registro[i][j]).lower():
                    print(registro[i])
                    teste = False
        if teste:
            #Se o código não encontrar, vai imprimir que o produto não existe
            print("Produto não cadastrado")
        esp()
    elif choice == "sair":
        #Para evitar que o código responda algo em caso o usuário queira sair
        #Criamos essa escolha para ter certeza que nada ocorra de modo inesperado
        #E como precisavamos que algo acontecesse, colocamos duas variáveis
        #E definimos como Gian = "Bonitão" e "Kamila = "Pequena"
        Gian = "Bonitão"
        Kamila = "Pequena"

    elif choice == "eliminar":
        #Caso o usuário queira eliminar algum item ou mesmo o registro inteiro
        teste = True
        while teste:
            load()
            print('''Apagar todo o registro?
    (S/N)''')
            escolha = input("")
            escolha = escolha.lower()
            if escolha == "s":
                #Caso o usuário queira apagar todo o resgistro
                    registro.clear()
                    teste = False
            elif escolha == "n":
                #Caso o usuário queira apagar apenas intens avulsos
                print(registro)
                teste = False
                #O código mostra o registro para o usuário ter uma referência
                esp()
                print("Qual produto você quer eliminar?")
                elim = input("")
                elim = elim.lower()
                #O usuário escolhe qual o nome, código ou marca dos produtos 
                #que ele quer eliminar
                elimina = []
                for i in range(len(registro)):
                    for j in registro[i]:
                        #Uso dois for para fazer o código procurar no registro
                        #Os produtos que o usuário quer eliminar
                        if elim == str(registro[i][j]).lower():
                            
                            #Quando ele encontrar ele salva em uma lista separada
                            #Usamos esse método e não excluimos direto
                            #pois caso utilizemos o pop, a lista vai diminuir de tamanho
                            #E essa dimunuição acaba gerando problema com o for
                            #Então, primeiro registramos as posições dos produtos a excluir
                            elimina.append(i)
                            
                else:
                    #Declaramos um n para que quando formos excluir cada posição
                    #Não ocorre que o código exclua as posições erradas
                    #Pois como a lista diminui
                    #As posições são alteradas
                    #Logo esse n existe para que a relação entre 
                    #a lista de posições a serem excuídas e o registro não se perca
                    n = 0
                    #Depois, excluímos um por um em um outro for
                    #Nesse caso,ligado ao tamanho da lista das posições a serem excluídas
                    for i in range(len(elimina)):
                        registro.pop(elimina[i-n])
                        n = n +1
            else:
                #Caso o usuário informe qualquer coisa fora s ou n
                    esp()
                    print("Funcionalidade não definida")
                    esp()
    else:
        #Caso o usuário informe uma funcionalidade não definida
        esp()
        print("Funcionalidade não definida")
        esp()
else:
    #Quando o usuário finalizar, aparece "encerrando..." e finaliza o código
    final()