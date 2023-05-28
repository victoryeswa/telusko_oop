#method overloading and method overiding in python

class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    s = 0
    def sum(self, a=None, b=None, c=None):

        if a!=None and b!=None and c!=None:
            s = a + b + c
        elif a!=None and b!=None:
            s = a + b
        else:
            s = a

        return s
    
s1 = Student(58, 59)

s1 = Student(58, 69)

print(s1.sum(5, 7, 9))

