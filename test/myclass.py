__metaclass__ = type


class Tst():
    name = 'tst'
    data = 'this is data'

    def NormalMethod(self):
        print 'hello world!'

    @classmethod
    def ClassMethod(cls, name):
        print cls.data, name

    @staticmethod
    def StaticMethod(name):
        print name


b = Tst
print b.normalMethod()
