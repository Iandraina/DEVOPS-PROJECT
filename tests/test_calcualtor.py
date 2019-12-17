# from calculator import add
# from calculator import subtract
# from calculator import multiply
# from calculator import divide

#test addition
def add(x, y):
       return x + y
def testAdd() : 
    assert (add(2,2)) == 4

#test substraction
def subtract(x, y):
       return x - y
def testSub() : 
    assert (subtract(116,46)) == 70
    assert (subtract(11,6)) == 5

#test multiplication
def multiply(x, y):
       return x * y
def testMul() : 
    assert (multiply(2,12)) == 24
    assert (multiply(15,4)) == 60

#test division
def divide(x, y):
       return x / y
def testDiv() : 
    assert (divide(12,2)) ==6