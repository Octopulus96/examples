from work_with_lists import coppy_aray, array_search, invert_array
from bruteforce_practice import is_simple_number, factorize_number
from cyclc_shift import cyclic_shift_first, cyclic_shift_last
from rever_str import rever_str

#work_with_lists
def test_coppy_array(m=[1, 2, 3, 4, 5]):
    assert coppy_aray(m) == m.copy()

def test_coppy_array(m=[1, 2, 3, 4, 5]):
    assert coppy_aray(m) == m


def test_coppy_array(m=[1, 2, 3, 4, 5]):
    coppy_m = coppy_aray(m)
    assert id(m) != id(coppy_m)


def test_array_search(m=[1, 2, 3, 4 ,5], l=5, x=8):
    assert array_search(m,l,x) == -1


def test_array_search(m=[1, 2, 3, 4, 5], l=20, x=5):
    assert array_search(m,l,x) == 4


def test_array_search(m=[1, 2, 3, 4, 5], l=5, x=4):
    assert array_search(m,l,x) == 3


def test_array_search(m=[1, 2, 3, 4, 5], l=20, x=8):
    assert array_search(m,l,x) == 0


def test_invert_search(m=[1, 2, 3, 4, 5], l=5):
    assert invert_array(m, l) == [5, 4, 3, 2, 1]


def test_invert_search(m=[0, 0, 0, 0, 0, 10], l=8):
    assert invert_array(m, l) == [10, 0, 0, 0, 0, 0]


def test_invert_search(m=[0, 0, 0, 0, 0, 10], l=9):
    assert invert_array(m, l) == 0


#bruteforce_practice
def test_simple_number(x=11):
    assert is_simple_number(x) == True


def test_simple_number(x=10):
    assert is_simple_number(x) == False


def test_factorize_number(x=1):
    b = factorize_number(x)
    assert b == None


def test_factorize_number(x=0):
    b = factorize_number(x)
    assert b == None


def test_factorize_number(x=10):
    b = factorize_number(x)
    assert b == [2, 5]


#cyclic_shift
def test_cycle_shift_first(m=[1, 2, 3, 4, 5]):
    x = cyclic_shift_first(m)
    assert x == [2, 3, 4, 5, 1]


def test_cyclic_shift_last(m=[1, 2, 3, 4, 5]):
    x = cyclic_shift_last(m)
    assert x == [5, 1, 2, 3, 4]


#rever_str
def test_rever_str(a='cats love python'):
    x = rever_str(a)
    assert x == 'nohtyp evol stac'