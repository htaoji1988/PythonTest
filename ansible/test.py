class MyTest:
    myname = 'peter'

    # add a instance attribute
    def __init__(self, name):
        self.name = name

    # class access class attribute
    def sayhello(self):
        print("say hello to %s" % MyTest.myname)

    # instance can access class attribute
    def sayhello_1(self):
        print("say hello to %s" % self.myname)

    # It's a snap! instance can access instance attribute
    def sayhello_2(self):
        print("say hello to %s" % self.name)

    # class can not access instance attribute!!!
    @classmethod
    def sayhello_3(cls):
        print("say hello to %s" % cls.myname)
        pass


if __name__ == '__main__':
    test = MyTest("abc")
    test.sayhello_3()
