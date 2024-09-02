COPY (
	WITH Quarterly_Orders AS (
    SELECT c.customerkey,
           c.firstname,
           c.lastname,
           c.emailaddress,
           EXTRACT(QUARTER FROM s.orderdate) AS quarter,
           COUNT(s.ordernumber) AS num_orders
    FROM sales AS s
    JOIN customers AS c
        ON c.customerkey = s.customerkey
    WHERE s.orderdate BETWEEN '2016-07-01' AND '2017-06-30'
    GROUP BY c.customerkey, c.firstname, c.lastname, c.emailaddress, EXTRACT(QUARTER FROM s.orderdate)
),
Customers_In_All_Quarters AS (
    SELECT customerkey,
           firstname,
           lastname,
           emailaddress
    FROM Quarterly_Orders
    GROUP BY customerkey, firstname, lastname, emailaddress
    HAVING COUNT(DISTINCT quarter) = 4
),
Total_Orders_By_Customer AS (
    SELECT c.customerkey,
           c.firstname,
           c.lastname,
           c.emailaddress,
           COUNT(s.ordernumber) AS total_orders
    FROM sales AS s
    JOIN customers AS c
        ON c.customerkey = s.customerkey
    JOIN Customers_In_AllQuarters AS ci
        ON ci.customerkey = c.customerkey
    WHERE s.orderdate BETWEEN '2016-07-01' AND '2017-06-30'
    GROUP BY c.customerkey, c.firstname, c.lastname, c.emailaddress
)
SELECT *
FROM Total_Orders_By_Customer
ORDER BY total_orders DESC
LIMIT 1
) TO 'C:/lucas/Hackathon SantoDigital/Desafio_I_engDados/queries/resultados/questao2.csv' WITH CSV HEADER;
