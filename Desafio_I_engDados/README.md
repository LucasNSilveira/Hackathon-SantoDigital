# Desafio de Engenharia de Dados
Utilizei o dataset público [AdventureWorks](https://www.kaggle.com/datasets/ukveteran/adventure-works/code)  para as próximas questões. 
### Questão I

Quais são os 10 produtos mais vendidos (em quantidade) na categoria "Bicicletas", considerando apenas vendas feitas nos últimos dois anos?
____
__Premissas__
1. Precisava buscar as categorias principais (bicicletas), e as subcategorias das (mountainbike por exemplo).

### Questão II
Qual é o cliente que tem o maior número de pedidos realizados, considerando apenas clientes que fizeram pelo menos um pedido em cada trimestre do último ano fiscal?
____
__Premissas__
1. Fragmentar as consultas em subconsultas: "Pedidos trimestrais", Clientes em todos os trimestres,  todos os pedidos por clientes

### Questão III

Em qual mês do ano ocorrem mais vendas (em valor total), considerando apenas os meses em que a receita média por venda foi superior a 500 unidades monetárias?
______
__Premissas__
1. Separei a receita média por mês, depois verifiquei quais estavam acima de 500 unidades monetárias. 

### Questão IV
Quais vendedores tiveram vendas com valor acima da média no último ano fiscal e também tiveram um crescimento de vendas superior a 10% em relação ao ano anterior?
******
__Premissas__
1. O banco de dados original, importado do kaggle, não possuia dados acerca dos vendedores.
2. Foi gerado uma coluna `Sellerkey`, na tabela Sales, e com a função `random()` do Postgres foi preenchido a coluna aleatoriamente com valores de 1 a 7.
3. Como os dados não poderiam ser precisos, foi criado uma pesquisa que entregasse os dados em forma de `yes` ou `no`, para os vendedores que fizeram uma venda acima da venda média do último ano e para os vendedores que tiveram um aumento de 10% nas vendas.  

### Questão EXTRA 
Extra: Elabore e responda uma pergunta de negócio do seu interesse que envolva a utilização de subconsultas, funções de janela ou CTEs.\
__Questão elaborada__: qual foi a média trimestral de cada território e quais foram os produtos mais vendidos por mês?

## Resoluções 
Inicialmente foi utilizado Python e PostgreSQL para carregar os dados e gerar o banco de dados. Na pasta `queries`, estão localizados as consultas para a resolução de cada questão, incluindo a Extra. Dentro dela há uma pasta com os resultados `.csv`.
* __Python__
1. Desenvolvi um código para carregar os arquivos .csv e verificar algumas inconsistências nos dados. 
2. Alguns arquivos .csv tinham problemas de formatação nas datas e valores númericos com a presença de strings. Portanto, escrevi um script com o pandas para ler esses arquivos, formatá-los e salvá-los em outra pasta. 
3. Criei dois scripts, um para os dados relacionados aos produtos e os outros para os demais. As tabelas de produtos, categorias dos produtos e subcategorias, foram feitas separadamente, para verificar se as relações eram mantidas durante o processo de formatação. 
* __PostgreSQL__
1. Utilizei o software para carregar o banco de dados. Primeiramente, criei as tabelas e as referências entre cada tabela. Gerando o seguinte  diagrama de entidade  relacionamento:
![alt text](ERD.png)
2. Importei as tabelas corrigidas, para o Postgres.
3. Com isso, foi possível desenvolver cada script para responder as perguntas dos problemas