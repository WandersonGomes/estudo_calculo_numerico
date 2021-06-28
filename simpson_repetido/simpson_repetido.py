from math import cos

def simpson_repetido(x1, x2n, n, funcao):
    h = (x2n - x1)/(2.0 * n)

    soma = 0.00
    for indice in range(2, (2*n + 1)):
        xi = x1 + (indice - 1) * h

        if indice % 2 == 0:
            soma += 4 * funcao(xi)
        else:
            soma += 2 * funcao(xi)
    
    integral = (h/3.0) * (funcao(x1) + soma + funcao(x2n))

    return integral

if __name__ == '__main__':
    def funcao(x):
        return x**4 - 2*cos(x)
    
    x1 = 0
    x2n = 1
    n = 4

    integral = simpson_repetido(x1, x2n, n, funcao)

    print('Integral pelo Simpson Repetido: %.2f' % integral)