# Day 1 Action Plan - Predictive Analytics MVP

## 🎯 GOAL TODAY
- ✅ Understand the business problem
- ✅ Set up project structure (DONE ✓)
- ✅ Load/generate data
- ✅ Do initial exploration

---

## 📋 CHECKLIST

### Step 1: Generate Sample Data
```bash
cd /path/to/project
python QUICKSTART.py
```
This creates `data/raw/customers.csv` with 5000 customer records.

**What we have:**
- Demographic data (age, region)
- Behavior data (purchases, visits, email engagement)
- Marketing data (campaigns, responses)
- **TARGET**: churn (1 = left, 0 = stayed)

### Step 2: Verify Data Structure
```python
import pandas as pd

df = pd.read_csv('data/raw/customers.csv')
print(df.shape)          # (5000, 11) - 5000 customers, 11 features
print(df.info())        # Data types
print(df['churn'].value_counts())  # Churn distribution
```

**Expected output:**
```
Shape: (5000, 11)

Churn distribution:
0    4200 (84%)  ← Most stay
1     800 (16%)  ← Some leave
```

### Step 3: Exploratory Analysis
Key questions to answer:
1. **Churn patterns**
   - How does churn relate to purchase frequency?
   - Does recency matter?
   - Which regions have highest churn?

2. **Campaign response**
   - Who responds to campaigns?
   - Best customer segments?

3. **Feature correlations**
   - Which features matter most?

### Step 4: Next - Run EDA Notebook
Once data is ready, open the EDA notebook:
```bash
jupyter notebook notebooks/01_eda.ipynb
```

---

## 📊 Data Dictionary

| Column | Type | Meaning | Example |
|--------|------|---------|---------|
| customer_id | int | Unique customer | 1, 2, 3 |
| age | int | Customer age | 25-70 |
| region | str | Geographic region | US, EU, ASIA |
| registration_date | date | When joined | 2023-01-15 |
| total_purchases | int | All-time purchases | 1-50+ |
| total_value | float | Total spent ($) | 50-5000 |
| avg_order_value | float | Average order ($) | 10-200 |
| days_since_last_purchase | int | Recency (days) | 0-365 |
| website_visits | int | Site sessions | 0-50 |
| email_opens | int | Email engagement | 0-20 |
| campaign_received | int | Campaign emails sent | 0-10 |
| **campaign_response** | **int** | **Responded? (0/1)** | **0 or 1** |
| **churn** | **int** | **Left? (0/1)** | **0 or 1** |

---

## 🔬 First Hypothesis (Before Analysis)

**H1: Customers with low recency (days_since_purchase) have lower churn**
- Intuition: Active customers stay longer
- Test: Compare churn rates by purchase recency

**H2: Customers who respond to campaigns are more engaged**
- Intuition: Response = engagement
- Test: Compare response rate vs churn

**H3: High-value customers have lower churn**
- Intuition: Valuable customers get better retention
- Test: Compare churn by total_value quartiles

---

## 💻 Quick Python Script to Verify

```python
import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('data/raw/customers.csv')

# Test H1: Recency vs Churn
print("=" * 50)
print("Hypothesis 1: Recency vs Churn")
print("=" * 50)

# Split by recency quartiles
df['recency_quartile'] = pd.qcut(df['days_since_last_purchase'], q=4, labels=['Recent', 'Q2', 'Q3', 'Old'])
churn_by_recency = df.groupby('recency_quartile')['churn'].agg(['mean', 'count'])
print(churn_by_recency)
print()

# Test H2: Campaign Response vs Churn
print("=" * 50)
print("Hypothesis 2: Response vs Churn")
print("=" * 50)

churn_by_response = pd.crosstab(df['campaign_response'], df['churn'], normalize='index')
print("Churn rate by campaign response:")
print(f"Response = 0 (No):  {churn_by_response.loc[0, 1]:.2%}")
print(f"Response = 1 (Yes): {churn_by_response.loc[1, 1]:.2%}")
print()

# Test H3: Value vs Churn
print("=" * 50)
print("Hypothesis 3: Value vs Churn")
print("=" * 50)

df['value_quartile'] = pd.qcut(df['total_value'], q=4, labels=['Q1_Low', 'Q2', 'Q3', 'Q4_High'])
churn_by_value = df.groupby('value_quartile')['churn'].agg(['mean', 'count'])
print(churn_by_value)
```

---

## 📌 Success Criteria for Day 1

By end of day:
- ✅ Data loaded and explored
- ✅ Understand churn distribution
- ✅ Identify top 3 features correlating with churn
- ✅ Have 2-3 initial hypotheses

---

## ⏰ Timeline

- **15 min**: Data generation / loading
- **30 min**: Initial exploration
- **45 min**: Hypothesis testing
- **30 min**: Documentation

**Total: ~2 hours** (can be done parallelly with other work)

---

## 🚀 Ready to Start?

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Generate data
python QUICKSTART.py

# 3. Explore
python scripts/explore.py

# 4. (Optional) Start Jupyter
jupyter notebook
```

Next: **Day 2 - Feature Engineering** (see 02_feature_engineering_plan.md)
