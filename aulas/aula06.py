import matplotlib.pylab as plt
import pandas as pd

# Analise qualitativa
frutas =[
    "Maçã", "Banana", "Maçã",
    "Laranja", "banana", "Banana", 
    "Maçã", "Uva", "Laranja"
]

serie = pd.Series(frutas)
frequencia = serie.value_counts()

print(frequencia)

frequencia.plot(kind="bar")

plt.title("Frutas Preferidas dos Alunos")
plt.xlabel("Frutas")
plt.ylabel('Frequência')

plt.show()
plt.savefig('aula06-qualitativo')