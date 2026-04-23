import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('./dados/dados.csv')

print(df)

print(df.head())

plt.boxplot(df['nota'])
plt.title('Boxplot das notas')
plt.ylabel('Notas')
plt.show()
plt.savefig('aula05-boxplot')