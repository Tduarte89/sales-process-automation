# 📊 Sales Process Automation (Python RPA & Data Analysis)

🌍 **Language:** English | [Português](README.pt-br.md)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![PyAutoGUI](https://img.shields.io/badge/RPA-PyAutoGUI-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

A practical **Robotic Process Automation (RPA)** and **Data Analytics** project built with Python. It automates the daily operational workflow of fetching daily sales data from cloud storage, calculating key business indicators (KPIs), and dispatching an executive summary report via email.

---

## 🎯 Business Context

In recurring sales operations, analysts often spend valuable time performing manual, repetitive tasks:
1. Accessing cloud file drives (Google Drive);
2. Downloading the latest sales records;
3. Consolidating total revenue and product sales volume;
4. Drafting and sending email reports to executive leadership.

This manual routine is repetitive and prone to human errors. This project automates the entire end-to-end cycle in seconds with precision and reliability.

---

## 🛠️ Tech Stack & Libraries

- **[Python](https://www.python.org/):** Core programming language.
- **[Pandas](https://pandas.pydata.org/):** Data extraction, manipulation, and KPI aggregations.
- **[OpenPyXL](https://openpyxl.readthedocs.io/):** Excel (`.xlsx`) file parsing engine.
- **[PyAutoGUI](https://pyautogui.readthedocs.io/):** Graphical user interface (GUI) automation for mouse and keyboard control.
- **[Pyperclip](https://pypi.org/project/pyperclip/):** Cross-platform clipboard management for special character rendering.
- **[python-dotenv](https://github.com/theskumar/python-dotenv):** Secure management of environment variables and secrets.

---

## 📁 Repository Structure

```text
sales-process-automation/
│
├── data/
│   └── Vendas - Dez.xlsx      # Sample sales dataset
│
├── First Automation.ipynb     # Interactive Jupyter Notebook step-by-step walkthrough
├── sales_automation.py        # Modular, production-ready Python script
├── requirements.txt           # Project dependencies
├── .env.example               # Template for environment variables and secrets
├── .gitignore                 # Files and cache directories excluded from Git
├── README.md                  # Main English documentation
└── README.pt-br.md            # Portuguese documentation
```

---

## ⚙️ Quickstart & Execution

### Prerequisites
- Python 3.10 or higher.
- Google Chrome browser.

### 1. Clone the repository
```bash
git clone https://github.com/YOUR-USERNAME/sales-process-automation.git
cd sales-process-automation
```

### 2. Set up a virtual environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables (Security Protocol)
Copy `.env.example` to create your private `.env` file:
```bash
copy .env.example .env
```
Open `.env` and fill in your target recipient email, drive URL, and sender name. *(The `.env` file is excluded from Git via `.gitignore` to guarantee security).*

### 5. Run the automation
```bash
python sales_automation.py
```

---

## 🔍 Consolidated Metrics

When executed against the sales dataset, the system automatically computes:
- **Total Revenue:** Sum of the `Valor Final` column (e.g., `$2,917,311.00`).
- **Units Sold:** Sum of the `Quantidade` column (e.g., `15,227 units`).

---

## 💡 Engineering Insights & Best Practices

> [!IMPORTANT]
> **Security Protocol (Twelve-Factor App):**  
> Personal emails, drive credentials, and specific system paths are strictly decoupled from source code and managed via environment variables (`.env`). The real `.env` file is explicitly ignored in `.gitignore`, preventing accidental leaks of private corporate data on public repositories.

> [!NOTE]
> **Screen Coordinate Calibration:**  
> Because PyAutoGUI drives mouse clicks via absolute pixel coordinates, screen resolution and browser positioning affect coordinates. A built-in calibration utility (`calibrate_coordinates()`) is provided within `sales_automation.py` to easily recalibrate coordinate targets for any monitor setup.

> [!TIP]
> **Architecture Roadmap (Next Iterations):**  
> - Integrate direct SMTP / Gmail API / SendGrid integration to handle headless background email delivery;
> - Leverage Google Drive API for direct file streaming without GUI dependencies;
> - Automate recurring schedules via Windows Task Scheduler or cloud-based serverless functions.

---

## 👤 Author

Developed by **Thiago A. Duarte**.  
- LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/thiago-duarte-32a64839)  
- GitHub: [Your GitHub Profile](https://github.com/Tduarte89)  
