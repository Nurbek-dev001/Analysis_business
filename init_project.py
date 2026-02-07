"""
Initialize Predictive Analytics MVP Project
Run this to set up everything for Day 1
"""

import os
import sys
import subprocess
from pathlib import Path
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def print_header(text):
    print(f"\n{'='*70}")
    print(f"🚀 {text}")
    print(f"{'='*70}\n")

def check_python_version():
    """Check Python version"""
    print_header("Checking Python Version")
    version = f"{sys.version_info.major}.{sys.version_info.minor}"
    print(f"✅ Python {version}")
    if sys.version_info < (3, 9):
        print("⚠️ Recommended Python 3.9+")

def install_dependencies():
    """Install required packages"""
    print_header("Installing Dependencies")
    
    try:
        print("Installing packages from requirements.txt...")
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-q",
            "-r", "requirements.txt"
        ])
        print("✅ Dependencies installed successfully")
    except Exception as e:
        print(f"⚠️ Warning: {e}")
        print("Try manual install: pip install -r requirements.txt")

def create_directories():
    """Create all necessary directories"""
    print_header("Creating Directory Structure")
    
    dirs = [
        'data/raw',
        'data/processed',
        'notebooks',
        'src',
        'models',
        'outputs',
        'logs'
    ]
    
    for dir_path in dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        print(f"✅ {dir_path}")

def generate_sample_data():
    """Generate realistic sample dataset"""
    print_header("Generating Sample Dataset")
    
    output_file = 'data/raw/customers.csv'
    
    if Path(output_file).exists():
        print(f"ℹ️ Dataset already exists at {output_file}")
        return
    
    print("Creating synthetic e-commerce customer dataset...")
    print("- 5,000 customers")
    print("- Demographics, behavior, and marketing data")
    print("- Churn and campaign response targets")
    
    n_customers = 5000
    np.random.seed(42)
    
    # Generate dates
    dates = [
        datetime(2023, 1, 1) + timedelta(days=int(x))
        for x in np.random.beta(2, 5, n_customers) * 365
    ]
    
    # Create dataset
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
        'churn': np.random.binomial(1, np.random.beta(2, 8, n_customers)),
    }
    
    df = pd.DataFrame(data)
    
    # Save dataset
    df.to_csv(output_file, index=False)
    print(f"✅ Dataset saved to {output_file}")
    
    # Print statistics
    print(f"\n📊 Dataset Statistics:")
    print(f"   Shape: {df.shape}")
    print(f"   Churn rate: {df['churn'].mean()*100:.1f}%")
    print(f"   Response rate: {df['campaign_response'].mean()*100:.1f}%")
    print(f"   Avg customer value: ${df['total_value'].mean():.2f}")

def verify_setup():
    """Verify everything is set up correctly"""
    print_header("Verifying Setup")
    
    checks = {
        'Project structure': Path('src').exists(),
        'Config file': Path('configs/config.yaml').exists(),
        'Sample data': Path('data/raw/customers.csv').exists(),
        'Dashboard app': Path('dashboard/app.py').exists(),
        'Requirements.txt': Path('requirements.txt').exists(),
    }
    
    all_passed = True
    for check_name, result in checks.items():
        status = "✅" if result else "❌"
        print(f"{status} {check_name}")
        all_passed = all_passed and result
    
    return all_passed

def print_next_steps():
    """Print next steps"""
    print_header("Next Steps")
    
    print("""
    📋 IMMEDIATE ACTIONS (Day 1-2):
    
    1. EXPLORE DATA
       python scripts/explore.py
       
    2. REVIEW FINDINGS
       - Check churn patterns
       - Identify key drivers
       - Review outputs/01_eda_overview.png
    
    3. UNDERSTAND CODE STRUCTURE
       - src/etl/ - Data loading
       - src/features/ - Feature engineering
       - src/models/ - ML models
       - src/metrics/ - Business metrics
       
    ─────────────────────────────────────────────────────────
    
    📊 WEEK 1 AGENDA:
    
    Day 1-2: Data Exploration & Feature Engineering
       → Understand customer behavior
       → Create business-relevant features
       
    Day 3-4: Model Training
       → Train churn prediction model
       → Train campaign response model
       
    Day 5: Integration
       → Connect models to business metrics
    
    ─────────────────────────────────────────────────────────
    
    🚀 WEEK 2 AGENDA:
    
    Day 6: Business Metrics
       → Calculate expected profit
       → Segment customers
       
    Day 7: Explainability (SHAP)
       → Understand model decisions
       → Generate business insights
       
    Day 8-9: AI Assistant + Integration
       → LLM for recommendations
       → Connect data pipeline
       
    Day 10: Dashboard
       → Streamlit interactive dashboard
       streamlit run dashboard/app.py
    
    ─────────────────────────────────────────────────────────
    
    💡 KEY FILES TO REVIEW:
    
    - README.md           → Full project overview
    - DAY_1_PLAN.md       → Today's checklist
    - QUICKSTART.py       → Example code
    - configs/config.yaml → Project configuration
    
    ─────────────────────────────────────────────────────────
    
    🎯 SUCCESS METRICS (By Day 10):
    
    ✅ Churn Model: ROC-AUC >= 0.85
    ✅ Marketing Model: ROC-AUC >= 0.80
    ✅ AI Assistant: Generates 3+ actionable insights
    ✅ Dashboard: All metrics visualized
    ✅ Code: Production-ready structure
    
    """)

def print_project_overview():
    """Print project overview"""
    print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║   🎯 PREDICTIVE ANALYTICS MVP FOR BUSINESS                  ║
    ║   Churn Prediction + Marketing Response + AI Recommendations ║
    ╚═══════════════════════════════════════════════════════════════╝
    
    📊 BUSINESS PROBLEM:
       • Reduce customer churn → Increase retention revenue
       • Optimize marketing budget → Target high-response customers
       • Make data-driven decisions → AI explains recommendations
    
    🏗️  TECH STACK:
       • Data: Pandas, NumPy
       • ML: XGBoost, LightGBM, SHAP
       • AI: OpenAI GPT-4 (with mock fallback)
       • Dashboard: Streamlit
       • Deployment: FastAPI, Docker
    
    ✨ UNIQUE FEATURES:
       • End-to-end pipeline (data → insights)
       • Explainable AI (SHAP interpretation)
       • Business metrics (profit/ROI calculation)
       • AI assistant (LLM recommendations)
       • Production-ready structure
    
    """)

def main():
    """Main initialization"""
    print_project_overview()
    
    # Check Python
    check_python_version()
    
    # Create directories
    create_directories()
    
    # Generate sample data
    generate_sample_data()
    
    # Install dependencies
    try_install = input("\n📦 Install Python dependencies? (y/n): ").strip().lower()
    if try_install == 'y':
        install_dependencies()
    
    # Verify setup
    print_header("Verification")
    if verify_setup():
        print("\n✅ ALL CHECKS PASSED")
    else:
        print("\n⚠️ Some checks failed - please verify manually")
    
    # Next steps
    print_next_steps()
    
    print(f"\n✅ Project initialized successfully at: {os.getcwd()}")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

if __name__ == '__main__':
    main()
