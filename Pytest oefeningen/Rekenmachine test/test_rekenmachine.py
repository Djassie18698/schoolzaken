import rekenmachine as rm 

def test_telop():
 assert rm.telop(3) == 4

def test_eraf():
 assert rm.eraf(3) == 2

def test_delen():
 assert rm.delen(6) == 3

def test_vermenigvuldigen():
 assert rm.vermenigvuldigen(3) == 6