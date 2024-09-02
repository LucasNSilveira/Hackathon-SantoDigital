COPY
(
	WITH TerritoryQuarterlySales AS (
		SELECT 
			s.territorykey,
			t.region, 
			t.country,
			DATE_TRUNC('quarter', s.orderdate) AS quarter,
			SUM(s.orderquantity * p.productprice) AS total_sales
		FROM sales AS s
		JOIN products AS p
			ON s.productkey = p.productkey
		JOIN territories AS t
			ON t.salesterritorykey = s.territorykey
		GROUP BY s.territorykey, DATE_TRUNC('quarter', s.orderdate), t.region, t.country
	),
	TerritoryQuarterlyAvg AS (
		SELECT 
			territorykey, 
			AVG(total_sales) AS avg_quarterly_sales
		FROM TerritoryQuarterlySales
		GROUP BY territorykey
	)


	SELECT 
		s.territorykey,
		t.region,
		t.country,
		DATE_TRUNC('month', s.orderdate) AS month,
		p.productname,
		SUM(s.orderquantity) AS total_quantity
	FROM sales AS s
	JOIN products AS p
		ON s.productkey = p.productkey
	JOIN territories AS t
		ON t.salesterritorykey = s.territorykey
	GROUP BY s.territorykey, DATE_TRUNC('month', s.orderdate), p.productname, t.region, t.country
	ORDER BY s.territorykey, month, total_quantity DESC
	LIMIT 10
) TO 'C:/lucas/Hackathon SantoDigital/Desafio_I_engDados/queries/resultados/questao_extra.csv' WITH CSV HEADER;
