"""
#
File    :lotto_test.py
Created :21/10/2021
Author  : Eoin O'Mahony
"""


import pytest
from lotto_example import Lotto


def test_lotto():
    x = Lotto
    assert x.run_lotto(Lotto,  21) == "Passed"


def test_lotto_negative():
    x = Lotto
    assert x.run_lotto(Lotto, 9) == "Failed"
    print("Successful")

