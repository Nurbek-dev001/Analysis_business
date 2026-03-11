# 📊 Predictive Analytics Platform: Churn + Marketing + AI

---

## 🎯 Business Problem

**Why this matters?**
- **Churn**: 5% customer churn reduction → 25-30% profit increase in SaaS/subscriptions
- **Marketing**: Wasting budget on unresponsive customers → AI-driven targeting increases ROI by 40-60%
- **Decisions**: Without ML, businesses rely on intuition → we provide data-driven recommendations

---

## 🏗️ Project Architecture

```
DATA → ETL → FEATURES → ML MODELS → BUSINESS METRICS → AI ASSISTANT → DASHBOARD
                          ↓
                    EXPLAINABILITY (SHAP)
```

### Core Components

1. **Churn Prediction** (`src/models/churn_model.py`)
   - Binary classification: Will customer leave?
   - Model: XGBoost
   - Metrics: ROC-AUC, Recall, Precision

2. **Marketing Response** (`src/models/marketing_model.py`)
   - P(customer responds to campaign)
   - Enables ROI-optimized targeting

3. **Business Metrics Engine** (`src/metrics/business_metrics.py`)
   - Expected Revenue
   - Expected Cost
   - Expected Profit
   - Customer Lifetime Value (CLV)

4. **Explainability** (`src/explainability/shap_analysis.py`)
   - SHAP values for model interpretation
   - Feature importance
   - Business-ready insights

5. **AI Assistant** (`src/ai/llm_assistant.py`)
   - LLM-powered recommendations
   - Answers: "Should we run this campaign?", "Where's the profit?"

6. **Dashboard** (`dashboard/app.py`)
   - Real-time churn risk
   - Campaign profitability
   - AI recommendations

---

## 📂 Project Structure

```
.
├── data/
│   ├── raw/              # Original datasets
│   └── processed/        # Cleaned & featurized data
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_model_analysis.ipynb
├── src/
│   ├── etl/              # Data loading & ETL
│   ├── features/         # Feature engineering
│   ├── models/           # ML models
│   ├── metrics/          # Business metrics calculation
│   ├── explainability/   # SHAP analysis
│   └── ai/               # LLM integration
├── models/               # Saved trained models
├── dashboard/            # Streamlit app
├── configs/
│   ├── config.yaml       # Project configuration
│   └── model_config.yaml # Model hyperparameters
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

---



## 🚀 Quick Start

### Prerequisites
```bash
python >= 3.10
pip install -r requirements.txt
```

### Run EDA
```bash
jupyter notebook notebooks/01_eda.ipynb
```

### Train Models
```bash
python src/models/train.py
```

### Run Dashboard
```bash
streamlit run dashboard/app.py
```

---

## 📊 Data Requirements

**Customers**
- `user_id`: Unique identifier
- `age`, `region`: Demographics
- `registration_date`: Customer tenure

**Behavior**
- `total_purchases`: Number of transactions
- `avg_order_value`: Average spending
- `purchase_frequency`: Transactions per month
- `days_since_last_purchase`: Recency
- `engagement_score`: Website/app activity

**Marketing**
- `campaign_id`: Campaign identifier
- `campaign_type`: Email, Push, Discount, etc.
- `discount_size`: Campaign offer
- `response`: Binary (responded/ignored)

**Financial**
- `revenue`: Total customer value
- `cost`: Cost to acquire/retain
- `profit`: Revenue - cost

---

## 🔬 ML Models

### Model 1: Churn Prediction
**Target**: `churn` (0/1)  
**Algorithms**: Logistic Regression → Random Forest → XGBoost  
**Key Metrics**: ROC-AUC (≥0.85), Recall (≥0.75)  
**Business Impact**: Identify at-risk customers → targeted retention

### Model 2: Campaign Response
**Target**: `response` (0/1)  
**Algorithms**: Gradient Boosting, Neural Networks  
**Key Metric**: ROC-AUC (≥0.80)  
**Business Impact**: Select high-probability responders → save marketing budget

---

## 💰 Business Metrics

```python
Expected Profit = P(response) × Avg_Order_Value − Campaign_Cost

Customer Lifetime Value (CLV) = (Purchase_Frequency × Avg_Order_Value) × Customer_Lifespan
```

---

## 🤖 AI Assistant Features

**Questions it answers:**
- ✅ "Should we run campaign X for segment Y?"
- ✅ "How much profit will we make?"
- ✅ "Which customers are at highest risk?"
- ✅ "Where should we allocate budget?"

**Technology**: OpenAI API + RAG (retrieval-augmented generation)

---

## 🎓 Key Learning Outcomes

- ✅ End-to-end ML pipeline (data → production)
- ✅ Explainable AI (why did model decide?)
- ✅ Business metrics (ML → money)
- ✅ LLM integration (modern AI)
- ✅ Production architecture (not just notebooks)

---

## 📚 Tech Stack

| Component | Technology |
|-----------|-----------|
| **Data Processing** | Pandas, NumPy |
| **ML Models** | XGBoost, LightGBM, Scikit-learn |
| **Explainability** | SHAP, Feature importance |
| **AI Assistant** | OpenAI GPT-4 / LLaMA |
| **Dashboard** | Streamlit |
| **Deployment** | FastAPI, Docker |
| **Database** | PostgreSQL (optional) |

---

## 📈 Expected Results

By end of MVP:
- ✅ 2 trained ML models (Churn: ROC-AUC > 0.85, Response: ROC-AUC > 0.80)
- ✅ Business impact metrics (profit lift, customer segmentation)
- ✅ Explainable predictions (SHAP features)
- ✅ AI-driven recommendations
- ✅ Interactive dashboard
- ✅ Production-ready code

---





