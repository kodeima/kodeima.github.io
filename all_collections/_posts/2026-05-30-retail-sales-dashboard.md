---
layout: post
title: "Retail Sales Performance Analysis Using SQL & Power BI"
date: 2026-05-30
categories: [data-analysis, sql, powerbi, business-intelligence]
---

### Overview

This project analyses retail sales data to uncover key business insights around revenue, product performance, and regional trends. The goal was to simulate a real-world business reporting system that helps stakeholders make data-driven decisions.

### Business Problem

Retail businesses generate large volumes of transaction data but often struggle to convert that data into actionable insignts. This project demonstrates how sales data can be transformed into meaningful information for decision-making.

The business needed answers to:

- Which products generate the highest revenue?
- Which regions are underperforming?
- How do sales trends change over time?
- What factors drive revenue growth or decline?

---

### Tools Used

- SQL (MySQL) for data extraction and transformation
- Power BI for dashboard development and visualisation
- Excel for initial data creation and validation
- GitHub Pages for project documentation and portfolio presentation

---

### Dataset Download

You can download the full dataset used in this project below:

[Download Energy_Dataset.csv](/assets/data/Energy_Dataset.csv)

The dataset contains 100 sales transactions and includes:

- Order ID
- Order Date
- Customer ID
- Product
- Category
- Region
- Quantity
- Unit Price
- Payment Method

Please note all result outputs have been converted to CSV files

---

### Analysis Performed

- Total revenue calculation

```sql
select
    round(sum(quantity * unit_price), 2) revenue
    from sales_data;
```

[View Output Here](/assets/data/total_rev.csv)

This answers the question of total revenue from the earliest date to latest.

---

- Revenue by region

```sql
select
    region,
    round(sum(quantity * unit_price), 2) revenue
from sales_data
group by region
order by revenue desc;
```
[View Output Here](/assets/data/rev_by_reg.csv)

The region that generates the most revenue is seen to be East, and the regions that are underperforming are South and Central.

---

- Revenue by product category

```sql
select
    category,
    round(sum(quantity * unit_price), 2) revenue
from sales_data
group by category
order by revenue desc;
```

[View Output Here](/assets/data/rev_by_prod.csv)

From the results we can see that Fuel contributes the most to the total revenue. 

Although it generates the most revenue, fuel itself has very low margins.

Therefore fuel was the highest-performing category, generating **$1,073,467.12** in revenue and contributing **31.74%** of total revenue during the analysis period. This performance appears to be driven primarily by high sales volume rather than premium pricing.

---

## Product Performance

- Top-selling products by revenue

```sql
select
    product,
    round(sum(quantity * unit_price), 2) revenue
    from sales_data
    group by product
    oder by revenue desc
    limit 10;
```

[View Output Here](/assets/data/top_prod_by_rev.csv)

#### Product Performance Analysis

Analysis of product-level revenue revealed that **Lubricant Oil** was the highest performing individual product, generating **$607,889.95** in revenue, followed by **Inverter Battery ($552,094.45)** and **LPG Cylinder ($493,999.91)**.

While the fuel category contributed the largest share of overall revenue **(31.74% of total revenue)**, a deeper product-level analysis showed that no single fuel product was the top revenue generator. Instead, the category's strong performance was driven by the combined sales of multiple fuel products, including Kerosene, Diesel, and Petrol. 

This distinction is important because it suggests that the fuel category's success is primarily volume-driven and diversified across several products, rather than dependent on a single high-performing item.

Management should continue monitoring demand across the fuel category due to its signnificant revenue contribution. However, special attention should be given to Lubricant oil, which demonstrated the strongest individual product performance and may offer opportunities for increased revenue through focused promotional campaigns and inventory planning.

---

- Top-selling products by quantity

```sql
select
    product,
    sum(quantity) units_sold
from sales_data
group by product
order by units_sold desc
limit 10;
```

[View Output Here](/assets/data/top_prod_by_unit.csv)

Comparing the result of Revenue rank vs Quantity sold rank

|       Product       |  Revenue Rank    |  Quantity Sold Rank    |
| :------------------ | :--------------- | :--------------------- |
|    Lubricant oil    |        1         |           3            |
|   Inverter Battery  |        2         |           1            |
| LPG Cylinder Refill |        3         |           2            |
|      Kerosene       |        4         |           5            |
|       Diesel        |        5         |           4            |

To get revenue per unit sold, the query was used:

```sql
select
    product,
    round(sum(quantity * unit_price) / sum(quantity), 2) revenue_per_unit
from sales_data
group by product
order by revenue_per_unit desc;
```

[View Output Here](/assets/data/rev_per_unit.csv)

Product performance varied significantly depending on the metric used. Inverter batteries recorded the highest sales volume **(878 units)**, indicating strong customer demand. Lubricant oil generated the highest total revenue **(607,889.95)**, demonstrating the strongest overall financial contribution.

Meanwhile, Industrial gas produced the highest revenue per unit **($767.36)**, suggesting a premium-value product with lower sales volume. 

These findings highlight the importance of evaluating product performance through multiple dimensions rather than relying on a single metric.

---

- Category Comparison

```sql
select
    category,
    count(*) as orders,
    sum(quantity) as units_sold,
    round(sum(quantity * unit_price), 2) revenue
from sales_data
group by category
order by revenue desc;
```

---


## Time Analysis

- Monthly sales trends

```sql
select
    date_format(oder_date, '%y-%m') month,
    round(sum(quantity * unit_price), 2) revenue
from sales_data
group by month
order by month;
```

---

- Peak sales periods

```sql
select
    date_format(order_date, '%y-%m') month,
    round(sum(quantity * unit_price), 2) revenue
from sales_data
group by month
order by revenue desc;
```
