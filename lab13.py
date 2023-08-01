import sys
sys.setrecursionlimit(16385)

def preencher_balde(imagem, c, t, col, row):
    cor_seed = imagem[row][col]
    if abs(cor_seed - c) <= t and imagem[row][col] != c:
        imagem[row][col] = c
        # Expandindo para os vizinhos
        if row > 0:
            preencher_balde(imagem, c, t, col, row - 1)  # pixel acima
        if row < len(imagem) - 1:
            preencher_balde(imagem, c, t, col, row + 1)  # pixel abaixo
        if col > 0:
            preencher_balde(imagem, c, t, col - 1, row)  # pixel à esquerda
        if col < len(imagem[0]) - 1:
            preencher_balde(imagem, c, t, col + 1, row)  # pixel à direita

def negativo(imagem, t, col, row):
    cor_seed = imagem[row][col]
    cor_maxima = 255
    if abs(cor_seed - cor_maxima) <= t and imagem[row][col] != cor_maxima:
        imagem[row][col] = cor_maxima - imagem[row][col]
        # Invertendo as cores dos vizinhos
        if row > 0:
            negativo(imagem, t, col, row - 1)  # pixel acima
        if row < len(imagem) - 1:
            negativo(imagem, t, col, row + 1)  # pixel abaixo
        if col > 0:
            negativo(imagem, t, col - 1, row)  # pixel à esquerda
        if col < len(imagem[0]) - 1:
            negativo(imagem, t, col + 1, row)  # pixel à direita

def mascara_complementar(imagem, t, col, row):
    cor_seed = imagem[row][col]
    mascara = [[0] * len(imagem[0]) for _ in range(len(imagem))]
    
    def dfs(row, col):
        if row < 0 or row >= len(imagem) or col < 0 or col >= len(imagem[0]):
            return
        if abs(imagem[row][col] - cor_seed) <= t and mascara[row][col] == 0:
            mascara[row][col] = 255
            dfs(row - 1, col)  # pixel acima
            dfs(row + 1, col)  # pixel abaixo
            dfs(row, col - 1)  # pixel à esquerda
            dfs(row, col + 1)  # pixel à direita
    
    dfs(row, col)
    return mascara

def ler_imagem_pgm(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    
    cabecalho = linhas[:4]
    pixels = [[int(pixel) for pixel in linha.split()] for linha in linhas[4:]]
    
    return pixels

def escrever_imagem_pgm(nome_arquivo, imagem):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write('P2\n')  # Identificador do formato PGM
        arquivo.write('# Imagem gerada\n')  # Descrição do arquivo
        arquivo.write(f'{len(imagem[0])} {len(imagem)}\n')  # Número de colunas e linhas
        arquivo.write('255\n')  # Valor máximo dos pixels
        
        for linha in imagem:
            arquivo.write(' '.join(str(pixel) for pixel in linha))
            arquivo.write('\n')

nome_arquivo