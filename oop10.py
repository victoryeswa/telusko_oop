#Introduction to polymorphism in Python
#duck typing 

class Pycharm:

    def execyte(self):
        print('Compiling')
        print('Running')

class Myeditor:

    def code(self, ide):
        ide.execute()

class Laptop:

    def code(self):
        ide.execute()

ide = Pycharm

lap1 = Laptop()
lap1.code()