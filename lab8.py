F = int(input()) 
lista_filmes = [input() for i in range(F)]
Q = int(input())
avaliacoes = {}
 
categorias = [
    "filme que causou mais bocejos",
    "filme que foi mais pausado",
    "filme que mais revirou olhos",
    "filme que não gerou discussão nas redes sociais",
    "enredo mais sem noção"]
for cat in categorias:
    avaliacoes[cat] = {}
    for filme in lista_filmes:
        avaliacoes[cat][filme] = [0, 0]
 
for i in range(Q):
    avaliacao = input().split(", ")
    avaliacoes[avaliacao[1]][avaliacao[2]] = [
        avaliacoes[avaliacao[1]][avaliacao[2]][0] + 1,
        avaliacoes[avaliacao[1]][avaliacao[2]][1] + int(avaliacao[3])]
 
# Procurando os premiados
# e printando a categoria simples
premiados = {}
print("#### abacaxi de ouro ####\n")
print("categorias simples")
for cat in categorias:
    max = [0, 0]
    for filme in lista_filmes:
        if avaliacoes[cat][filme][0] != 0:
            avaliacoes[cat][filme] = [
                avaliacoes[cat][filme][0],
                avaliacoes[cat][filme][1] /
                avaliacoes[cat][filme][0]]
            if avaliacoes[cat][filme][1] > max[1]:
                max = avaliacoes[cat][filme]
                escolhido = filme
            elif avaliacoes[cat][filme][1] == max[1]:
                if avaliacoes[cat][filme][0] > max[0]:
                    max = avaliacoes[cat][filme]
                    escolhido = filme
    premiados[cat] = escolhido
    print("categoria:", cat)
    print("-", premiados[cat])
 
print("\ncategorias especiais")
 
# prêmio especial prêmio não merecia estar aqui
# e a soma total das notas de cada filme
esp_n_merecia = []
soma_notas = {}
for filme in lista_filmes:
    soma_notas[filme] = [0, 0]
    for cat in categorias:
        soma_notas[filme][1] += avaliacoes[cat][filme][1]
        soma_notas[filme][0] += avaliacoes[cat][filme][0]
    if soma_notas[filme][1] == 0:
        esp_n_merecia.append(filme)
 
# Procurando o pior filme
inv_premiados = {}
for chave, valor in premiados.items():
    inv_premiados[valor] = inv_premiados.get(valor, []) + [chave]
 
max = [0, "filme"]
for filme in lista_filmes:
    premios = len(inv_premiados.get(filme, []))
    if premios > 0:
        if premios > max[0]:
            max[0] = premios
            max[1] = filme
        elif premios == max[0]:
            if soma_notas[filme][1] > soma_notas[max[1]][1]:
                max[0] = premios
                max[1] = filme
 
# Printando as categorias especiais
print("prêmio pior filme do ano")
print("-", max[1])
 
print("prêmio não merecia estar aqui")
if len(esp_n_merecia) == 0:
    print("- sem ganhadores")
else:
    print("-", ", ".join(esp_n_merecia))