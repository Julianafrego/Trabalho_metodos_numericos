import math

#definição da funcao e derivada

def f(x):
    return math.exp(x) - 4 * x  # calcula o valor da função 

def f_derivada(x):
    return math.exp(x) - 4 # calcula a derivada

def metodo_newton( x_inicial=0.5, tolerancia=1e-4, iteracoes_maxima=50):
    # nosso x_inicial é a metade do intervalo [1,2]
    # tolerancia igual a 1 x 10(elevado a -4), procuramos uma solucao com precisao de 4 casas decimais,
    x = x_inicial

    for i in range(iteracoes_maxima):  # itera até o nuero maximo 
        fx = f(x)   # chamamos a funcao em questao para o valor obtido em x
        fdx = f_derivada(x) # chamamos a derivada da funcao em questao para o valor obtido de x

        if fdx == 0:   # se a derivada for igual a zero, teremos erro devido derivada nula
            raise ZeroDivisionError("derivada nula")
        
        #calcula-se o novo valor de x
        # fazemos isso, usando a formula do método de newton
        novo_x = x - fx / fdx 
        
        print(f"Iteração {i+1}: x = {novo_x}, f(x) = {fx}")

        # verifica se a diferença entre o novo e o antigo valor de x é menor que a tolerancia
        # se for verdade, significa que a solucao encontrada é suficientemente precisa,
        # assim, retornarmos a mensagem indicando a convergencia
        if abs(novo_x - x) < tolerancia:
            print(f"convergiu para {novo_x} após {i+1} iterações")
            return novo_x, i+1, 
        
        # atualiza o valor de x para a próxima iteração
        x = novo_x

    print("Número máximo de iterações alcançado.")   
    return x, iteracoes_maxima, 

raiz, iteracoes = metodo_newton()

print(f"Raiz encontrada: {raiz}")
print(f"Número de iterações: {iteracoes}")