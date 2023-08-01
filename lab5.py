class Genoma: 
    def __init__(self,string_):
        self.string_ = string_
 
    #funções que vão ser utilizadas
    def reverter(self, i:int, j:int):
        '''Reverte a lista do índice i até o índice j'''
        n = len(self.string_)
        j = min(n, j+1)-1 #caso o número passado foi maior do que o comprimento da string 
        if i < n-1:
            lista = list(self.string_)
            for k in range((j-i+1)//2):
                temp = lista[i+k]
                lista[i+k] = lista[j-k]
                lista[j-k] = temp
            self.string_ = "".join(lista)
        
    def transpor(self,i:int, j:int, k:int):
        '''Troca de lugar a substring i:j e a substring j+1:k de lugar'''
        n = len(self.string_)
        k = min(n, k+1)-1 
        if i < n-1 and j < n-1:
            lista = list(self.string_)
            tamanho = len(lista)
            lista1 = [lista[x] for x in range(i,j+1)]
            lista2 = [lista[x] for x in range(j+1,k+1)]
            lista3 = [lista[x] for x in range(k+1, tamanho)]
            del lista[i:tamanho]
            self.string_ = "".join(lista) + "".join(lista2) + "".join(lista1) + "".join(lista3)
        
 
    def combinar(self, string1:str, i:int):
        '''Adiciona uma substring em um indice i'''
        lista = list(self.string_)
        lista1 = list(string1)
        contador = i
        for k in lista1:
            lista.insert(contador, k)
            contador+=1
        self.string_ = "".join(lista)
 
    def concatenar(self, string1:str):
        '''Junta duas strings'''
        self.string_ = self.string_ + string1
 
    def remover(self, i:int,j:int):
        '''Remove uma substring i:j'''
        n = len(self.string_)
        j= min(n, j+1)-1 
        if i < n-1:
            lista = list(self.string_)
            del lista[i:(j+1)]
            self.string_ = "".join(lista)
 
    def transpor_e_reverter(self, i:int,j:int,k:int):
        '''Ele transpõe e depois reverte a substring que foi transposta'''
        self.transpor(i,j,k)
        self.reverter(i,k)
        
    def buscar(self, substring:str):
        '''Busca uma substring no genoma'''
        contador = self.string_.count(substring)
        return contador
        #Para fins de reutilização tem que printar manualmente o contador nessa função
 
    def buscar_bidirecional(self, substring:str):
        '''Busca na string e depois busca na string revertida'''
        x = self.buscar(substring)
        self.reverter(0, len(self.string_)-1)
        y = self.buscar(substring)
        self.reverter(0, len(self.string_)-1)
        print(x+y)
    
    def mostrar(self):
        '''Printa o genoma na tela'''
        print(self.string_)
 
#Recebendo a string e criando um objeto classe com ela
string = input()
genoma = Genoma(string)
 
#loop de fazer as operações em seguida na string
resposta = ["olá","como você está corretor"]
while resposta[0] != "sair":
    resposta = input().split()
    if resposta[0] == "reverter":
        genoma.reverter(int(resposta[1]),int(resposta[2]))
 
    elif resposta[0] == "transpor":
        genoma.transpor(int(resposta[1]),int(resposta[2]),int(resposta[3]))
 
    elif resposta[0] == "combinar":
        genoma.combinar(resposta[1],int(resposta[2]))
 
    elif resposta[0] == "concatenar":
        genoma.concatenar(resposta[1])
 
    elif resposta[0] == "remover":
        genoma.remover(int(resposta[1]),int(resposta[2]))
 
    elif resposta[0] == "transpor_e_reverter":
        genoma.transpor_e_reverter(int(resposta[1]),int(resposta[2]),int(resposta[3]))
 
    elif resposta[0] == "buscar":
        print(genoma.buscar(resposta[1]))
 
    elif resposta[0] == "buscar_bidirecional":
        genoma.buscar_bidirecional(resposta[1])
 
    elif resposta[0] == "mostrar":
        genoma.mostrar()
