from threading import Thread
import time


class PrintSth(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(2)
        print("%s say hello" % self.name)


if __name__ == "__main__":
    t = PrintSth("ni hao a !")
    t.start()
