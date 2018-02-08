from threading import Thread
import time


def PrintTime(times, contnet, seconds):
    n = 0
    for n in range(times):
        n += 1
        print("It's %s times %s!", (times, contnet))
        time.sleep(seconds)


work1 = Thread(target=PrintTime, args=(5, "aaa", 3))
work2 = Thread(target=PrintTime, args=(6, "aaa", 4))
work3 = Thread(target=PrintTime, args=(4, "aaa", 4))

work1.start()
work2.start()
work3.start()
