-- Practice SQL queries. Import sales_data.csv into a table named sales_data.
SELECT
  SUM(quantity * unit_price_inr) AS total_revenue,
  SUM(quantity * unit_cost_inr) AS total_cost,
  SUM(quantity * (unit_price_inr - unit_cost_inr)) AS total_profit
FROM sales_data;

SELECT category,
  SUM(quantity * unit_price_inr) AS revenue,
  SUM(quantity * (unit_price_inr - unit_cost_inr)) AS profit
FROM sales_data
GROUP BY category ORDER BY revenue DESC;

SELECT region, SUM(quantity * unit_price_inr) AS revenue
FROM sales_data GROUP BY region ORDER BY revenue DESC;

SELECT sales_channel, SUM(quantity * unit_price_inr) AS revenue,
  SUM(quantity) AS units_sold
FROM sales_data GROUP BY sales_channel ORDER BY revenue DESC;

-- SQLite monthly revenue query
SELECT strftime('%Y-%m', order_date) AS month,
  SUM(quantity * unit_price_inr) AS revenue
FROM sales_data
GROUP BY strftime('%Y-%m', order_date) ORDER BY month;
