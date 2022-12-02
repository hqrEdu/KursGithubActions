###########
# Funkcje #
###########

def inc(x):
    return x + 1


def plus(x, y):
    return x + y


def minus(x, y):
    return x - y


def times(x, y):
    return x * y


def div(x, y):
    return x / y


def power(x, y):
    return x**y

def nstr(x):
    return str(x)


###########
#  Testy  #
###########

def test_inc():
    assert inc(3) == 4


def test_plus():
    assert plus(3, 2) == 5


def test_minus():
    assert minus(3, 2) == 1


def test_times():
    assert times(2, 2) == 4


def test_div():
    assert div(2, 2) == 1


def test_power():
    assert power(2, 2) == 4

