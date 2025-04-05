import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Função original f(x) cujo zero queremos encontrar
def f(x):
    return np.log(x) + x**2 - 3

# Método do Ponto Fixo
def ponto_fixo(phi, x0, epsilon_1=1e-4, epsilon_2=1e-4, iterMax=50):
    """
    Implementa o Método do Ponto Fixo para encontrar uma raiz da equação f(x) = 0.
    
    Parâmetros:
    - phi: função de iteração (φ(x))
    - x0: chute inicial
    - epsilon_1: tolerância para |f(xk)|
    - epsilon_2: tolerância para |xk - x(k-1)|
    - iterMax: número máximo de iterações
    
    Retorna:
    - raiz aproximada
    - número de iterações realizadas
    - histórico com valores de x e f(x) em cada iteração
    """
    historico = [(0, x0, f(x0))]  # Guarda o valor inicial na lista de histórico

    # Verifica se o chute inicial já é suficientemente bom
    if abs(f(x0)) < epsilon_1:
        return x0, 0, historico

    k = 1  # contador de iterações
    while k <= iterMax:
        try:
            x1 = phi(x0)  # calcula a próxima iteração com φ(x)
        except ValueError:
            # Trata casos em que ln(x) esteja fora do domínio
            raise ValueError(f"Erro: valor fora do domínio em ln(x). Iteração {k}, x = {x0}")

        fx1 = f(x1)
        historico.append((k, x1, fx1))

        # Mostra os valores a cada iteração no console
        print(f"Iteração {k}: x1 = {x1:.6f}, x0 = {x0:.6f}, Diferença = {abs(x1 - x0):.6e}, f(x1) = {fx1:.6e}")

        # Critérios de parada: |f(x1)| pequeno o suficiente ou |x1 - x0| pequeno o suficiente
        if abs(fx1) < epsilon_1 or abs(x1 - x0) < epsilon_2:
            return x1, k, historico

        # Atualiza x0 para próxima iteração
        x0 = x1
        k += 1

    # Caso atinja o número máximo de iterações sem convergir
    raise ValueError("Método não convergiu dentro do número máximo de iterações")

# Define a função φ(x) que será usada no método do ponto fixo
phi = lambda x: np.sqrt(3 - np.log(x))

# Valor inicial escolhido no meio do intervalo [1, 2]
x0 = (1 + 2) / 2

# Executa o método do ponto fixo
raiz, iteracoes, historico = ponto_fixo(phi, x0)

# Exibe a raiz aproximada e o número de iterações realizadas
print(f"\nRaiz aproximada: {raiz:.6f}")
print(f"Número de iterações: {iteracoes}")

# Cria um DataFrame com os resultados para exibir em tabela
df = pd.DataFrame(historico, columns=["Iteração", "x", "f(x)"])
print("\nTabela de Iterações:")
print(df)

# Gráfico mostrando a evolução dos valores de x ao longo das iterações
plt.figure(figsize=(8, 6))
plt.plot(df["Iteração"], df["x"], marker='o', linestyle='-', color='blue', label='x em cada iteração')
plt.axhline(raiz, color='red', linestyle='--', label=f'Raiz aproximada ≈ {raiz:.6f}')
plt.xlabel("Iteração")
plt.ylabel("Valor de x")
plt.title("Evolução da Aproximação para a Raiz")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
