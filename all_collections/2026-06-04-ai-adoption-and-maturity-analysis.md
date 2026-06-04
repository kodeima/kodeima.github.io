---
layout: post
title: "AI Adoption & Maturity Analysis (2015-2025)"
date: 2026-06-04
categories: [Exploratory Data Analysis, Time Series Analysis, CAGR Modelling]
---

### Overview

This project investigates how AI maturity has evolved across **10 industries** and **15 countries** over a decade (2015-2025). The central question driving the analysis: *does geography or industry have a stronger influence on AI adoption levels?*

Working from a corporate AI adoption dataset, I engineered group time series aggregations, computed industry-level Compound Annual Growth Rates (CAGR), and produced a suite of interactive visualisations to surface actionable insights about the global AI landscape.

---

### Buisness Questions Addressed

- How has AI maturity changed across industries from 2015 to 2025?
- Which industries show the highest level of AI maturity, and which are adopting AI the fastest?
- How does AI maturity vary across countries, and do developed economies consistently outpace emerging ones?
- Does geographical location play a meaningful role in AI maturity levels?
- How do industry and geography interact to influence AI maturity?
- Which country-industry combinations show the highest and lowest maturity?
- Which sectors are experiencing the fastest AI transformation (by CAGR)?

---

### Methodology

#### Data Preparation
```python

import pandas as pd
import plotly.express as pxx

df = pd.read_csv('corporate_ai_adoption_dataset.csv')

# coerce year column to numeric and drop incomplete records

df['year'] = pd.to_numeric(df['year'], errors='coerce')
df = df.dropna(subset=['industry', 'country', 'ai_maturity_score', 'ai_adoption_level'])
```

**Why this matters:** Coercing the `year` column and removing nulls in key analytical columns ensures that all downstream aggregations and groth calculations operated on clean, consistent data. Preventing silent errors in the CAGR computation.