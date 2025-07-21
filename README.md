# 📊 Sales KPI Dashboard

An interactive dashboard that tracks key sales metrics like top-performing products, category-wise trends, and order processing delays. Built with Python (Streamlit) for data handling and visualization, and optionally integrated with Power BI for executive-level reporting.

![Dashboard Preview](./Data/sales_kpi_dashboard.gif)
---

## 🚀 Features

- 🔍 **Top Products by Sales**
- 📦 **Category Performance Overview**
- ⏱️ **Order Processing Delay Insights**
- 📈 **Live Charts** powered by Plotly & Streamlit
- 🔄 Optional integration with **Power BI** for extended reporting

---

## 🧠 Why This Exists

Running e-commerce or B2B sales without clear KPIs is like flying blind. This dashboard provides clarity by turning raw data into meaningful visuals that can guide real business decisions.

---

## 🗂️ Directory Structure

```bash
Sales_KPI_Dashboard/
├── app.py
├── requirements.txt
├── utils/
│   ├── data_loader.py
│   ├── top_products.py
│   ├── category_performance.py
│   └── order_delay.py
├── data/
│   └── global_superstore.csv
├── assets/
│   ├── dashboard_preview.gif
│   ├── top_products.png
│   ├── category_perf.png
│   └── order_delay.png
└── README.md
```
## ⚙️ Setup & Usage

### 1. Clone the repo
```bash
git clone https://github.com/your-username/Sales_KPI_Dashboard.git
cd Sales_KPI_Dashboard
```
### 2. Install Dependencies
```bash
git clone https://github.com/your-username/Sales_KPI_Dashboard.git
cd Sales_KPI_Dashboard
```
### #. Run the dashboard
```bash
streamlit run app.py
```
## 💡 Ideas to Extend

- Add monthly targets vs. actuals  
- Trigger email alerts for KPI breaches  
- Live SQL/NoSQL data source hookup  
- Push to a web dashboard using Streamlit Cloud  

---

## 🙌 Credits

Built with ❤️ by Aryan Jain  
Powered by: **Streamlit**, **Plotly**, **Pandas**, and optionally **Power BI**(Upto Personal Preference)