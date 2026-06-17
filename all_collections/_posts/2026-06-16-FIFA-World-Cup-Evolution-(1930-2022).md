---
layout: post
title: "FIFA World Cup Evolution (1930-2022)"
date: 2026-06-16
categories: [Exploratory Data Analysis, Time Series Analysis, Descriptive Analysis, Correlation Analysis]
---

## Overview

The FIFA World Cup is the most prestigious international football tournament, bringing together nations from around the world every four years. Over the decades, the tournament has expanded significantly in size and popularity.

This project explores the evolution of the FIFA World cup from 1930 to 2022 using Python-based data analysis techniques. The analysis examines tournament growth, scoring trends, country performance, and the impact of tournament expansion on overall goal production.

Using Exploratory Data Analysis (EDA), trend analysis, comparative analysis, and correlation analysis, I investigated how the competition has changed over nearly a century. Key areas of focus include growth in participating teams, chnages in goals scored per matches, historical dominance of winning nations, and the relationship between match size and scoring output.

The project was developed using Python, Pandas, and Matplotlib, with fidings presented through data visualizations and statistical insights to tell the story of the World Cup's development over time.

---

### Questions Addressed

1. Has the number of participating teams increased over time?
2. Did the increase in participating teams lead to more goals being scored?
3. Has the number of matches increased over time?
4. Which world cup has the most goals?
5. Which country has won the most world cups?
6. Which countries frequently reach the final?
7. How often does the host nation win?

---

### Methodology

#### Dataset

The dataset contains historical FIFA World Cup tournament data from 1930 to 2022, including the columns:

- Year
- Host country
- Winner
- Runner up
- Third place
- Fourth place
- Total goals
- Matches played
- Teams
- Goals per match

---

#### Data Preparation
```python

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('fifa_world_cup_history.csv')

df.head(5)
df.info()
df.describe()

```

The initial exploration of the dataset was performed using:

- Data inspection
- Data structure analysis
- Summary statistics

This helped validate the dataset structure and understand the available variables before conducting deeper analysis (column datatype, empty cells/ null values, mean of a column with numerical values)

---

#### Trend Analysis

Trend analysis was used to evaluate how the World Cup has evolved over time by examining:

- Participating teams
- Matches played
- Goal-scoring patterns

* **Has the Number of Particiapting Teams Increased Over Time?**

A line chart was created to visualize the number of participating teams across all World cup tournaments.

```python
df[['Year', 'Teams']]

plt.figure(figsize=(10, 5))
plt.plot(df['Year'], df['Teams'], marker='o')
plt.title('Number of Participating Teams Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Teams')
plt.grid(True)

plt.show()
```

![Number of Team Over Time Chart](/assets/data/Num_of_team_over_time.png)

The analysis shows that FIFA has progressively expanded participation over time, making the competition more globally inclusive and increasing opportunities for nations to compete in the world cup.

* **Did More Participating Teams Lead to More Goals Being Scored?**

A scatter plor was created to examine the relationship between the number of teams and total goals scored.

```python
df[['Teams', 'Total_Goals', 'Year']]

plt.scatter(df['Teams'], df['Total_Goals'])
plt.xlabel('Teams')
plt.ylabel('Total Goals')
plt.show()

```

A correlation coefficient was then calculated.

```python
df[['Teams', 'Total_Goals']].corr()
```

The correlation value between Teams and Total Goals is **0.89**. This indicates a strong positive relationship between the tournament size and total goal scored.
As more teams participated, the total number of goals generally increased.
However, this increase is likely influenced by the larger number of matches played in expanded tournaments, which creates more scoring opportunities.

