COPY (
	SELECT p.productname AS product, 
       p.modelname,
       pc.category_name,
       SUM(s.orderquantity) AS total_quantity
	FROM sales AS s
	JOIN products AS p 
    	ON p.productkey = s.productkey
	JOIN productsubcategories AS ps
		ON p.productsubcategorykey = ps.productsubcategorykey
	JOIN poducts_categories AS pc
		ON ps.productsubcategorykey = pc.product_category_key
	WHERE pc.product_category_key = 1 
	  AND s.orderdate >= '2017-06-30'::date - INTERVAL '2 years'
	GROUP BY p.productname, p.modelname, pc.category_name
	ORDER BY total_quantity DESC
	LIMIT 10
	) TO 'C:/lucas/Hackathon SantoDigital/Desafio_I_engDados/queries/resultados/questao1.csv' WITH CSV HEADER;
