from math import cos

def trapezio_repetido(x1, xn, n, funcao):
    h = (xn - x1)/(n * 1.0)
    
    soma = 0.00
    for indice in range(2, n + 1):
        xi = x1 + (indice - 1) * h
        soma += 2 * funcao(xi)
    
    integral = (h/2.0) * (funcao(x1) + soma + funcao(xn))
    return integral

if __name__ == '__main__':
    def funcao(x):
        return x**4 - 2 * cos(x)
    
    x1 = 0
    xn = 1
    n = 4

    integral = trapezio_repetido(x1, xn, n, funcao)

    print('Integral pelo Trapezio Repetido: %.10f' % integral)