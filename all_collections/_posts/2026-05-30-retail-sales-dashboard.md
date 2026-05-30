---
layout: post
title: "Retail Sales Performance Analysis Using SQL & Power BI"
date: 2026-05-30
categories: [data-analysis, sql, powerbi, business-intelligence]
---

# Retail Sales Performance Analysis (SQL + Power BI)


---

## Business Problems

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

## Tools Used

- SQL (MySQL) for data extraction and transformation
- Power BI for dashboard development and visualisation
- Excel for initial data creation and validation
- GitHub Pages for project documentation and portfolio presentation

---

## Dataset Download

You can download the full dataset used in this project below:

[Download Energy Dataset](/assets/data/Energy_Dataset.csv)

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

---

## Analysis Performed

- Total revenue calculation

```sql
select
    round(sum(quantity * unit_price), 2) revenue
    from sales_data;
```

- Revenue by region

```sql
select
    region,
    round(sum(quantity * unit_price), 2) revenue
from sales_data
group by region
order by revenue desc;
```


- Revenue by product category

```sql
select
    category,
    round(sum(quantity * unit_price), 2) revenue
from sales_data
group by category
order by revenue desc;
```

## Product Performance

- Top-selling products
- Category comparison

## Time Analysis

- Monthly sales trends
- Peak sales periods
