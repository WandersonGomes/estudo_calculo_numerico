from math import cos

def simpson_simples(x1, x3, funcao):
    h = (x3 - x1)/2.0

    x2 = x1 + h

    integral = (h/3.0) * (funcao(x1) + 4 * funcao(x2) + funcao(x3))

    return integral

if __name__ == '__main__':
    def funcao(x):
        return x**4 - 2 * cos(x)
    
    x1 = 0
    x3 = 1

    integral = simpson_simples(x1, x3, funcao)

    print('Integral pelo Simpson Simples: %.2f' % integral)