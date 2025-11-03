from pricer import bs_price,bond_pv,mini_swap_pv
def test_bs():
    assert bs_price(100,100,0.03,0.0,0.2,1.0,'call')>0
def test_bond():
    assert bond_pv(1000,0.05,0.04,5,2)>0
def test_swap():
    pv=mini_swap_pv(1_000_000,0.04,0.035,5,2,'fixed'); assert abs(pv)<30000
