import pandas as pd

# Correções de erros para importar no Postgres
# Carregar os arquivos CSV
data_product_cat = pd.read_csv("C:\\lucas\\Hackathon SantoDigital\\Desafio_I_engDados\\adventureWorks\\AdventureWorks_Product_Categories.csv")
data_products_subcat = pd.read_csv("C:\\lucas\\Hackathon SantoDigital\\Desafio_I_engDados\\adventureWorks\\AdventureWorks_Product_Subcategories.csv")
data_products = pd.read_csv("C:\\lucas\\Hackathon SantoDigital\\Desafio_I_engDados\\adventureWorks\\AdventureWorks_Products.csv", encoding="ISO-8859-1")

# Mapear SubcategoryName para ProductSubcategoryKey
mapping = dict(zip(data_products_subcat['SubcategoryName'], data_products_subcat['ProductSubcategoryKey']))
print(mapping)

# Aplicar o mapeamento para corrigir a coluna ProductSubcategoryKey
data_products['ProductSubcategoryKey'] = data_products['ProductSubcategoryKey'].map(mapping)
data_products.to_csv("C:\\lucas\\Hackathon SantoDigital\\Desafio_I_engDados\\adventureWorks\\AdventureWorks_Products_corrected.csv", index=False)

# Verificar se a correção foi aplicada corretamente
data2 = pd.read_csv("C:\\lucas\\Hackathon SantoDigital\\Desafio_I_engDados\\adventureWorks\\AdventureWorks_Products_corrected.csv", encoding="ISO-8859-1")

# Se os dados estiverem nulos, aplicar o merge para corrigir
if data2['ProductSubcategoryKey'].isnull().all():
    print("Os dados são nulos")
    merged_data = pd.merge(data2, data_products[['ProductKey', 'ProductSubcategoryKey']], on='ProductKey')
    data2['ProductSubcategoryKey'] = merged_data['ProductSubcategoryKey_y'].fillna(merged_data['ProductSubcategoryKey_x'])
    print(data2.head())

# Salvar o arquivo final corrigido
data2.to_csv("C:\\lucas\\Hackathon SantoDigital\\Desafio_I_engDados\\adventureWorks\\AdventureWorks_Products_corrected_2.csv", index=False)
