import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Carregar os dados
vendas = pd.read_csv("C:\\lucas\\Hackathon SantoDigital\\Desafio_I_engDados\\adventureWorks_OK\\AdventureWorks_Sales_corrected.csv")
vendas = vendas.drop(['StockDate', 'OrderNumber', 'ProductKey', 'CustomerKey', 'TerritoryKey', 'OrderLineItem'], axis=1)

# Converter a coluna 'OrderDate' para datetime
vendas['OrderDate'] = pd.to_datetime(vendas['OrderDate'])

vendas.set_index('OrderDate', inplace=True)

vendas_mes = vendas.resample('M').sum()

print(vendas.head())

vendas_mes['month_number'] = np.arange(len(vendas_mes))
X = vendas_mes[['month_number']]
y = vendas_mes['OrderQuantity']
# x = vendas['OrderDate']
# y = vendas['OrderQuantity']
#plt.plot(x, y)
#plt.show()
#plt.plot()