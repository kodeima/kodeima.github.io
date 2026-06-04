import pandas as pd
import plotly.express as px

df = pd.read_csv('corporate_ai_adoption_dataset.csv')

print(df.head(10))

df['year']= pd.to_numeric(df['year'], errors='coerce')

df = df.dropna(subset=['industry', 'country', 'ai_maturity_score', 'ai_adoption_level'])

industry_trends = df.groupby(['industry', 'year'])['ai_maturity_score'].mean().reset_index()

country_trends = df.groupby(['country', 'year'])['ai_maturity_score'].mean().reset_index()

# CAGR = (Ending Value / Beginning Value)^(1 / Number of Years) - 1

growth = industry_trends.groupby('industry').apply(
    lambda x: ((x.loc[x['year']==2025, 'ai_maturity_score'].values[0] / 
                x.loc[x['year']==2015, 'ai_maturity_score'].values[0]) ** (1/10) -1)
).reset_index(name= 'CAGR')

fig = px.line(industry_trends,
              x = 'year', y = 'ai_maturity_score',
              color = 'industry',
              title = "AI Maturity Trends by Industry (2015 - 2025)")

fig.show()

fig = px.line(country_trends,
              x = 'year', y = 'ai_maturity_score',
              color = 'country',
              title = "AI Maturity Trends by Country (2015 - 2025)")

fig.show()

# Industry with the most rapid growth

print(growth.sort_values('CAGR', ascending = False).head(1))

# Geographical role

# geo_corr = country_trends.groupby('country')['ai_maturity_score'].mean().corr(
#     industry_trends.groupby('industry')['ai_maturity_score'].mean()
# )

# print("Correlation between geography and industry maturity:", geo_corr)

# Average maturity scores by country and industry
country_trends.groupby('country')['ai_maturity_score'].mean()

industry_trends.groupby('industry')['ai_maturity_score'].mean()

# Which industries are most mature today?

current_maturity = industry_trends[industry_trends['year'] == 2025].sort_values('ai_maturity_score', ascending=False)

print(current_maturity[['industry', 'ai_maturity_score']])

# Does geography play a role in AI maturity?
country_avg = df.groupby('country')['ai_maturity_score'].mean()

print(country_avg.sort_values(ascending=False))

# Visualize
country_avg_df = (
    df.groupby('country')['ai_maturity_score'].mean().reset_index()
)
fig = px.bar(
    country_avg_df,
    x='country',
    y='ai_maturity_score',
    title='Average AI Maturity by Country'
)
fig.show()

# For the same industry, do certain countries show higher maturity scores than others?

country_industry = df.groupby(
    ['country', 'industry']
)['ai_maturity_score'].mean().reset_index()

fig = px.bar(
    country_industry,
    x='country',
    y='ai_maturity_score',
    color='industry',
    title='Average AI Maturity by Country and Industry'
)

fig.show()

# AI Maturity CAGR by Industry (2015-2025), which industries are growing the fastest?

print(growth.sort_values('CAGR', ascending=False).head(5))

cagr_fig = px.bar(
    growth,
    x='industry',
    y='CAGR',
    title='AI Maturity CAGR by Industry (2015-2025)'
)
cagr_fig.show()