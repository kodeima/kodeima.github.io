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

This answers the question of total revenue from the earliest date to latest.

[View Output Here](/assets/data/total_rev.csv)

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

The region that generates the most revenue is seen to be East, and the regions that are underperforming are South and Central.

[View Output Here](/assets/data/rev_by_reg.csv)

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
