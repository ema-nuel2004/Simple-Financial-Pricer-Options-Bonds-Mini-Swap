"""
Simple Pricer: European options (Black–Scholes), coupon bonds and a tiny deterministic swap.
Signed by: Emanuel Armas
"""
from __future__ import annotations

import math
import argparse
from typing import Literal

try:
    from scipy.stats import norm
except Exception as e:
    raise SystemExit("Please install dependencies: `pip install -r requirements.txt`")

# ---------- European options: Black–Scholes ----------
def _d1(S: float, K: float, r: float, q: float, sigma: float, T: float) -> float:
    if S <= 0 or K <= 0 or sigma <= 0 or T <= 0:
        raise ValueError("Invalid parameters for Black–Scholes.")
    return (math.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))

def _d2(S: float, K: float, r: float, q: float, sigma: float, T: float) -> float:
    return _d1(S, K, r, q, sigma, T) - sigma * math.sqrt(T)

def bs_price(S: float, K: float, r: float, q: float, sigma: float, T: float, kind: Literal["call", "put"]) -> float:
    d1 = _d1(S, K, r, q, sigma, T)
    d2 = d1 - sigma * math.sqrt(T)
    if kind == "call":
        return S * math.exp(-q * T) * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    elif kind == "put":
        return K * math.exp(-r * T) * norm.cdf(-d2) - S * math.exp(-q * T) * norm.cdf(-d1)
    else:
        raise ValueError("kind must be 'call' or 'put'")

# ---------- Coupon bond PV (simple convention) ----------
def bond_pv(face: float, coupon: float, y: float, n: int, freq: int = 1) -> float:
    if freq not in (1, 2, 4, 12):
        raise ValueError("freq must be 1, 2, 4 or 12")
    periods = int(n * freq)
    c = face * coupon / freq
    df = [(1 / (1 + y / freq) ** t) for t in range(1, periods + 1)]
    pv_coupons = sum(c * d for d in df)
    pv_face = face * df[-1]
    return pv_coupons + pv_face

# ---------- Tiny deterministic fixed-vs-fixed swap (demo) ----------
def mini_swap_pv(notional: float, fixed_rate: float, float_rate: float, years: int, freq: int, payer: Literal["fixed", "float"]) -> float:
    periods = years * freq
    df = [(1 / (1 + float_rate / freq) ** t) for t in range(1, periods + 1)]
    fixed_leg = sum((notional * fixed_rate / freq) * d for d in df) + notional * df[-1]
    float_leg = sum((notional * float_rate / freq) * d for d in df) + notional * df[-1]
    if payer == "fixed":
        return float_leg - fixed_leg
    elif payer == "float":
        return fixed_leg - float_leg
    else:
        raise ValueError("payer must be 'fixed' or 'float'")

# ---------- CLI ----------
def _cli(argv=None):
    p = argparse.ArgumentParser(prog="pricer", description="Simple pricer (BS options, bond PV, mini-swap).")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_opt = sub.add_parser("option", help="Black–Scholes for European options")
    p_opt.add_argument("--type", choices=["call", "put"], required=True)
    p_opt.add_argument("--S", type=float, required=True, help="Spot")
    p_opt.add_argument("--K", type=float, required=True, help="Strike")
    p_opt.add_argument("--r", type=float, required=True, help="Risk-free")
    p_opt.add_argument("--q", type=float, default=0.0, help="Dividend yield")
    p_opt.add_argument("--sigma", type=float, required=True, help="Volatility")
    p_opt.add_argument("--T", type=float, required=True, help="Time in years")

    p_bond = sub.add_parser("bond", help="Coupon bond PV")
    p_bond.add_argument("--face", type=float, required=True)
    p_bond.add_argument("--coupon", type=float, required=True)
    p_bond.add_argument("--y", type=float, required=True, help="YTM")
    p_bond.add_argument("--n", type=int, required=True, help="Years to maturity")
    p_bond.add_argument("--freq", type=int, default=2)

    p_swap = sub.add_parser("swap", help="Tiny fixed-vs-fixed deterministic swap (demo)")
    p_swap.add_argument("--notional", type=float, required=True)
    p_swap.add_argument("--fixed_rate", type=float, required=True)
    p_swap.add_argument("--float_rate", type=float, required=True)
    p_swap.add_argument("--years", type=int, required=True)
    p_swap.add_argument("--freq", type=int, default=2)
    p_swap.add_argument("--payer", choices=["fixed", "float"], required=True)

    args = p.parse_args(argv)

    if args.cmd == "option":
        price = bs_price(args.S, args.K, args.r, args.q, args.sigma, args.T, args.type)
        print(f"BS {args.type} price = {price:.6f}")
    elif args.cmd == "bond":
        price = bond_pv(args.face, args.coupon, args.y, args.n, args.freq)
        print(f"Bond PV = {price:.6f}")
    elif args.cmd == "swap":
        pv = mini_swap_pv(args.notional, args.fixed_rate, args.float_rate, args.years, args.freq, args.payer)
        print(f"Swap PV (payer={args.payer}) = {pv:.6f}")

if __name__ == "__main__":
    import sys
    # Avoid auto-argparse when executed inside ipykernel/colab
    joined = " ".join(sys.argv).lower()
    if ("ipykernel" in joined) or ("colab" in joined):
        pass
    else:
        _cli(sys.argv[1:])
