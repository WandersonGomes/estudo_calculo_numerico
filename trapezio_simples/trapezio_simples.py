from math import cos

def trapezio_simples(x1, x2, funcao):
    h = x2 - x1
    
    integral = (h/2.0) * (funcao(x1) + funcao(x2))

    return integral

if __name__ == '__main__':
    def funcao(x):
        return x**4 - 2 * cos(x)
    
    x1 = 0
    x2 = 1

    integral = trapezio_simples(x1, x2, funcao)

    print('Integral pelo Trapezio Simples: %.2f' % integral)