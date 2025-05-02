# Kevin Beaghan 4/6/2025
# [COMS 1270 A] Week 12 Lab - Using pytest and unit tests to fix code for math operations

import pytest

from myMath import add
def test_add():
    assert add(1, 2) == 3
    assert add(-1, -1) == -2
    assert add(0, 0) == 0

from myMath import subtract
def test_subtract():
    assert subtract(1, 2) == -1
    assert subtract(-1, -1) == 0
    assert subtract(0, 0) == 0

from myMath import multiply
def test_multiply():
    assert multiply(1, 2) == 2
    assert multiply(-1, -1) == 1
    assert multiply(0, 0) == 0

from myMath import divide
def test_divide():
    assert divide(1, 2) == 0.5
    assert divide(2, 1) == 2
    assert divide(10, 0) == "Error: Cannot division by zero"
    assert divide(5, -1) == -5

from myMath import power
def test_power():
    assert power(1, 2) == 1
    assert power(2, 3) == 8
    assert power(0, 9) == 0
    assert power(4, 0.5) == 2
    assert power(4, -1) == 0.25

from myMath import factorial
def test_factorial():
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(-1) == "Error: Cannot n cannot be zero"

from myMath import is_prime
def test_is_prime():
    assert is_prime(1) == False
    assert is_prime(5) == True
    assert is_prime(10) == False
    assert is_prime(-1) == False

from myMath import sum_of_digits
def test_sum_of_digits():
    assert sum_of_digits(12) == 3
    assert sum_of_digits(100) == 1
    assert sum_of_digits(123) == 6

from myMath import gcd
def test_gcd():
    pass

from myMath import fib
def test_fib():
    pass

from myMath import lcm
def test_lcm():
    pass

from myMath import square_root
def test_square_root():
    pass

from myMath import abs_diff
def test_abs_diff():
    pass

from myMath import log
def test_log():
    pass

from myMath import mod
def test_mod():
    pass

from myMath import mean
def test_mean():
    pass

from myMath import median
def test_median():
    pass

from myMath import mode
def test_mode():
    pass

from myMath import celsius_to_fahrenheit
def test_celsius_to_fahrenheit():
    pass

from myMath import fahrenheit_to_celsius
def test_fahrenheit_to_celsius():
    pass

from myMath import inverse
def test_inverse():
    pass

from myMath import triangular_number
def test_triangular_number():
    pass