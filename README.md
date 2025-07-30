# GA4 Traffic Breakdown for E-commerce

This project simulates and analyzes Google Analytics 4 (GA4) traffic data for an e‑commerce site, focusing on:

1. **Traffic Trends**: daily/weekly active users  
2. **Cohort Retention**: monthly user retention rates  
3. **Lifetime Value (LTV)**: cumulative revenue per cohort  
4. **Engagement & Conversion Funnel**: event depth and drop‑off analysis  

---

## 📁 Project Structure

```

project-3-ga4-traffic-breakdown/
│
├── data/
│   └── ga4\_sample\_data.csv        
│
├── scripts/
│   └── mock\_ga4\_data\_generator.py   
│
├── notebooks/
│   └── traffic\_breakdown\_analysis.ipynb  
│
├── visuals/                       
│   ├── monthly\_retention.png
│   └── cohort\_cumulative\_ltv.png
│
├── .gitignore
├── README.md
└── requirements.txt

````

---

## 🛠️ Installation & Usage

1. **Clone repo**  
   ```bash
   git clone https://github.com/your-username/project-3-ga4-traffic-breakdown.git
   cd project-3-ga4-traffic-breakdown
   ```

2. **Cài đặt dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Generate Mock Data**

   ```bash
   python scripts/mock_ga4_data_generator.py
   ```

4. **Chạy Jupyter Notebook**

   ```bash
   jupyter notebook notebooks/traffic_breakdown_analysis.ipynb
   ```

---

## 📊 Key Findings

* **Daily/Weekly Active Users**: DAU/WAU ratio \~ 0.6 ⇒ good stickiness
* **Monthly Retention**:

  * Jan 2025 cohort: 64% Month 1 → 18% Month 2
  * Feb 2025 cohort: 32% Month 1 → 0% Month 2
* **Cumulative LTV**:

  * Jan 2025 cohort: \$325 K → \$410 K → \$422 K
  * Feb 2025 cohort: \$113 K → \$124 K → \$0
* **Conversion Funnel**:

  * Drop‑off view → add\_to\_cart: 45%
  * Drop‑off add\_to\_cart → purchase: 70%

---

## 🎯 Recommendations

1. **Scale January’s acquisition channels** — replicate high‑value campaign setups.
2. **Plug Month 2 churn** — set up automated re‑engagement at day 30 (email/push).
3. **Audit February’s funnel** — improve landing pages & onboarding flows.
4. **Incentivize early purchases** in newer cohorts (e.g. March) with first‑order discounts.
5. **Optimize conversion funnel** — reduce friction at “add to cart” and “checkout” steps.

---

## 👤 Author

**Pham Ba Phuoc** – Aspiring Marketing Analyst

* GitHub: https://github.com/pbphuoc3927
* LinkedIn: https://www.linkedin.com/in/pham-ba-phuoc-61a02527a/
