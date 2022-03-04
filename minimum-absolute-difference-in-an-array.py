# Questão "Minimum Absolute Difference in an Array" do HackerRank
# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem

def minimumAbsoluteDifference(arr):
    arr.sort() # Ordenando tarefas que nos interessam
    
    diferencas = [] # Todas as tarefas nos interessam no array recebido, entao sera uma variavel que vamos utilizar em todas as manipulacoes dos intervalos
    
    diferencas.append(abs(arr[0] - arr[1])) # Esta e a diferenca minima para o primeiro elemento do array
    
    diferencas.append(abs(arr[n - 1] - arr[n - 2])) # Esta e a diferenca minima para o ultimo elemento do array
         
    for i in range(1, n - 1): # Percorre todo o array buscando a minima diferenca absoluta
        diferencas.append(min(abs(arr[i] - arr[i - 1]),
                  abs(arr[i] - arr[i + 1])))
                
    return min(diferencas) # Retornamos a menor diferenca encontrada na lista de diferencas