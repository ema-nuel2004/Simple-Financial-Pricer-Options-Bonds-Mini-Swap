import math
from pricer import bs_price, bond_pv

def test_bs_smoke():
    p = bs_price(100, 100, 0.03, 0.0, 0.2, 1.0, 'call')
    assert p > 0

def test_bond_smoke():
    p = bond_pv(1000, 0.05, 0.04, 5, 2)
    assert p > 0
