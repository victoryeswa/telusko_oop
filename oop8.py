#Inheritance in python
class A:
    def feature(self):
        print('Feature 1 working')

    def feature2(self):
        print('Feature 2 working')

class B(A): #has feature 1, 2,3, 4
    def feature3(self):
        print('Feature 3 working')

    def feature4(self):
        print('Feature 4 working')

class C(B):
    def feature5(self):
        print('Feature 5 working')
a1 = A()

a1.feature()
a1.feature2()

