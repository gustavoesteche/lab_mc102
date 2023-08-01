# definindo o nosso espaço
N = int(input())
space_matrix = []
clean = "."
dirty = "o"
for _ in range(N):
    line = input().split()
    M = len(line)
    space_matrix.append(line)
 
# função que printa o nosso espaço
 
 
def print_matrix(matrix:list[list])->None:
    for line in matrix:
        print(" ".join(line))
    print()
 
 
print_matrix(space_matrix)
 
# parâmetros do robo
position = [0, 0]
mode = "scan"
i, j = 0, 0
last_movement = ""
 
# definindo a movimentação do rôbo
 
 
def move_left(position:list[int]) -> None:
    '''Move o robo para a esquerda'''
    global last_movement
    position[1] -= 1
    space_matrix[position[0]][position[1]] = 'r'
    space_matrix[position[0]][position[1] + 1] = clean
    last_movement = "left"
    print_matrix(space_matrix)
 
 
def move_right(position:list[int]) -> None:
    '''Move o robô para a direita'''
    global last_movement
    position[1] += 1
    space_matrix[position[0]][position[1]] = 'r'
    space_matrix[position[0]][position[1] - 1] = clean
    print_matrix(space_matrix)
    last_movement = "right"
 
 
def move_up(position:list[int]) -> None:
    '''Move o robô para cima'''
    global last_movement
    position[0] -= 1
    space_matrix[position[0]][position[1]] = 'r'
    space_matrix[position[0] + 1][position[1]] = clean
    print_matrix(space_matrix)
    last_movement = "up"
 
 
def move_down(position:list[int]) -> None:
    '''Move o robô para baixo'''
    global last_movement
    position[0] += 1
    space_matrix[position[0]][position[1]] = 'r'
    space_matrix[position[0] - 1][position[1]] = clean
    last_movement = "down"
    print_matrix(space_matrix)
 
# definindo o scanner
 
 
def scan(position: list[int]) -> None:
    '''Escaneia as posições adjacentes para procurar sujeiras'''
    global i, j
    done = True
    if position[1] != 0 and done:
        if (space_matrix[position[0]][position[1] - 1] == dirty):
            if mode == "scan" and position[0] % 2 == 1:
                move_left(position)
                done = False
                scan(position)
            else:
                move_left(position)
                done = False
                cleaning(position[0], position[1] + 1)
 
    if position[0] != 0 and done:
        if (space_matrix[position[0] - 1][position[1]] == dirty):
            move_up(position)
            done = False
            cleaning(position[0] + 1, position[1])
 
    if position[1] != M - 1 and done:
        if (space_matrix[position[0]][position[1] + 1] == dirty):
            if mode == "scan" and position[0] % 2 == 0:
                move_right(position)
                done = False
                scan(position)
            else:
                move_right(position)
                done = False
                cleaning(position[0], position[1] - 1)
 
    if position[0] != N - 1 and done:
        if (space_matrix[position[0] + 1][position[1]] == dirty):
            if position[1] == M-1 and position[0]%2==0:
                move_down(position)
                done = False
                scan(position)
            elif position[1] == 0 and position[0]%2==1:
                move_down(position)
                done = False
                scan(position)
            else:
                move_down(position)
                done = False
                cleaning(position[0] - 1, position[1])
 
    if done and mode == "clean":
        return_to_scan()
 
# retornando a posição inicial antes do scan
 
 
def return_to_scan() -> None:
    '''Retorna a o robô para quando ele entrou no modo limpeza'''
    global i, j
    while position != [i, j]:
        if j > position[1]:
            move_right(position)
            scan(position)
        elif j < position[1]:
            move_left(position)
            scan(position)
        elif j == position[1]:
            if i < position[0]:
                move_up(position)
                scan(position)
            else:
                move_down(position)
                scan(position)
 
# função de limpeza
 
 
def cleaning(a: int, b: int) -> None:
    '''Guarda a posição onde começou a limpar
    e limpa todas as posições adjacentes'''
    global mode, i, j
    if mode == "scan":
        i = a
        j = b
    mode = "clean"
    scan(position)
 
 
def stop_cleaning() -> None:
    '''Para o loop'''
    global mode
    mode = "end"
 
direction = "left"
# loop do movimento
while mode != "end":
    scan(position)
    if N % 2 == 0 and position[0] == N - 1 and direction == "left":
        move_left(position)
        if position[1] == 0:
            direction = "right"
    elif N % 2 == 0 and position[0] == N - 1 and direction == "right":
        move_right(position)
        if mode == "scan" and position == [N - 1, M - 1]:
            stop_cleaning()
    else:
        if position[0] % 2 == 0:
            if position[1] == M - 1:
                move_down(position)
            else:
                move_right(position)
        else:
            if position[1] == 0:
                move_down(position)
            else:
                move_left(position)
        mode = "scan"
        if mode == "scan" and position == [N - 1, M - 1] and last_movement == "right":
            stop_cleaning()