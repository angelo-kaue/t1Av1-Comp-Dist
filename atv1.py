from math import comb
import pandas as pd
import matplotlib.pyplot as plt
import random

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


print("Caso k=1 (consulta):", disponibilidade(5, 1, 0.9)) 
print("Caso k=n (atualização):", disponibilidade(5, 5, 0.9))


#1.2 cálculo analítico + simulação
n = 10
lista_p = [i/10 for i in range(0, 11)]
rodadas = 5

disp_k1 = [disponibilidade(n, 1, p) for p in lista_p]
disp_kn2 = [disponibilidade(n, n//2, p) for p in lista_p]
disp_kn = [disponibilidade(n, n, p) for p in lista_p]

sim_k1 = [simulador(n, 1, p, rodadas) for p in lista_p]
sim_kn2 = [simulador(n, n//2, p, rodadas) for p in lista_p]
sim_kn = [simulador(n, n, p, rodadas) for p in lista_p]


plt.plot(lista_p, disp_k1, label="Analítico k=1", color="blue")
plt.plot(lista_p, disp_kn2, label="Analítico k=n/2", color="orange")
plt.plot(lista_p, disp_kn, label="Analítico k=n", color="green")

plt.plot(lista_p, sim_k1, linestyle="dotted", marker="o", color="blue", label="Simulação k=1")
plt.plot(lista_p, sim_kn2, linestyle="dotted", marker="s", color="orange", label="Simulação k=n/2")
plt.plot(lista_p, sim_kn, linestyle="dotted", marker="^", color="green", label="Simulação k=n")

plt.title("Disponibilidade Analítica vs Simulação (n=10)")
plt.xlabel("Probabilidade p")
plt.ylabel("Disponibilidade")
plt.legend()
plt.grid()
plt.show()

n, k, p = 5, 3, 0.7
print("\nComparação analítico x simulação")
print("Analítico :", disponibilidade(n, k, p))
print("Simulação:", simulador(n, k, p))