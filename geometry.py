'''
Module geometry.py
'''
# variables
pi = 3.14159265359
phi = 1.6180

# function that calculates the area
def area(obj):
    if type(obj) == square:
        return obj.a**2



# definitions of some classes
class square(object):
    def __init__(self,a):
        self.a = a

class triangle(object):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c