COPY (
	WITH annual_sales AS (
    -- Receita total por vendedor para cada ano fiscal
    SELECT 
        s.sellerkey,
        EXTRACT(YEAR FROM s.orderdate) AS year_,
		sum(s.orderquantity) as total_quantity,
        SUM(p.productprice * s.orderquantity) AS total_revenue
    FROM sales AS s
    JOIN products AS p 
        ON s.productkey = p.productkey
    GROUP BY s.sellerkey, EXTRACT(YEAR FROM s.orderdate)
),
last_year as (
	select max(date_part('year', s.orderdate)) as max_year
		from sales s 
),
 average_seller_sales AS (
     -- Receita média de vendas por vendedor no último ano fiscal
      SELECT 
          sellerkey,
          AVG(total_revenue) AS avg_revenue_last_year, year_
      FROM annual_sales, last_year
      WHERE year_ = last_year.max_year
      GROUP BY sellerkey, year_
)
,
growth AS (
     -- Receita total por vendedor no último ano fiscal e o ano anterior, e crescimento percentual
   SELECT
         s1.sellerkey,
		SUM((CASE WHEN s1.year_ = last_year.max_year THEN s1.total_revenue else 0 end)) total_last_year,
		SUM((CASE WHEN s1.year_ = last_year.max_year - 1  THEN s1.total_revenue else 0 end)) total_second_year
     FROM annual_sales AS s1, last_year
     where s1.year_ >= last_year.max_year - 1 AND s1.year_ <= last_year.max_year
	GROUP BY s1.sellerkey
),
average_sales_last_year as (
	select AVG(a.total_revenue) as average_sales_last_year from annual_sales as a, last_year
	where a.year_ = last_year.max_year
	
)
select s1.sellerkey, 
case when (total_last_year/total_second_year*100) -100 > 10 then 'yes' else 'no' end seller_10_more_year_before,
case when aas.avg_revenue_last_year > average_sales_last_year then 'yes' else 'no' end sales_avg_above_avg_last_year
from growth s1
join average_seller_sales aas on s1.sellerkey=aas.sellerkey, average_sales_last_year
order by s1.sellerkey
) TO 'C:/lucas/Hackathon SantoDigital/Desafio_I_engDados/queries/resultados/questao4.csv' with CSV HEADER;
