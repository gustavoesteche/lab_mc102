#Definindo as operações que vão ser usadas nas operações vetoriais
def igualando_dimensoes(vetor1 : list[int], vetor2 : list[int], elemento_neutro:int):
    '''Igualando a quantidade de dimensões dos vetores de acordo com o elemento neutro indicado'''
    if len(vetor1) < len(vetor2):
        for _ in range(len(vetor2)- len(vetor1)):
            vetor1.append(elemento_neutro)
    if len(vetor1) > len(vetor2):
        for _ in range(len(vetor1)- len(vetor2)):
            vetor2.append(elemento_neutro)
    return vetor1, vetor2

def soma_vetores(vetor1 : list[int], vetor2 : list[int]):
    '''Soma elemento a elemento de dois vetores'''
    vetor1, vetor2 = igualando_dimensoes(vetor1, vetor2,0)
    for i in range(len(vetor1)):
        vetor1[i] += vetor2[i]
    return vetor1

def subtrai_vetores(vetor1 : list[int], vetor2 : list[int]):
    '''Subtrai os elemento a elemento do vetor1 usando o vetor2 '''
    vetor1, vetor2 = igualando_dimensoes(vetor1, vetor2,0)
    for i in range(len(vetor1)):
        vetor1[i] -= vetor2[i]
    return vetor1

def multiplica_vetores(vetor1 : list[int], vetor2 : list[int]):
    '''Multiplica elemento a elemento de dois vetores'''
    vetor1, vetor2 = igualando_dimensoes(vetor1, vetor2,1)
    for i in range(len(vetor1)):
        vetor1[i] *= vetor2[i]
    return vetor1

def divide_vetores(vetor1 : list[int], vetor2 : list[int]):
    '''Divide elemento a elemento do vetor1 usando o vetor2'''
    if len(vetor1) < len(vetor2):
        vetor1, vetor2 = igualando_dimensoes(vetor1, vetor2,0)
    else:
        vetor1, vetor2 = igualando_dimensoes(vetor1, vetor2,1)

    for i in range(len(vetor1)):
        vetor1[i] //= vetor2[i]
    return vetor1

def multiplicacao_escalar(vetor : list[int], escalar:int):
    '''Multiplica todo elemento por um escalar'''
    for i in range(len(vetor)):
        vetor[i] *= escalar
    return vetor

def n_duplicacao(vetor:list[int], n:int):
    '''Duplica o vetor n vezes'''
    vetor = vetor * n
    return vetor 

def soma_elementos(vetor : list[int]):
    '''Soma todos os elementos da lista e retorna um vetor'''
    soma = [0]
    for i in range(len(vetor)):
        soma[0] += vetor[i]
    return soma

def produto_interno(vetor1 : list[int], vetor2 : list[int]):
    '''Realiza a operação de produto escalar em dois vetores'''
    vetor1, vetor2 = igualando_dimensoes(vetor1, vetor2,1)
    prod_interno = [0]
    for i in range(len(vetor1)):
        prod_interno[0] += vetor1[i] * vetor2[i]
    return prod_interno 


def multiplica_todos(vetor1 : list[int], vetor2 : list[int]):
    '''multiplica cada elemento do primeiro vetor por todos os elementos do segundo vetor e 
    soma o resultado.'''
    vetor = []
    for i in range(len(vetor1)):
        vetor.append(vetor1[i] * soma_elementos(vetor2)[0])
    return vetor

def correlacao_cruzada(vetor : list[int], mascara : list[int]):
    '''Realiza a operação de correlação cruzada em um vetor dado, com uma mascara também dada e retorna seu valor'''
    CC = []
    for i in  range(len(vetor) - len(mascara) + 1):
        somatorio = 0
        for j in range(len(mascara)):
            somatorio += vetor[i+j]*mascara[j]
        CC.append(somatorio)
    return CC

#Inicia o vetor que vai ser modificado e o loop das operações
vetor1 = list(map(int, input().split(",")))
resposta = "desejo uma ótimo final de semana para você"
while resposta != "fim":
    resposta = input()
    if resposta == "soma_vetores":
        vetor2 = list(map(int, input().split(",")))
        vetor1 = soma_vetores(vetor1, vetor2)
        print(vetor1)

    elif resposta == "subtrai_vetores":
        vetor2 = list(map(int, input().split(",")))
        vetor1 = subtrai_vetores(vetor1, vetor2)
        print(vetor1)

    elif resposta == "multiplica_vetores":
        vetor2 = list(map(int, input().split(",")))
        vetor1 = multiplica_vetores(vetor1, vetor2)
        print(vetor1)

    elif resposta == "divide_vetores":
        vetor2 = list(map(int, input().split(",")))
        vetor1 = divide_vetores(vetor1, vetor2)
        print(vetor1)

    elif resposta == "multiplicacao_escalar":
        escalar = int(input())
        vetor1 = multiplicacao_escalar(vetor1, escalar)
        print(vetor1)

    elif resposta == "n_duplicacao":
        n = int(input())
        vetor1 = n_duplicacao(vetor1, n)
        print(vetor1)

    elif resposta == "soma_elementos":
        vetor1 = soma_elementos(vetor1)
        print(vetor1)

    elif resposta == "produto_interno":
        vetor2 = list(map(int, input().split(",")))
        vetor1 = produto_interno(vetor1, vetor2)
        print(vetor1)

    elif resposta == "multiplica_todos":
        vetor2 = list(map(int, input().split(",")))
        vetor1 = multiplica_todos(vetor1, vetor2)
        print(vetor1)

    elif resposta == "correlacao_cruzada":
        mascara = list(map(int, input().split(",")))
        vetor1 = correlacao_cruzada(vetor1, mascara)
        print(vetor1)
    