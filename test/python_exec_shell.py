import multiprocessing
import threading
import time


class Producer(threading.Thread):
    def __init__(self, queue):
        self.queue = queue
        super().__init__()

    def run(self):
        while True:
            # 这里写发现文件代码
            pass
            time.sleep(10)


def worker(queue):
    while True:
        task = queue.get()
        # 这里写处理文件代码
        pass
        time.sleep(10)


if __name__ == '__main__':
    CPU_CORES = 10
    queue = multiprocessing.Queue()
    producer = Producer(queue)
    producer.start()

    process_list = []

    for i in range(0, CPU_CORES):
        worker = multiprocessing.Process(target=worker, args=(queue,))

        process_list.append(worker)

    for worker in process_list:
        worker.start()

    for worker in process_list:
        worker.join()

    producer.join()
