# Questão "Luck Balance do HackerRank"
# https://www.hackerrank.com/challenges/luck-balance/problem

def luckBalance(important_contests, contests):
    list1 = []
    aux = 1
    
    for x,y in contests: 
        if y: 
            list1.append(x)
        else: 
            aux += x
    
    length = len(list1)
    list1.sort() # Ordenamos
    z = len(list1) - important_contests
    sumx = sum(list1)
    
    if important_contests < length:
        return aux + sum(list1[z:]) - sum(list1[:z]) -1
    
    else:
        return aux + sumx - 1

# "Main"

# Fazemos a leitura do n, k
n,k = map(int,input().split()) 

# Para que possamos fazer o uso do contests na funcao, ele precisa ser uma lista de listas ou lista de tuplas
contests = [list(map(int,input().split())) for x in range(n)] 

# Na questao, eh pedido a utilizacao de dois parametros: k e contests.
print(luckBalance(k, contests))