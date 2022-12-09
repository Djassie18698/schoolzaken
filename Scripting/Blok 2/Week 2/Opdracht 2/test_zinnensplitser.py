import Zinnensplitser as zp 
import pytest

def test_zinnensplitser1():
    assert zp.zinnensplitser("Dit is een zin. Dit is een tweede zin") == ['Dit is een zin', ' Dit is een tweede zin']

def test_zinnensplitser2():
    assert zp.zinnensplitser("Dit is een zin. Dit is een derde zin") == ['Dit is een zin', ' Dit is een derde zin']