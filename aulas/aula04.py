import pandas as pd


# criação do data frame
df = pd.DataFrame({
    "Idade":[20,22,20,23,24]
})


print(df['Idade'].describe())

print("Média: " +str(df['Idade'].mean()))
print('Mediana: ' + str(df['Idade'].median()))
print("Moda: " +str(df['Idade'].mode()))

