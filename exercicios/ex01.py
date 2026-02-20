import matplotlib.pyplot as plt

categorias = ['Stranger Things', 'It', 'Game of Thrones', 'Friends']
valores = [5.0, 4.5, 4.3, 4.1]

plt.bar(categorias, valores)
plt.show()
plt.savefig('./exercicios/ex01.png')

plt.clf()


categorias = ['iPhone 17 Pro Max', 'iPhone 17', 'Xiaomi 17']
valores = [200000, 320000, 500000]

plt.bar(categorias, valores)
plt.show()
plt.savefig('./exercicios/ex02.png')

# 3) Identifique na turma qual é o time de cada um e construa um gráfico de barras para mostrar a popularidade cada time.
#gremio: 3; flamengo: 2; palmeiras: 1; inter: 2; vasco: 1;

plt.clf()

times = ['Grêmio', 'Palmeiras', 'flamengo', 'internacional', 'vasco']
torcedores = [2, 1, 2, 2, 1]
cores = ['#0D80BF', '#006437', '#C52613', '#E5050F', '#000000']
plt.bar(times, torcedores, color=cores)
plt.show()
plt.xlabel()
plt.ylabel()
plt.savefig('./exercicios/ex03.png')