"""
Autor: Wanderson Gomes da Costa
Data Ultima Modificao: 28 de Maio de 2021
E-mail: dersom100@gmail.com
"""
import numpy as np

def metodo_gauss_jacobi(x_inicial, coeficientes, idependentes, erro, max_iteracoes=10000):
    # calcula a matriz C
    C = coeficientes.copy().tolist()
    ordem = len(C)

    for i in range(0, ordem):
        for j in range(0, ordem):
            if i == j:
                C[i][j] = 0
            else:
                C[i][j] = -C[i][j]/coeficientes[i][i]
    C = np.array(C)

    # calcula a matriz g
    G = idependentes.copy().tolist()
    ordem = len(G)
    for i in range(0, ordem):
        G[i] = G[i]/coeficientes[i][i]
    G = np.array(G)

    # inicializa os x's
    x_anterior = x_inicial.copy()
    x_atual = x_inicial.copy()

    for iteracao in range(0, max_iteracoes):
        x_atual = C.dot(x_anterior) + G
        
        erro_atual = maximo_absoluto(x_atual - x_anterior)/maximo_absoluto(x_atual)

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

def criterio_linhas(matriz):
    ordem = len(matriz)
    for i in range(0, ordem):
        soma = 0.00
        for j in range(0, ordem):
            if i != j:
                soma += abs(matriz[i][j])
        if (soma/abs(matriz[i][i])) >= 1:
            return False
    return True

if __name__ == '__main__':
    matriz_coeficientes = np.array([[10, 2, 1], [1, 5, 1], [2, 3, 10]])
    matriz_idependentes = np.array([7, -8, 6])
    chute_inicial = np.array([0.7, -1.6, 0.6])
    erro = 0.05

    resposta = metodo_gauss_jacobi(chute_inicial, matriz_coeficientes, matriz_idependentes, erro)
    print(resposta)

    # TRABALHO CALCULO NUMERICO
    matriz_coeficientes = np.array([[2, 1, -0.2, 0.2], [0.6, 3, -0.6, -0.3], [-0.1, -0.2, 1, 0.2], [0.4, 1.2, 0.8, 4]])
    matriz_idependentes = np.array([0.4, -7.8, 1.0, -10.0])
    chute_inicial = np.array([0, 0, 0, 0])
    erro = 0.001

    print(criterio_diagonal(matriz_coeficientes))
    print(criterio_linhas(matriz_coeficientes))

    resposta = metodo_gauss_jacobi(chute_inicial, matriz_coeficientes, matriz_idependentes, erro)
    resposta = resposta.tolist()
    print(f'X1: {resposta[0]:.4f}, X2: {resposta[1]:.4f}, X3: {resposta[2]:.4f}, X4: {resposta[3]:.4f}')