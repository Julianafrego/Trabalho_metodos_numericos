import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Função original f(x)
def f(x):
    return np.log(x) + x**2 - 3

# Método do Ponto Fixo
def ponto_fixo(phi, x0, epsilon_1=1e-4, epsilon_2=1e-4, iterMax=50):
    """
    Implementa o Método do Ponto Fixo para encontrar raízes de uma equação.
    Retorna a raiz aproximada, número de iterações e histórico de valores.
    """
    historico = [(0, x0, f(x0))]  # Inclui x0 como ponto inicial no histórico

    # Verifica se o valor inicial já é suficiente
    if abs(f(x0)) < epsilon_1:
        return x0, 0, historico

    k = 1
    while k <= iterMax:
        try:
            x1 = phi(x0)
        except ValueError:
            raise ValueError(f"Erro: valor fora do domínio em ln(x). Iteração {k}, x = {x0}")

        fx1 = f(x1)
        historico.append((k, x1, fx1))

        print(f"Iteração {k}: x1 = {x1:.6f}, x0 = {x0:.6f}, Diferença = {abs(x1 - x0):.6e}, f(x1) = {fx1:.6e}")

        if abs(fx1) < epsilon_1 or abs(x1 - x0) < epsilon_2:
            return x1, k, historico

        x0 = x1
        k += 1

    raise ValueError("Método não convergiu dentro do número máximo de iterações")

# Função de iteração φ(x) = sqrt(3 - ln(x))
phi = lambda x: np.sqrt(3 - np.log(x))

# Valor inicial (meio do intervalo [1, 2])
x0 = (1 + 2) / 2

# Execução do método
raiz, iteracoes, historico = ponto_fixo(phi, x0)

# Resultados
print(f"\nRaiz aproximada: {raiz:.6f}")
print(f"Número de iterações: {iteracoes}")

# Tabela de resultados
df = pd.DataFrame(historico, columns=["Iteração", "x", "f(x)"])
print("\nTabela de Iterações:")
print(df)

# Gráfico de convergência
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
