# Declarando as classes a ser utilizadas
# Criar uma classe personagem com vida, dano ,posicao, morte, movimento
# nas 4 direções

class Personagem:
    def __init__(self) -> None:
        self.vida = 0
        self.dano = 0
        self.posicao = [0, 0]
        self.vivo = True

    def mod_vida(self, modificador: int):
        '''Altera a vida do Personagem'''
        self.vida += modificador
        if self.vida < 0:
            self.vida = 0
        self.check_vivo()

    def check_vivo(self):
        '''Checa se o personagem está vivo e altera o estado do personagem'''
        if self.vida <= 0:
            self.vivo = False

    def move_up(self):
        '''Move o personagem pra cima'''
        self.posicao[0] -= 1

    def move_down(self):
        '''Move o personagem para baixo'''
        self.posicao[0] += 1

    def move_right(self):
        '''Move o personagem para direita'''
        self.posicao[1] += 1

    def move_left(self):
        '''Move o personagem para a esquerda'''
        self.posicao[1] -= 1


class Link(Personagem):
    def __init__(self) -> None:
        super().__init__()
        self.baixo = True

    def set_data(self):
        '''Recebe o input da vida e do dano do link'''
        self.vida, self.dano = map(int, input().split())

    def set_posicao(self):
        '''Recebe o input da posição do link'''
        self.posicao = list(map(int, input().split(",")))

    def mod_dano(self, modificador: int):
        '''Altera o dano do link'''
        self.dano += modificador
        if self.dano < 1:
            self.dano = 1

    def move(self, N: int, M: int):
        '''Move o link pelo mapa'''
        if self.baixo:
            self.move_down()
            if self.posicao[0] == N - 1:
                self.baixo = False
        else:
            if self.posicao[0] % 2 == 0:
                if self.posicao[1] == 0:
                    self.move_up()
                else:
                    self.move_left()
            else:
                if self.posicao[1] == M - 1:
                    self.move_up()
                else:
                    self.move_right()

    def printa(self) -> None:
        '''Printa as características do link'''
        print(
            "vida",
            self.vida,
            "dano",
            self.dano,
            "posicao",
            self.posicao[0],
            self.posicao[1],
            self.vivo,
            "\n")


class Monstro(Personagem):
    def __init__(self) -> None:
        super().__init__()
        self.tipo = ""

    def set_data(self):
        '''Recebe o input com as informação do monstro'''
        data = input().split()
        pos = list(map(int, data[3].split(",")))
        self.vida, self.dano, self.tipo, self.posicao = int(
            data[0]), int(data[1]), data[2], [pos[0], pos[1]]

    def move(self, N: int, M: int):
        '''Move o monstro pelo mapa'''
        if self.tipo == "U":
            if self.posicao[0] > 0:
                self.move_up()
        elif self.tipo == "D":
            if self.posicao[0] < N - 1:
                self.move_down()
        elif self.tipo == "R":
            if self.posicao[1] < M - 1:
                self.move_right()
        elif self.tipo == "L":
            if self.posicao[1] > 0:
                self.move_left()

    def printa(self) -> None:
        '''Printa as características do Monstro'''
        print(
            "vida:",
            self.vida,
            "dano:",
            self.dano,
            "tipo",
            self.tipo,
            "posicao",
            self.posicao,
            "\n")


class Mapa:
    def __init__(self) -> None:
        self.N = 0
        self.M = 0
        self.objetos_dict = {}
        self.saida = [0, 0]

    def set_data(self):
        '''Recebe os inputs do tamanho do mapa'''
        self.N, self.M = map(int, input().split())
        self.declaring_map()

    def set_saida(self):
        '''Recebe o input da saída'''
        self.saida[0], self.saida[1] = map(int, input().split(","))

    def declaring_map(self):
        '''Declarando o dicionário que guarda os objetos que estão em uma posição do mapa'''
        for i in range(self.N):
            for j in range(self.M):
                self.objetos_dict[(i, j)] = []

    def set_map(self, posicao: tuple[int, int], objeto):
        '''Adiciona os objetos a sua posição'''
        self.objetos_dict[posicao].append(objeto)

    def change_map(
            self, last_posicao: tuple[int, int], new_posicao: tuple[int, int], objeto):
        '''Altera um objeto de posição no mapa'''
        self.objetos_dict[last_posicao].pop(
            self.objetos_dict[last_posicao].index(objeto))
        self.objetos_dict[new_posicao].append(objeto)

    def remove_map(self, posicao: tuple[int, int], objeto):
        '''Remove um objeto do mapa'''
        self.objetos_dict[posicao].pop(
            self.objetos_dict[posicao].index(objeto))

    def print_map(self, link_vivo: bool):
        '''Printa o mapae os objetos contidos nele'''
        for i in range(self.N):
            for j in range(self.M):
                if j == self.M - 1:
                    if self.objetos_dict[(i, j)] != [] and type(
                            self.objetos_dict[(i, j)][-1]) == Link:
                        if link_vivo:
                            print("P", end="")
                        else:
                            print("X", end="")
                    elif [i, j] == self.saida:
                        print("*", end="")
                    elif self.objetos_dict[(i, j)] != []:
                        if type(self.objetos_dict[(i, j)][-1]) == Monstro:
                            print(self.objetos_dict[(i, j)][-1].tipo, end="")
                        elif type(self.objetos_dict[(i, j)][-1]) == Objeto:
                            print(self.objetos_dict[(i, j)][-1].tipo, end="")
                    else:
                        print(".", end="")
                else:
                    if self.objetos_dict[(i, j)] != [] and type(
                            self.objetos_dict[(i, j)][-1]) == Link:
                        if link_vivo:
                            print("P", end=" ")
                        else:
                            print("X", end=" ")
                    elif [i, j] == self.saida:
                        print("*", end=" ")
                    elif self.objetos_dict[(i, j)] != []:
                        if type(self.objetos_dict[(i, j)][-1]) == Monstro:
                            print(self.objetos_dict[(i, j)][-1].tipo, end=" ")
                        elif type(self.objetos_dict[(i, j)][-1]) == Objeto:
                            print(self.objetos_dict[(i, j)][-1].tipo, end=" ")
                    else:
                        print(".", end=" ")
            print()
        print()

    def printa(self) -> None:
        '''Printa os atributos do mapa'''
        print(self.N, self.M, self.objetos_dict, self.saida, "\n")


class Objeto:
    def __init__(self) -> None:
        self.nome = ""
        self.tipo = ""
        self.posicao = [0, 0]
        self.status = 0

    def set_data(self) -> None:
        '''Recebe os inputs das características dos objetos'''
        data = input().split()
        pos = list(map(int, data[2].split(",")))
        self.nome, self.tipo, self.posicao, self.status = data[0], data[1], pos, int(
            data[3])


###############################

# Iniciando o Link(personagem) e o objeto representando o mapa

link = Link()
mapa = Mapa()

###############################


def main():
    # Recebendo os inputs fornecidos
    link.set_data()
    mapa.set_data()
    link.set_posicao()
    mapa.set_map(tuple(link.posicao), link)
    mapa.set_saida()

    Qm = int(input())
    monstros = [Monstro() for x in range(Qm)]
    for i in range(Qm):
        monstros[i].set_data()

    B = int(input())
    objetos = [Objeto() for x in range(B)]
    for i in range(B):
        objetos[i].set_data()

    for i in range(B):
        mapa.set_map(tuple(objetos[i].posicao), objetos[i])

    for i in range(Qm):
        mapa.set_map(tuple(monstros[i].posicao), monstros[i])

    mapa.print_map(link.vivo)

    run = True
    while (run):
        # movimentar os monstros
        for i in range(Qm):
            last_monstros = (tuple(monstros[i].posicao))
            monstros[i].move(mapa.N, mapa.M)
            mapa.change_map(last_monstros, tuple(
                monstros[i].posicao), monstros[i])

        # movimentar link
        last_link = tuple(link.posicao)
        link.move(mapa.N, mapa.M)
        mapa.change_map(last_link, tuple(link.posicao), link)

        # checar contato 
        n_coisas = len(mapa.objetos_dict[tuple(link.posicao)])
        coisas = mapa.objetos_dict[tuple(link.posicao)].copy()
        if n_coisas > 1 and link.posicao != mapa.saida:
            for i in range(n_coisas-1):  # o último elemento da lista é o link
                if type(coisas[i]) == Objeto and link.vivo:
                    if coisas[i].tipo == "d":
                        link.mod_dano(coisas[i].status)
                    elif coisas[i].tipo == "v":
                        link.mod_vida(coisas[i].status)
                    print("[{}]Personagem adquiriu o objeto {} com status de {}".format(
                        coisas[i].tipo, coisas[i].nome, coisas[i].status))
                    mapa.remove_map(tuple(coisas[i].posicao), coisas[i])

                elif type(coisas[i]) == Monstro and link.vivo:
                    v = coisas[i].vida
                    coisas[i].mod_vida(-link.dano)
                    if coisas[i].vivo:
                        print(
                            "O Personagem deu {} de dano ao monstro na posicao {}".format(
                                link.dano, tuple(
                                    link.posicao)))
                        v = link.vida
                        link.mod_vida(-coisas[i].dano)
                        if link.vivo:
                            print(
                                'O Monstro deu {} de dano ao Personagem. Vida restante = {}'.format(
                                    coisas[i].dano, link.vida))
                        else:
                            print(
                                'O Monstro deu {} de dano ao Personagem. Vida restante = {}'.format(
                                    v, link.vida))
                    else:
                        print(
                            "O Personagem deu {} de dano ao monstro na posicao {}".format(
                                v, tuple(
                                    link.posicao)))
                        mapa.remove_map(tuple(coisas[i].posicao), coisas[i])
                        Qm -= 1
                        monstros.pop(monstros.index(coisas[i]))

        # checar saída do loop
        if not link.vivo:
            run = False

        if mapa.saida == link.posicao:
            run = False

        mapa.print_map(link.vivo)

    if link.vivo:
        print("Chegou ao fim!")


if __name__ == "__main__":
    main()
