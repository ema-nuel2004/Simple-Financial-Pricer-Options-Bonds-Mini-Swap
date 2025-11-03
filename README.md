# Simple Financial Pricer — Colab & Tested Edition

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ema-nuel2004/Simple-Financial-Pricer-Options-Bonds-Mini-Swap/blob/main/examples/colab_full_test.ipynb)

Run everything directly in **Google Colab** — including automatic validation with `pytest`.

##Colab Quickstart

1. Open `examples/colab_full_test.ipynb` in Colab (or click the badge above).
2. The notebook will install dependencies and ask for `pricer.py` (upload it from this ZIP).
3. It will also run pricing examples and automatically execute `pytest` to verify everything works.

```python
!pytest -q  # runs basic smoke tests for options, bonds, and swaps
```

## Features
- **Black–Scholes** pricing for European options (call/put)
- **Coupon bond** PV calculator
- **Mini fixed-vs-fixed swap** demo valuation
- **Colab-safe CLI** and `pytest` validation

## Author
**Emanuel Armas**
