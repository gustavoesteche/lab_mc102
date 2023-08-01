# declarando os tipos de números e naipes na ordem decrescente
numbers = ['K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2', 'A']
suits = ["P","C","E","O"]
suits_dict = {"P":1, "C":2, "E":3, "O":4}



# funções utilizadas para printar variáveis relevantes
def print_hands(players:list[int]) -> None:
    '''Exibe a mão de todos os jogadores'''
    for i in range(J):
        players[i].print_hand()

def print_stack(stack):
    '''Exibe a pilha atual do jogo'''
    print("Pilha:",end = "")
    if len(stack)>0:
        print(" ",end="")
        print(" ".join(stack))
    else:
        print()

class Player:
    def __init__(self, id) -> None:
        self.id = id
        self.blefe = False
        self.count = 0 
        self.cards = {number:[] for number in numbers}
        self._cards_ = {i:[] for i in range(13,0,-1)}
        self.convertion = {}
        self.mount_convertion()

    def mount_convertion(self):
        '''Monta o dicionário de conversão de strings para números e vice-versa'''
        j = 13
        for number in numbers:
            self.convertion[number] = j
            j -= 1
    
    def add_cards(self, cards):
        '''Adiciona as cartas a mão do jogador'''
        self.count += len(cards)
        for card in cards:
            if len(card) == 2:
                self.cards[card[0]].append(card[1])
            else:
                s = "{}{}".format(card[0],card[1])
                self.cards[s].append(card[2])
        self.organize_cards()
    
    def remove_cards(self, number):
        '''Remove as cartas da mão dos jogadores'''
        self.count -= len(self.cards[number])
        self.cards[number] = []
        self._cards_[self.key_str_num(number)] = []

    def set_cards(self):
        '''Recebe o input da mão do jogador'''
        cards = input().split(", ")
        self.add_cards(cards)

    def organize_cards(self):
        '''Organiza os naipes das cartas'''
        for key in self.cards:
            lista = []
            for j in range(4):
                for i in range(len(self.cards[key])):
                    if self.cards[key][i] == suits[j]:
                        lista.append(suits[j])
            self.cards[key] = lista
        self.str_to_num() 

    def num_to_str(self):
        '''Transfere os dados salvos em chave numéria para chave em string'''
        i = 13
        for key in self.cards:
            self.cards[key] = self._cards_[i].copy()
            i -= 1

    def str_to_num(self):
        '''Transfere os dados salvos em chave em string para chave em número'''
        i = 13
        for key in self.cards:
            self._cards_[i] = self.cards[key].copy()
            i -= 1
    
    def key_num_str(self, x):
        '''Transforma uma chave de número para chave de string'''
        for key,value in self.convertion.items():
            if value == x:
                x = key 
                break
        return x

    def key_str_num(self,x): 
        '''Transforma uma chave de string para chave de número'''
        x = self.convertion[x]
        return x
        
    def pull_stack(self, stack):
        '''Puxa as cartas da pilha para o jogador e limpa a pilha'''
        self.add_cards(stack)
        stack.clear()

    def push_stack(self, stack, min):
        '''Define quais cartas do jogador vão ser postas na pilha e se ele blefará'''
        min = str(min)
        min = self.key_str_num(min)

        self.blefe = True
        for i in range(min,14):
            if len(self._cards_[i]) > 0:
                pushed = i
                self.blefe = False                 
                break
        
        if self.blefe:
            for i in range(1,14):
                if len(self._cards_[i]) > 0:
                    pushed = i
                    break
            self.print_push(pushed, min)
            self.push_(stack, pushed)
            return self.key_num_str(min)
        else:
            self.print_push(pushed, min)
            self.push_(stack, pushed)
            return self.key_num_str(pushed)
    
    def push_(self,stack, pushed):
        '''Coloca as cartas na pilha'''
        pushed = self.key_num_str(pushed)
        for i in range(len(self.cards[pushed])-1,-1,-1):
            card = "{}{}".format(pushed,self.cards[pushed][i])
            stack.append(card)
        self.remove_cards(pushed)

    def print_push(self, pushed,min):
        '''Printa a string para indicar a entrega de cartas à pilha'''
        pushed = self.key_num_str(pushed)
        if not self.blefe:
            print("[Jogador {}] {} carta(s) {}".format(self.id, len(self.cards[pushed]),pushed))
        else:
            min = self.key_num_str(min)
            print("[Jogador {}] {} carta(s) {}".format(self.id, len(self.cards[pushed]),min))


    def print_hand(self):
        '''Exibe a mão do jogador '''
        s = "Jogador {}\nMão: ".format(self.id)
        for key in self.cards:
            for value in self.cards[key]:
                    s += "{}{} ".format(key,value) 
        print(s.rstrip())

# Declarando a lista que guardará os jogadores e a pilha
players = []
stack = []


# recebendo os inputs do usuário
J = int(input())

for i in range(J):
    player = Player(i+1)
    player.set_cards()
    players.append(player)

N = int(input())

print_hands(players)
print_stack(stack)


# Declarando as variáveis para o loop
run = True
doubt = 0 # Quando é igual a N o jogador dúvida.
turn = 0 # Quando chega em J o jogador 1 joga novamente.
min = "A"
last_played = players[0]


# loop de jogo
while run:
    min = players[turn].push_stack(stack, min)
    last_played = players[turn]
    print_stack(stack)

    if (players[turn].count == 0):
        save = turn 
        run = False

    turn += 1
    doubt += 1

    if turn >= J:
        turn = 0

    if doubt >= N:
        doubt = 0
        print("Jogador {} duvidou.".format(players[turn].id))
        if last_played.blefe:
            last_played.pull_stack(stack)
            run = True
        else:
            players[turn].pull_stack(stack)
        min = "A"
        print_hands(players)
        print_stack(stack)
    

print("Jogador {} é o vencedor!".format(save+1))
    