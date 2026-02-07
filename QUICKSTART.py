"""
Quick Start Guide - Day 1 Actions
"""

# 1. INSTALL DEPENDENCIES
# Run in terminal:
# pip install -r requirements.txt

# 2. CHOOSE BUSINESS CASE (EXAMPLE: E-COMMERCE)
# - Customers: users making online purchases
# - Target: reduce churn (customer lifetime value loss)
# - Campaign: email/push to drive repeat purchases

# 3. GET DATA
# Option A: Use Kaggle dataset
#   - https://www.kaggle.com/datasets/blastchar/telco-customer-churn
#   - https://www.kaggle.com/datasets/carrie1/ecommerce-data
#   - Download → place in data/raw/

# Option B: Generate synthetic data (for quick start)
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_sample_data(n_customers=5000):
    """Generate realistic e-commerce customer data"""
    
    np.random.seed(42)
    
    dates = [
        datetime(2023, 1, 1) + timedelta(days=int(x))
        for x in np.random.beta(2, 5, n_customers) * 365
    ]
    
    data = {
        'customer_id': range(1, n_customers + 1),
        'age': np.random.randint(18, 70, n_customers),
        'region': np.random.choice(['US', 'EU', 'ASIA', 'OTHER'], n_customers),
        'registration_date': dates,
        'total_purchases': np.random.exponential(5, n_customers).astype(int) + 1,
        'total_value': np.random.exponential(500, n_customers),
        'avg_order_value': np.random.gamma(5, 20, n_customers),
        'days_since_last_purchase': np.random.exponential(30, n_customers).astype(int),
        'website_visits': np.random.exponential(10, n_customers).astype(int),
        'email_opens': np.random.binomial(20, 0.4, n_customers),
        'campaign_received': np.random.binomial(10, 0.6, n_customers),
        'campaign_response': np.random.binomial(1, 0.15, n_customers),
        # TARGET VARIABLE
        'churn': np.random.binomial(
            1,
            np.random.beta(2, 8, n_customers)  # Most customers don't churn
        ),
    }
    
    return pd.DataFrame(data)

# 4. SAMPLE CODE TO START
if __name__ == '__main__':
    # Generate or load data
    df = generate_sample_data(5000)
    
    # Save to data/raw/
    df.to_csv('data/raw/customers.csv', index=False)
    print(f"✅ Dataset created: {df.shape}")
    print(f"\nData sample:\n{df.head()}")
    print(f"\nChurn rate: {df['churn'].mean()*100:.1f}%")
    print(f"Response rate: {df['campaign_response'].mean()*100:.1f}%")

# 5. NEXT STEPS
"""
Once data is ready:

✅ Day 1: Data Exploration (EDA)
   → Run notebooks/01_eda.ipynb
   
✅ Day 2: Feature Engineering
   → Run notebooks/02_feature_engineering.ipynb
   
✅ Day 3: ML Model Training
   → Run src/models/train.py
   
✅ Day 4: Dashboard
   → streamlit run dashboard/app.py

For detailed structure, see README.md
"""
