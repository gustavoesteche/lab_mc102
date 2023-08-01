# Inicializando os grupos em listas para facilitar a procura
vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
consoantes = [
    'b',
    'c',
    'd',
    'f',
    'g',
    'h',
    'j',
    'k',
    'l',
    'm',
    'n',
    'p',
    'q',
    'r',
    's',
    't',
    'v',
    'w',
    'x',
    'y',
    'z',
    'B',
    'C',
    'D',
    'F',
    'G',
    'H',
    'J',
    'K',
    'L',
    'M',
    'N',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'V',
    'W',
    'X',
    'Y',
    'Z']
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
 
 
def procurar_operando(mensagem_total: str, operando: str, i: int) -> int:
    '''Procura o operador dentro da string total codificada
 
 
    Procura apenas o caracter ou um grupo de caracteres dentro da string
    total e retorna o índice para o cálculo da chave de decodificação
    '''
    if len(operando) == 1:
        index = mensagem_total.find(operando, i, len(mensagem_total) - 1)
        return index
    elif operando == "vogal":
        for j in range(i, len(mensagem_total)): 
            if mensagem_total[j] in vogais: 
                return j 
    elif operando == "consoante":
        for j in range(i, len(mensagem_total)):
            if mensagem_total[j] in consoantes:
                return j
    elif operando == "numero":
        for j in range(i, len(mensagem_total)):
            if mensagem_total[j] in numeros:
                return j
    return -1
 
 
def calcular_chave(
        mensagem_total: str,
        operador: str,
        operando1: str,
        operando2: str) -> int:
    '''Calcula a chave de decriptação da string codificada
 
 
    Usando a função procurar_operando a função acha os índices procurados e faz
    a devida operação usando o operador fornecido
    '''
    index1 = procurar_operando(mensagem_total, operando1, 0)
    index2 = procurar_operando(mensagem_total, operando2, index1)
    if operador == "+": 
        print(index1 + index2) 
        return index1 + index2 
    elif operador == "-": 
        print(index1 - index2) 
        return index1 - index2 
    elif operador == "*": 
        print(index1 * index2) 
        return index1 * index2 
    return 0
 
 
def calcular_indice(indice: int, k: int) -> int:
    '''Usando a chave calculada a função encontra o indices dos novos
    elementos na tabela ASCII
 
 
    A função soma o índice atual com k e checa os limites calculando
    o valor do índice dentro do intervalo 26 - 126.
    '''
    indice = indice + k
    if (indice) > 126:
        indice = 32 + (k - (127 - (indice - k))) % 95
    elif (indice) < 32:
        indice = 127 - (32-indice) % 95
    return indice
 
 
def decodificar_mensagem(mensagem: str, k: int) -> None:
    '''Chama a função calcular_indice para decodificar as mensagens
 
    Chama para todo o caracter a função que decodifica eles e depois
    junta todos eles em uma única string.
    '''
    mensagem_char = [ord(x) for x in mensagem]
    for i in range(len(mensagem_char)):
        mensagem_char[i] = calcular_indice(mensagem_char[i], k)
    msg_decodificada = "".join([chr(char) for char in mensagem_char])
    print(msg_decodificada)
 
 
def main() -> None:
    '''Função utilizada para operacionalizar o programa'''
    operador = input()
    operando1 = input()
    operando2 = input()
    n_linhas = int(input())
    mensagem_total = ''
    mensagem_lista = []
    for _ in range(0, n_linhas):
        mensagem = input()
        mensagem_total += mensagem
        mensagem_lista.append(mensagem)
 
    k = calcular_chave(mensagem_total, operador, operando1, operando2)
    for i in range(n_linhas):
        decodificar_mensagem(mensagem_lista[i], k)
 
 
if __name__ == "__main__":
    main()