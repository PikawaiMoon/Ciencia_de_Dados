import matplotlib.pyplot as plt

categorias = ['Stranger Things', 'It', 'Game of Thrones', 'Friends']
valores = [5.0, 4.5, 4.3, 4.1]

plt.bar(categorias, valores)
plt.show()
plt.savefig('./exercicios/ex01.png')