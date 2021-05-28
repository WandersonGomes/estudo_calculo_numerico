"""
Autor: Wanderson Gomes da Costa
Data Ultima Modificao: 28 de Maio de 2021
E-mail: dersom100@gmail.com
"""
import numpy as np

def metodo_gauss_seidel(x_inicial, coeficientes, idependentes, erro, max_iteracoes=10000):
    # calcula a matriz C
    C = coeficientes.copy().tolist()
    ordem = len(C)

    for i in range(0, ordem):
        for j in range(0, ordem):
            if i == j:
                C[i][j] = 0
            else:
                C[i][j] = -C[i][j]/coeficientes[i][i]

    # calcula a matriz G
    G = idependentes.copy().tolist()
    ordem = len(G)
    for i in range(0, ordem):
        G[i] = G[i]/coeficientes[i][i]

    # inicializa os x
    x_anterior = x_inicial.copy().tolist()
    x_atual = x_inicial.copy().tolist()

    for iteracao in range(0, max_iteracoes):
        for i in range(0, ordem):
            soma = 0.00
            for j in range(0, ordem):
                if j < i:
                    soma += C[i][j] * x_atual[j]
                else:
                    soma += C[i][j] * x_anterior[j]
            
            soma += G[i]
            x_atual[i] = soma
        
        erro_atual = maximo_absoluto(np.array(x_atual) - np.array(x_anterior))/maximo_absoluto(np.array(x_atual))
        print(f'ITERACAO: {iteracao + 1}, X_ATUAL: {x_atual}, erro atual: {erro_atual}')
        if erro_atual < erro:
            break

        x_anterior = x_atual.copy()
    
    return x_atual


def maximo_absoluto(vetor):
    maior = -1.00
    for elemento in vetor:
        if abs(elemento) > maior:
            maior = abs(elemento)
    return maior

def criterio_diagonal(matriz):
    ordem = len(matriz)
    for i in range(0, ordem):
        if matriz[i][i] == 0:
            return False
    return True

def criterio_sassenfeld(matriz):
    ordem = len(matriz)
    betas = []
    
    for i in range(0, ordem):
        soma = 0.00
        for j in range(0, ordem):
            if j < i:
                soma += abs(matriz[i][j]) * betas[j]
            elif j > i:
                soma += abs(matriz[i][j])
        soma = soma/abs(matriz[i][i])
        if soma >= 1:
            return False
        betas.append(soma)

    print(betas)
    return True

if __name__ == '__main__':
    matriz_coeficientes = np.array([[2, 1, -0.2, 0.2], [0.6, 3, -0.6, -0.3], [-0.1, -0.2, 1, 0.2], [0.4, 1.2, 0.8, 4]])
    matriz_idependentes = np.array([0.4, -7.8, 1.0, -10.0])
    chute_inicial = np.array([0, 0, 0, 0])
    erro = 0.001

    resposta = metodo_gauss_seidel(chute_inicial, matriz_coeficientes, matriz_idependentes, erro)
    print(f'X1: {resposta[0]:.4f}, X2: {resposta[1]:.4f}, X3: {resposta[2]:.4f}, X4: {resposta[3]:.4f}')