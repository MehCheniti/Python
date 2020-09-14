#!/usr/bin/env python

from array0 import Array

def testPrint():
    assert str(Array((1,), True)) == "Array has 1 value(s) of type: boolean."

def testAdd():
    assert add(Array((3,), [5, 4, 3]), 10) == [5, 4, 3, 10]

def testAdd1():
    assert add(Array((4,), [5, 4, 3, 11]), 25) == [5, 4, 3, 11, 25]

def testSub():
    assert sub(Array((5,), [5, 4, 3, 10, 8]), 3) == [5, 4, 10, 8]

def testSub1():
    assert sub(Array((2,), [8, 10]), 8) == [10]

def testMul():
    assert mul(Array((3,), [8, 8, 5]), 10) == [80, 80, 50]

def testMul1():
    assert mul(Array((4,), [5, 2, 42, 50]), 0) == [0, 0, 0, 0]

def testEq():
    assert eq(Array((4,), [5, 5, 4, 5]), Array((4,), [5, 2, 4, 5])) == False

def testEq1():
    assert eq(Array((4,), [5, 2, 4, 5]), Array((4,), [5, 2, 4, 5])) == True

def testIsEq():
    assert is_equal(Array((4,), [5, 5, 4, 5]), Array((4,), [5, 2, 4, 5])) == [True, False, True, True]

def testIsEq1():
    assert is_eq(Array((4,), [5, 2, 4, 5]), 3) == [False, False, False, False]

def testMean():
    assert mean(Array((3,), [8, 8, 5])) == 7.0

def testMean1():
    assert mean(Array((1,), [5])) == 5.0

def testVariance():
    assert variance(Array((5,), [1, 2, 3, 4, 5])) == 2.0

def testVariance1():
    assert variance(Array((5,), [7, 7, 8, 8, 3])) == 3.0

def testMin():
    assert min_element(Array((5,), [7, 0, 8, 8, 3])) == 0.0

def testMin1():
    assert min_element(Array((4,), [7, 12, 8, 8])) == 7.0

# testPrint()
# testAdd()
# testAdd1()
# testSub()
# testSub1()
# testMul()
# testMul1()
# testEq()
# testEq1()
# testIsEq()
# testIsEq1()
# testMean()
# testMean1()
# testVariance()
# testVariance1()
# testMin()
# testMin1()
