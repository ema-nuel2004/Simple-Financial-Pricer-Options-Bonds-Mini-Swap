"""
Simple Pricer — Colab + Testing Version
European options (Black–Scholes), coupon bonds, and a tiny deterministic swap.
Signed by: Emanuel Armas
"""
from __future__ import annotations
import math, argparse
from typing import Literal
from scipy.stats import norm

def _d1(S,K,r,q,sigma,T):
    return (math.log(S/K)+(r-q+0.5*sigma**2)*T)/(sigma*math.sqrt(T))
def _d2(S,K,r,q,sigma,T): return _d1(S,K,r,q,sigma,T)-sigma*math.sqrt(T)

def bs_price(S,K,r,q,sigma,T,kind:Literal["call","put"]):
    d1=_d1(S,K,r,q,sigma,T); d2=d1-sigma*math.sqrt(T)
    if kind=="call":
        return S*math.exp(-q*T)*norm.cdf(d1)-K*math.exp(-r*T)*norm.cdf(d2)
    elif kind=="put":
        return K*math.exp(-r*T)*norm.cdf(-d2)-S*math.exp(-q*T)*norm.cdf(-d1)
    else: raise ValueError("kind must be call or put")

def bond_pv(face,coupon,y,n,freq=1):
    periods=int(n*freq); c=face*coupon/freq
    df=[1/(1+y/freq)**t for t in range(1,periods+1)]
    return sum(c*d for d in df)+face*df[-1]

def mini_swap_pv(notional,fixed_rate,float_rate,years,freq,payer:Literal["fixed","float"]):
    periods=years*freq
    df=[1/(1+float_rate/freq)**t for t in range(1,periods+1)]
    fixed_leg=sum((notional*fixed_rate/freq)*d for d in df)+notional*df[-1]
    float_leg=sum((notional*float_rate/freq)*d for d in df)+notional*df[-1]
    return (float_leg-fixed_leg) if payer=="fixed" else (fixed_leg-float_leg)

def _cli(argv=None):
    p=argparse.ArgumentParser(prog="pricer",description="Simple pricer CLI")
    sub=p.add_subparsers(dest="cmd",required=True)
    p_opt=sub.add_parser("option"); p_opt.add_argument("--type",choices=["call","put"],required=True)
    for a in ["S","K","r","q","sigma","T"]: p_opt.add_argument(f"--{a}",type=float,required=(a!="q"))
    p_b=sub.add_parser("bond"); [p_b.add_argument(f"--{a}",type=float,required=True) for a in ["face","coupon","y"]]
    p_b.add_argument("--n",type=int,required=True); p_b.add_argument("--freq",type=int,default=2)
    p_s=sub.add_parser("swap"); [p_s.add_argument(f"--{a}",type=float,required=True) for a in ["notional","fixed_rate","float_rate"]]
    p_s.add_argument("--years",type=int,required=True); p_s.add_argument("--freq",type=int,default=2)
    p_s.add_argument("--payer",choices=["fixed","float"],required=True)
    args=p.parse_args(argv)
    if args.cmd=="option": print("BS",args.type,"=",bs_price(args.S,args.K,args.r,args.q,args.sigma,args.T,args.type))
    elif args.cmd=="bond": print("Bond PV =",bond_pv(args.face,args.coupon,args.y,args.n,args.freq))
    elif args.cmd=="swap": print("Swap PV =",mini_swap_pv(args.notional,args.fixed_rate,args.float_rate,args.years,args.freq,args.payer))

if __name__=="__main__":
    import sys
    joined=" ".join(sys.argv).lower()
    if "ipykernel" in joined or "colab" in joined: pass
    else: _cli(sys.argv[1:])
