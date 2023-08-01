# declarando os tipos de números e naipes na ordem decrescente
numbers = ['K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2', 'A']
suits = ["P","C","E","O"]

# Dicionário que transforma as cartas de string em sua força numérica
dict_str_num = {}
k = 0 
for i in range(len(numbers)):
    for j in range(len(suits)):
        s = numbers[i]+suits[j]
        dict_str_num[s] = k
        k+=1

# Dicionário que transforma as cartas de sua força numérica 
# em formato de string
dict_num_str = {}
k = 0 
for i in range(len(numbers)):
    for j in range(len(suits)):
        s = numbers[i]+suits[j]
        dict_num_str[k] = s
        k+=1

def merge_sort(arr:list[int])->list[int]:
    '''Algoritmo de merge_sort que perfoma em ordenação na lista'''
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left:list[int], right:list[int])->list[int]:
    '''Função recursiva que da o merge da direita e da 
        esquerda no merge sort'''
    merged = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged

def bin_search(arr:list,target:int)->int:
    '''Algoritmo de busca de binária para achar um elemento em um array'''
    left = 0
    right = len(arr) - 1
    while left <= right: 
        mid = (left+right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid +  1
    return None

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
        self.cards_str = []
        self.cards_num = []

    def set_cards(self):
        '''Recebe o input da mão do jogador'''
        cards = input().split(", ")
        self.cards_str = cards
        self.count = len(cards)
        self.str_to_num()
        self.organize_cards()

    def organize_cards(self):
        '''Organiza a ordem das cartas'''
        self.cards_num = merge_sort(self.cards_num)
        self.num_to_str()

    def num_to_str(self):
        '''Transfere os dados salvos em numericamente para string'''
        self.cards_str = []
        for i in self.cards_num:
            self.cards_str.append(dict_num_str[i])

    def str_to_num(self):
        '''Transfere os dados salvos em string para números'''
        self.cards_num = []
        for i in self.cards_str:
            self.cards_num.append(dict_str_num[i])
    

    def push_stack(self, stack:list[str], min:int):
        '''Define quais cartas do jogador vão ser postas na pilha e se o Player blefará'''
        self.blefe = True
        
        k = (min // 4) * 4 + 3
        for i in range(k,-1,-1):
            x = bin_search(self.cards_num, i)
            if x != None:
                self.blefe = False
                card = self.cards_num[x]
                break
        
        if self.blefe:
            x = 0
            card = self.cards_num[-1]
        
        n = (card // 4) * 4 
        cards = []
        for i in range(n, n+4): 
            x = bin_search(self.cards_num, i)
            if x != None:
                cards.append(i)
        
        for j in range(len(cards)):
            cards[j] = dict_num_str[cards[j]]
        

        if self.blefe:
            self.print_push(cards, dict_num_str[min])
            self.push_(stack, cards)
            return min
        else:
            self.print_push(cards, dict_num_str[card])
            self.push_(stack, cards)
            return card


    def remove_cards(self, cards:list[str]):
        '''Remove as cartas da mão dos jogadores'''
        for i in range(len(cards)):
            cards[i] = dict_str_num[cards[i]]
        for num in cards:
            x = bin_search(self.cards_num, num)
            self.cards_num.pop(x)

        self.num_to_str()
        self.count = len(self.cards_str)
        

    def pull_stack(self, stack):
        '''Puxa as cartas da pilha para o jogador e limpa a pilha'''
        for card in stack:
            self.cards_str.append(card)
        self.str_to_num()
        self.organize_cards()
        self.count = len(self.cards_str)
        stack.clear()

    def push_(self,stack, pushed:list[str]):
        '''Coloca as cartas na pilha'''
        for i in range(len(pushed)-1,-1,-1):
            stack.append(pushed[i])
        self.remove_cards(pushed)

    def print_push(self, pushed:list[str],min:str):
        '''Printa a string para indicar a entrega de cartas à pilha'''
        
        if not self.blefe:
            if len(pushed[0]) == 3:
                s = "{}{}".format(pushed[0][0],pushed[0][1])
                print("[Jogador {}] {} carta(s) {}".format(self.id, len(pushed),s))
            else:
                print("[Jogador {}] {} carta(s) {}".format(self.id, len(pushed),pushed[0][0]))
        else:
            if len(min) == 3: 
                s = "{}{}".format(min[0],min[1])
                print("[Jogador {}] {} carta(s) {}".format(self.id, len(pushed),s))
            else:
                print("[Jogador {}] {} carta(s) {}".format(self.id, len(pushed),min[0]))

    def print_hand(self):
        '''Exibe a mão do jogador '''
        s = "Jogador {}\nMão: ".format(self.id)
        for card in self.cards_str:
                s += "{} ".format(card) 
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
min = 51
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
        min = 51
        print_hands(players)
        print_stack(stack)
    

print("Jogador {} é o vencedor!".format(save+1))
