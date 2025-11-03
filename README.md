# 💹 Simple Financial Pricer — Options, Bonds & Mini-Swap

A compact Python project that prices **basic financial instruments** — European options (Black–Scholes), coupon bonds, and a simple deterministic swap.  
Built for educational and portfolio purposes to demonstrate understanding of **quantitative finance and market valuation models**.  
Includes CLI, unit tests, and a ready-to-run **Google Colab** notebook.

---

## 🚀 Try it on Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/emanuelarmas/simple-pricer/blob/main/examples/colab_simple_pricer.ipynb)

> If you open it directly from this badge, the notebook will install dependencies and ask you to upload `pricer.py` if the file is not found.  
> No setup required — everything runs in Colab in a few seconds.

---

## 📘 Quickstart (Local)

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m pricer option --type call --S 100 --K 100 --r 0.03 --q 0.0 --sigma 0.2 --T 1.0
python -m pricer bond --face 1000 --coupon 0.05 --y 0.04 --n 5 --freq 2
python -m pricer swap --notional 1000000 --fixed_rate 0.04 --float_rate 0.035 --years 5 --freq 2 --payer fixed
```

---

## 🧮 What the Pricer Analyzes

### 1️⃣ **European Options (Calls & Puts)**
Computes the **theoretical fair value** using the **Black–Scholes–Merton model**, considering:
- Spot price (`S`)
- Strike price (`K`)
- Risk-free rate (`r`)
- Dividend yield (`q`)
- Volatility (`σ`)
- Time to maturity (`T`)

🎯 Output → the option’s **fair market value**, showing your grasp of how risk, time, and volatility affect derivatives.

---

### 2️⃣ **Coupon Bonds**
Calculates the **present value (PV)** of a coupon-paying bond using:
- Nominal value (`face`)
- Coupon rate (`coupon`)
- Yield to maturity (`y`)
- Years to maturity (`n`)
- Payment frequency (`freq`)

🎯 Output → the **fair price of the bond**, discounted at the yield curve.

---

### 3️⃣ **Mini Swap (Fixed vs Fixed, Deterministic)**
Computes both legs of a fixed-vs-fixed swap and returns the **net PV** from either perspective (`payer = fixed` or `float`).  
Ideal to illustrate **discounting**, **notional exposure**, and **interest rate structure**.

---

## 📂 Project Structure

```
simple-pricer/
├─ pricer.py
├─ requirements.txt
├─ README.md
├─ LICENSE
├─ examples/
│  ├─ simple_pricer_demo.ipynb
│  └─ colab_simple_pricer.ipynb
└─ tests/
   └─ test_pricer.py
```

---

## 🧠 Next Improvements
- Add **Greeks** (Delta, Gamma, Vega, Theta, Rho).
- Implement **implied volatility** solver and smile.
- Integrate **term structure** discounting curves.
- Add **Monte Carlo** pricing for exotic options.
- Build a **Streamlit** web app (`streamlit_app.py`).

---

## ✍️ Author
**Emanuel Armas**  
AI Developer & Quant Enthusiast  
Licensed under the MIT License
