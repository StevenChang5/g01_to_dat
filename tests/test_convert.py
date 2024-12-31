import os
import pytest
from src.convert import G01toDAT

@pytest.mark.usefixtures("g2d")
class TestConvert():
    def test_Init(self, g2d):
        assert g2d.dir == os.getcwd()
        assert g2d.name_g01 == "TujungaWash"
        assert g2d.name_dat == "laces"
        assert g2d.g01 == None

    def test_OpenG01(self, g2d):
        g2d.open_g01()
        assert g2d.g01.read(4) == 'Geom'

    def test_ReadG01(self, g2d):
        g2d.open_g01()
        g2d.read_g01()
        assert True
    def test_WriteDat(self, g2d):
        g2d.open_g01()
        g2d.read_g01()
        g2d.write_dat()
        assert False