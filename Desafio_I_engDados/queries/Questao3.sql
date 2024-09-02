COPY (
	WITH monthly_revenue AS (
		SELECT 
			DATE_TRUNC('month', s.orderdate) AS month,
			SUM(p.productprice * s.orderquantity) AS total_revenue,
			AVG(p.productprice * s.orderquantity) AS avg_revenue_per_sale
		FROM sales AS s
		JOIN products AS p 
			ON s.productkey = p.productkey
		GROUP BY month
		HAVING AVG(p.productprice * s.orderquantity) > 500
	)
	SELECT 
		month,
		SUM(total_revenue) AS total_monthly_revenue
	FROM monthly_revenue
	GROUP BY month
	ORDER BY total_monthly_revenue DESC
	LIMIT 1
	) TO 'C:/lucas/Hackathon SantoDigital/Desafio_I_engDados/queries/resultados/questao3.csv' WITH CSV HEADER;

