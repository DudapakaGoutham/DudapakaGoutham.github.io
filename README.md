# Sales Data Analysis Project

**Author:** Goutham Dudapaka  
**Tools:** Python, Pandas, Matplotlib, SQL; optional Power BI

## Important data note
`sales_data.csv` is synthetic sample data created for learning and demonstration. It is not real company data. Describe the project honestly as a sample-data analysis.

## Objective
Calculate sales revenue, cost, profit and profit margin; compare performance by month, product category, region and sales channel.

## Dataset columns
- `order_date`: order date
- `region`: sample sales region
- `category`: product category
- `product`: product name
- `quantity`: units in the order row
- `unit_price_inr`: selling price per unit (INR)
- `unit_cost_inr`: cost per unit (INR)
- `sales_channel`: Online or Retail

## Run the analysis
Install Python 3, then run:

```bash
pip install pandas matplotlib
python analyze_sales.py
```

The script creates an `output/` folder with summary metrics, monthly/category/region tables, cleaned data and PNG charts.

## SQL
See `sales_analysis.sql` for practice queries. Import the CSV into a database table called `sales_data` first. SQL date functions vary by database.

## Optional Power BI dashboard
Import `output/cleaned_sales_data.csv` into Power BI and add:
- KPI cards: Revenue, Profit, Profit Margin, Units Sold
- Line chart: Month vs Revenue
- Bar chart: Category vs Revenue
- Bar chart: Region vs Profit
- Slicers: Region, Category, Sales Channel

## Portfolio description
Analyzed synthetic sales data using Python and Pandas, calculated revenue and profit metrics, and compared monthly, category and regional performance. Exported summary tables and visualizations to support basic business reporting.

## Improvements to make
Add a screenshot of your Power BI dashboard and explain 2–3 findings after reviewing the output. Only list tools and results you can explain in an interview.
