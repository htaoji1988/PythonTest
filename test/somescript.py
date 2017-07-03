class Student(object):
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print('65666')

    def setage(self, age):
        self.age = age
        return str(self.age)

