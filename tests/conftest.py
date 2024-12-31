import os
import pytest
from src.convert import G01toDAT

@pytest.fixture
def g2d():
    dir = os.getcwd()
    name_g01 = "TujungaWash"
    name_dat = "laces"
    return G01toDAT(dir, name_g01, name_dat)