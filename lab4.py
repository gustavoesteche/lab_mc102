#declarando uma função para juntar elementos de uma lista em uma string para corresponder com o 
#formato do output desejado.
def juntar(lista):
    string_resultado = ""
    for indice in range(len(lista)):
        if indice == len(lista) -1:
            string_resultado += lista[indice]
        else:
            string_resultado += lista[indice]+", "
    return string_resultado
 
#declarando as listas para armazenar os dados diários da clínica.
atendido = []
nao_atendido = []
nao_disponivel = []
n_brigaslista = []
 
D = int(input())
#O loop para que a operação seja realizada em todos os dias.
for dia in range(D):
 
    #processando os pares de cachorros que brigam no dia.
    pares_briga = []
    M = int(input())
    for j in range(M):
        par = list(map(str, input().split()))
        pares_briga.append(par) 
 
    #processando os procedimentos disponibilizados pela clínica e a disponibilidade no dia, na forma de um dicionário 
    # para o acesso da quantidade ser mais limpo e compreensível.
    procedimentos = {}
    proced_input = list(map(str, input().split()))
    index1 = 0
    while index1 < len(proced_input):
        procedimentos[proced_input[index1]] = int(proced_input[index1+1])
        index1 += 2
    
    #processando os atendimentos que foram requisitados para a clínica no dia.
    atendimentos = []
    Z = int(input())
    for k in range(Z):
        ola = list(map(str, input().split())) 
        atendimentos.append(ola)
    
    #contando a quantidades de brigas que aconteceram no dia.
    n_brigas = 0 
    for index2 in range(Z):
        for index3 in range(Z):
            if [atendimentos[index2][0],atendimentos[index3][0]] in pares_briga:
                n_brigas += 1
    n_brigaslista.append(n_brigas)
    
    #checar quem vai ser atendido, não atentido, ou procedimento não disponível.
    #sufixo "pd" é para indicar que a lista é por dia, e não a lista de todos os dias.
    nao_atendidopd = []
    atendidopd = []
    nao_disponivelpd = []
    for index4 in range(Z):
        if not (atendimentos[index4][1] in proced_input):
            nao_disponivelpd.append(atendimentos[index4][0])
        else:
            if procedimentos[atendimentos[index4][1]] > 0:
                atendidopd.append(atendimentos[index4][0])
                procedimentos[atendimentos[index4][1]] -= 1
            else:
                nao_atendidopd.append(atendimentos[index4][0])
    
    atendido.append(atendidopd)
    nao_atendido.append(nao_atendidopd)
    nao_disponivel.append(nao_disponivelpd)
 
for dia in range(D):
    #printando na tela o resultado adiquirido no formato desejado.
    print("Dia:", dia+1)
    print("Brigas:", n_brigaslista[dia])
    if len(atendido[dia]) > 0:
        print("Animais atendidos:", juntar(atendido[dia]))
    if len(nao_atendido[dia]) > 0:
        print("Animais não atendidos:", juntar(nao_atendido[dia]))
    for animal in nao_disponivel[dia]:
        print("Animal", animal ,"solicitou procedimento não disponível.")
    print()