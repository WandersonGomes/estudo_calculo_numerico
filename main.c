#include <stdio.h>
#include <math.h>

typedef struct {
    double a;
    double b;
} Intervalo;

typedef struct {
    double raiz;
    int numero_interacoes;
} Resultado;

double funcao(double x) {
    return pow(x, 4) + 12.6 * pow(x, 3) - 155.7 * pow(x, 2) - 678.6 * x + 1863;
}

double modulo(double numero) {
    return (numero < 0) ? -numero : numero;
}

Resultado bisseccao(Intervalo intervalo, double tolerancia) {
    Resultado resultado;
    double x1, x0;
    double error_atual = __DBL_MAX__;
    
    resultado.numero_interacoes = 0;

    do {
        resultado.numero_interacoes++;
        x1 = (intervalo.a + intervalo.b)/2;
        
        //raiz exata
        if (funcao(x0) == 0) break;

        //calcula o erro atual
        if (resultado.numero_interacoes > 1)
            error_atual = modulo(x1 - x0);
        
        //atualiza o intervalo
        if ((funcao(intervalo.a) * funcao(x1)) < 0)
            intervalo.b = x1;
        else
            intervalo.a = x1;

        //atualiza o x anterior
        x0 = x1;
    } while (error_atual >= tolerancia);

    resultado.raiz = x0;

    return resultado;
}

int main() {
    Intervalo intervalo;
    double tolerancia;
    Resultado resultado;

    printf("Informe o intervalo [a, b]: ");
    scanf("%lf %lf", &intervalo.a, &intervalo.b);

    printf("Informe a tolerancia: ");
    scanf("%lf", &tolerancia);

    if ((funcao(intervalo.a) * funcao(intervalo.b)) < 0) {
        resultado = bisseccao(intervalo, tolerancia);
        printf("Valor funcao: %.6lf\n", funcao(resultado.raiz));
        printf("Raiz Encontrada: %.6lf\n", resultado.raiz);
        printf("Numero Interacoes: %d\n", resultado.numero_interacoes);        
    } else {
        printf("Error: intervalo invalido para a funcao!\n");
    }

    return 0;
}