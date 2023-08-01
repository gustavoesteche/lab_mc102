# funções usadas pelo código
def dano_calc(M: int,
              critico_tuple: tuple[int,
                                   int],
              coordenada_tuple: tuple[int,
                                      int],
              critico: bool) -> int:
    '''Calcula o dano causado pela personagem em uma máquina'''
    if critico:
        dano = (M -
                (abs(critico_tuple[0] -
                     coordenada_tuple[0]) +
                 abs(critico_tuple[1] -
                     coordenada_tuple[1])))
    else:
        dano = (M - (abs(critico_tuple[0] - coordenada_tuple[0]) +
                abs(critico_tuple[1] - coordenada_tuple[1]))) // 2
 
    if dano < 0:
        dano = 0
    return dano
 
 
def ataque_input() -> tuple[int, str, str, tuple[int, int]]:
    '''Recebe o input de cada ataque com flecha'''
    ataque = input().split(", ")
    K = int(ataque[0])
    C = ataque[1]
    tipo_flecha = ataque[2]
    coordenada = (int(ataque[3]), int(ataque[4]))
    return K, C, tipo_flecha, coordenada
 
 
def acess_info_parte(maquinas_parte: dict, C: str) -> list:
    '''Acessa a lista correspondente as informações de uma parte'''
    lista = maquinas_parte[C]
    return lista
 
 
# Definindo a classe da personagem, da máquina e do combate
class Aloy:
    def __init__(self) -> None:
        self.vida_maxima = 0
        self.vida = 0
        self.flechas = {}
        self.flechas_usadas = {}
        self.nmax_flechas = 0
        self.n_flechas = 0
        self.contador_ataques = 0
        self.venceu = False
        self.viva = True
        self.set_vida()
        self.set_flechas()
 
    def set_vida(self) -> None:
        '''Define a vida da personagem aloy'''
        A = int(input())
        self.vida_maxima = A
        self.vida = self.vida_maxima
 
    def set_flechas(self) -> None:
        '''Define o conjunto de flechas da personagem aloy'''
        flechas_input = input().split()
 
        for i in range(0, len(flechas_input), 2):
            self.flechas[flechas_input[i]] = int(flechas_input[i + 1])
            self.flechas_usadas[flechas_input[i]] = 0
            self.n_flechas += int(flechas_input[i + 1])
        self.nmax_flechas = self.n_flechas
 
    def remover_vida(self, dano_sofrido: int) -> None:
        '''Diminui a vida da personagem aloy de um dano dado'''
        self.vida -= dano_sofrido
        if self.vida <= 0:
            self.vida = 0
            self.viva = False
 
    def remover_flecha(self, tipo_flecha: str) -> None:
        '''Remove as flechas da personagem
        
        Remova uma flecha do tipo, adiciona uma flecha usada do tipo
        e remove uma flecha do total possuido
        '''
        self.flechas[tipo_flecha] -= 1
        self.n_flechas -= 1
        self.flechas_usadas[tipo_flecha] += 1
 
    def cura(self):
        '''Cura a personagem aloy
        
        Cura a personagem floor(0,5*vida maxima) pontos de vida
        '''
        self.vida += self.vida_maxima // 2
        if self.vida > self.vida_maxima:
            self.vida = self.vida_maxima
 
    def recarregar_flechas(self) -> None:
        '''Recarrega as flechas para o estado inicial
        
        Soma as flechas atuais com as usadas chegando no
        número inicial de flechas
        '''
        for estilo_flechas in self.flechas:
            self.flechas[estilo_flechas] = self.flechas[estilo_flechas] + self.flechas_usadas[estilo_flechas]
            self.flechas_usadas[estilo_flechas] = 0
        self.n_flechas = self.nmax_flechas
 
    def preparar_combate(self):
        '''Prepara a personagem pra um novo vombate
        
        A função recarrega as flechas da personagens e cura
        a personagem floor(0,5*vida maxima) pontos de vida
        '''
        self.recarregar_flechas()
        self.cura()
        self.contador_ataques = 0
 
 
# objeto para salvar as informações do combate
class Combate:
    def __init__(self, vida_aloy: int) -> None:
        self.n_combate = 0
        self.vida_aloy = vida_aloy
        self.critico = {}
        self.maquinas_mortas = []
 
 
aloy = Aloy() # cria a personagem 
  
# informações das máquinas 
N = int(input())  # quantidade de máquinas 
 
 
interrupcao = ""
combate = Combate(aloy.vida)
 
################################################################
while (N > 0 and interrupcao == ""): 
    # Reinicia as variáveis referentes as máquinas
    vida_inimigos = 0
    ataque_inimigos = 0
    U = int(input())  # máquinas enfrentadas por turno
    N -= U
    maquinas = {}
    for i_maquina in range(U):
        pontos_vida, pontos_ataque, qnt_partes = map(int, input().split())
        partes = {}
        coord_criti = {}
        for i in range(qnt_partes):
            parte = input().split(", ")
            partes[parte[0]] = [parte[1], int(
                parte[2]), (int(parte[3]), int(parte[4]))]
            coord_criti[(int(parte[3]), int(parte[4]))] = 0
        # [nome] = [fraqueza, dano máximo, tupla da coordenada do ponto fraco]
 
        maquinas[i_maquina] = [pontos_vida, pontos_ataque, partes]
        combate.critico[i_maquina] = coord_criti
        vida_inimigos += pontos_vida
        ataque_inimigos += pontos_ataque
        # maquinas[número da máquina] = [pontos de vida, pontos de ataque, dict
        # de partes e informações]
 
    # combate em si
    print("Combate", combate.n_combate, end=", ")
    print("vida =", combate.vida_aloy)
    while (vida_inimigos > 0 and interrupcao == ""):
        aloy.contador_ataques += 1
 
        # ataque aloy
        K, C, tipo_flecha, coordenada = ataque_input()
        lista_parte = acess_info_parte(maquinas[K][2], C)
 
        if (lista_parte[0] == "todas" or lista_parte[0] ==
                tipo_flecha):
            dano = dano_calc(lista_parte[1], lista_parte[2], coordenada, True)
            aloy.remover_flecha(tipo_flecha)
        else:
            dano = dano_calc(lista_parte[1], lista_parte[2], coordenada, False)
            aloy.remover_flecha(tipo_flecha)
 
        if coordenada == lista_parte[2]:
            combate.critico[K][coordenada] += 1
 
        maquinas[K][0] -= dano
 
        if maquinas[K][0] <= 0:
            vida_inimigos -= (maquinas[K][0] + dano)
            maquinas[K][0] = 0
            ataque_inimigos -= maquinas[K][1]
            combate.maquinas_mortas.append(K)
            print("Máquina", K, "derrotada")
        else:
            vida_inimigos -= dano
 
        # ataque inimigos
        if aloy.contador_ataques == 3:
            aloy.contador_ataques = 0
            aloy.remover_vida(ataque_inimigos)
 
        # caso houver morte ou falta de flecha
        if not aloy.viva and interrupcao == "":
            interrupcao = "morte"
            break
        if aloy.n_flechas <= 0 and interrupcao == "":
            interrupcao = "falta de flechas"
            break
 
    if interrupcao == "":
        print("Vida após o combate", "=", aloy.vida)
        print("Flechas utilizadas:")
        for estilo_flecha in aloy.flechas_usadas:
            if aloy.flechas_usadas[estilo_flecha] != 0:
                print("-", estilo_flecha, end=": ")
                print(aloy.flechas_usadas[estilo_flecha], end="/")
                print(
                    aloy.flechas[estilo_flecha] +
                    aloy.flechas_usadas[estilo_flecha])
 
        critico_existe = False
        for i in range(U):
            maq_critada = False
            for coord in combate.critico[i]:
                if combate.critico[i][coord] != 0:
                    if not critico_existe:
                        print("Críticos acertados:")
                        critico_existe = True
                    if not maq_critada:
                        print("Máquina", i, end=":\n")
                        maq_critada = True
                    print("-", coord, end=": ")
                    print(combate.critico[i][coord], end="x\n")
 
    else:
        print("Vida após o combate =", aloy.vida)
 
    # preparando para o próximo combate
    aloy.preparar_combate()
    combate.maquinas_mortas = []
    combate.n_combate += 1  
    combate.vida_aloy = aloy.vida
    combate.critico = {}
 
 
 
if interrupcao == "":
    print("Aloy provou seu valor e voltou para sua tribo.")
else:
    if interrupcao == "morte":
        print("Aloy foi derrotada em combate e não retornará a tribo.")
    else:
        print("Aloy ficou sem flechas e recomeçará sua missão mais preparada.")