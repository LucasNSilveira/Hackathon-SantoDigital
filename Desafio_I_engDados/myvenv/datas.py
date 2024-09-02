import pandas as pd

# Correções de erros para importar os dados para o Postgres

data_calendar =  pd.read_csv("C:\\lucas\\Hackathon SantoDigital\\Desafio_I_engDados\\adventureWorks\\AdventureWorks_Calendar.csv")
print(data_calendar.head())
data_calendar['Date'] = pd.to_datetime(data_calendar['Date'], format='%m/%d/%Y').dt.strftime('%Y-%m-%d')
data_calendar.to_csv("C:\\lucas\\Hackathon SantoDigital\\Desafio_I_engDados\\adventureWorks\\AdventureWorks_Calendar_corrected.csv", index=False)

# Dados dos clientes
data_customer = pd.read_csv("C:\\lucas\\Hackathon SantoDigital\\Desafio_I_engDados\\adventureWorks\\AdventureWorks_Customers.csv", encoding='ISO-8859-1')
data_customer['AnnualIncome'] = data_customer['AnnualIncome'].replace('[\\$,]', '', regex=True).astype(float)
data_customer['BirthDate'] = pd.to_datetime(data_customer['BirthDate'], format='%m/%d/%Y').dt.strftime('%Y-%m-%d')
data_customer.to_csv("C:\\lucas\\Hackathon SantoDigital\\Desafio_I_engDados\\adventureWorks\\AdventureWorks_Customers_corrected.csv", index=False)

# Dados de Vendas
data_sales2015 =  pd.read_csv("C:\\lucas\\Hackathon SantoDigital\\Desafio_I_engDados\\adventureWorks\\AdventureWorks_Sales_2015.csv")
data_sales2015['OrderDate'] = pd.to_datetime(data_sales2015['OrderDate'], format='%m/%d/%Y').dt.strftime('%Y-%m-%d')
data_sales2015['StockDate'] = pd.to_datetime(data_sales2015['StockDate'], format='%m/%d/%Y').dt.strftime('%Y-%m-%d')

data_sales2016 =  pd.read_csv("C:\\lucas\\Hackathon SantoDigital\\Desafio_I_engDados\\adventureWorks\\AdventureWorks_Sales_2016.csv")
data_sales2016['StockDate'] = pd.to_datetime(data_sales2016['StockDate'], format='%m/%d/%Y').dt.strftime('%Y-%m-%d')
data_sales2016['OrderDate'] = pd.to_datetime(data_sales2016['OrderDate'], format='%m/%d/%Y').dt.strftime('%Y-%m-%d')

data_sales2017 =  pd.read_csv("C:\\lucas\\Hackathon SantoDigital\\Desafio_I_engDados\\adventureWorks\\AdventureWorks_Sales_2017.csv")
data_sales2017['StockDate'] = pd.to_datetime(data_sales2017['StockDate'], format='%m/%d/%Y').dt.strftime('%Y-%m-%d')
data_sales2017['OrderDate'] = pd.to_datetime(data_sales2017['OrderDate'], format='%m/%d/%Y').dt.strftime('%Y-%m-%d')
data_sales = pd.concat([data_sales2015, data_sales2016, data_sales2017], ignore_index=True)
print(data_sales.head())
data_sales.to_csv("C:\\lucas\\Hackathon SantoDigital\\Desafio_I_engDados\\adventureWorks\\AdventureWorks_Sales_corrected.csv", index=False)

# Territórios
data_territory =  pd.read_csv("C:\\lucas\\Hackathon SantoDigital\\Desafio_I_engDados\\adventureWorks\\AdventureWorks_Territories.csv")

# Retornos 
data_returns =  pd.read_csv("C:\\lucas\\Hackathon SantoDigital\\Desafio_I_engDados\\adventureWorks\\AdventureWorks_Returns.csv")
data_returns['ReturnDate'] = pd.to_datetime(data_returns['ReturnDate'], format='%m/%d/%Y').dt.strftime('%Y-%m-%d')
data_returns.to_csv("C:\\lucas\\Hackathon SantoDigital\\Desafio_I_engDados\\adventureWorks\\AdventureWorks_Returns_corrected.csv", index=False)
