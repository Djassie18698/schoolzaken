import evenorodd as eo 
import pytest

def test_evenorodd1(getal=2):
 assert eo.evenorodd(getal) == "Getal is even"

def test_evenorodd2(getal=3):
 assert eo.evenorodd(getal) == "Getal is oneven"

def test_evenorodd3(getal="a"):
 assert eo.evenorodd(getal) == "geen getal"
