from math import comb
import pandas as pd
import matplotlib.pyplot as plt
import random

#n número total de servidores.
#k mínimo de servidores ativos necessários.
#p probabilidade de cada servidor funcionar.

def disponibilidade(n_servidores, k_minimo, probabilidade):
    return sum(
        comb(n_servidores, i) * (probabilidade**i) * ((1 - probabilidade)**(n_servidores - i))
        for i in range(k_minimo, n_servidores + 1)
    )

def simulador(n_servidores, k_minimo, probabilidade, rodadas=10000):
    sucessos = 0
    for _ in range(rodadas):
        disponiveis = sum(1 for _ in range(n_servidores) if random.random() <= probabilidade)
        if disponiveis >= k_minimo:
            sucessos += 1
    return sucessos / rodadas


#testes do exercício 1.1
print("Caso k=1 (consulta):", disponibilidade(5, 1, 0.9))
print("Caso k=n (atualização):", disponibilidade(5, 5, 0.9))


#exercício 1.2 analítico 3, 5 e 10 servs
lista_n = [3, 5, 10]
lista_p = [i/10 for i in range(0, 11)]

resultados = []
for n in lista_n:
    for p in lista_p:
        valores = {
            "n_servidores": n,
            "probabilidade": round(p, 2),
            "k=1": disponibilidade(n, 1, p),
            "k=n/2": disponibilidade(n, n // 2, p),
            "k=n": disponibilidade(n, n, p)
        }
        resultados.append(valores)

tabela = pd.DataFrame(resultados)
print("\nTabela de resultados (primeiras linhas):")
print(tabela.head())

for n in lista_n:
    dados = tabela[tabela["n_servidores"] == n]
    plt.plot(dados["probabilidade"], dados["k=1"], label=f"k=1, n={n}")
    plt.plot(dados["probabilidade"], dados["k=n/2"], label=f"k=n/2, n={n}")
    plt.plot(dados["probabilidade"], dados["k=n"], label=f"k=n, n={n}")

plt.title("Disponibilidade Analítica")
plt.xlabel("Probabilidade p")
plt.ylabel("Disponibilidade")
plt.legend()
plt.grid()
plt.show()



#exercício 1.2 simulador
n, k, p = 5, 3, 0.7
print("\nComparação analítico x simulação")
print("Analítico :", disponibilidade(n, k, p))
print("Simulação:", simulador(n, k, p))