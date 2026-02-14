# revenue-leakage-recovery-audit
This project addresses a critical financial risk: **Revenue Leakage**. By reconciling consultant-logged hours against client-billed invoices, I identified discrepancies caused by manual data entry errors and billing system mismatches. This automated audit can identify an average of **8-12% in unbilled revenue
# 💰 Revenue Leakage Recovery Audit

## 📋 Project Overview
This project addresses a critical financial risk: **Revenue Leakage**. By reconciling consultant-logged hours against client-billed invoices, I identified discrepancies caused by manual data entry errors and billing system mismatches. This automated audit can identify an average of **8-12% in unbilled revenue**.



## 🛠️ Technical Implementation
* **Fuzzy Matching:** Utilized `polyfuzz` and `RecordLinkage` to resolve inconsistencies in client naming conventions across HR and Finance databases.
* **Financial Reconciliation:** Automated the comparison of `revenue_logged` vs. `revenue_billed` to isolate leakages at the consultant level.
* **Aging Analysis:** Categorized leakages into 0-30, 31-60, and 60+ day buckets to prioritize immediate debt recovery efforts.

## 📊 Dashboard Features
* **KPI Metrics:** Real-time tracking of Total Leakage and Leakage Percentage.
* **Monthly Trends:** Visualizing the gap between work performed and work invoiced.
* **Client Risk Profile:** Identifying which clients or departments have the highest billing error rates.

## ⚙️ How to Run
1. Clone the repo.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run the dashboard: `streamlit run app.py`.
