import matplotlib.pyplot as plt

categorias = ['iPhone 17 Pro Max', 'iPhone 17', 'Xiaomi 17']
valores = [200000, 320000, 500000]

plt.bar(categorias, valores)
plt.show()
plt.savefig('./exercicios/ex02.png')