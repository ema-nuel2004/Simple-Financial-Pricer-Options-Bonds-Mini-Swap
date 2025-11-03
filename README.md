# Simple Pricer (Options, Bonds, Mini-Swap)

Small portfolio project: a **simple pricer** for
- European options (Black–Scholes, call/put; with dividend yield `q`),
- Coupon bonds (PV, simple convention),
- A tiny **fixed vs fixed** deterministic swap (demo only).

**Colab:** click to open a ready-to-run notebook  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TU_USUARIO/TU_REPO/blob/main/examples/colab_simple_pricer.ipynb)

> If the notebook is opened without the repository cloned (typical when coming from the badge), it will ask you to upload `pricer.py` or will try to clone the repo automatically if you provide the GitHub URL.

## Quickstart (Local)

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m pricer option --type call --S 100 --K 100 --r 0.03 --q 0.0 --sigma 0.2 --T 1.0
python -m pricer bond --face 1000 --coupon 0.05 --y 0.04 --n 5 --freq 2
python -m pricer swap --notional 1000000 --fixed_rate 0.04 --float_rate 0.035 --years 5 --freq 2 --payer fixed
```

## Structure
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

## Next steps / Ideas
- Greeks (Delta, Gamma, Vega, Theta, Rho) and their CLI flags.
- Implied volatility solver and smile.
- Term structure discounting / yield curves.
- Monte Carlo for exotic payoffs.
- A tiny Streamlit UI (`streamlit_app.py`).

---

**Author:** Emanuel Armas
