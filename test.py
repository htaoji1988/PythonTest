class Student(object):

    @property
    def birth(self):
        return self.birth

    @birth.setter
    def birth(self, value):
        self.birth = value

    @property
    def age(self):
        return 2014 - self.birth