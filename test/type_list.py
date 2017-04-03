class CountList:
    def __str__(self):
        return "hello world!"

    def __init__(self, *args):
        super(CountList, self).__init__(*args)
        self.counter = 0

    def __getitem__(self, index):
        self.counter += 1
        return super(CountList, self).__getitem__(index)
