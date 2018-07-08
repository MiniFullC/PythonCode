'''
python 多线程经典案例
使用队列的数据结构，生产者生产商品，消费者选取商品，且时间均不固定————摘自《python核心编程》
'''
from random import randint
from time import sleep
from queue import Queue
from threading import Thread

class ThreadFunc(Thread):
    def __init__(self, target, args, name):
        super().__init__(target=target, args=args, name=name)
        self.func = target
        self.args = args
        self.name = name

    def run(self):
        self.func(self.args[0], self.args[1])

def writeQ(queue):
    print("Producing object for Q...")
    queue.put("xxx", 1)
    print("size now", queue.qsize())

def readQ(queue):
    val = queue.get(1)
    print("consumed object from Q... size now", queue.qsize())

def writer(queue, loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1,3))

def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(2,5))

funcs = [writer, reader]

def main():
    loops = randint(2,5)
    q = Queue(32)

    thread = list()
    for i in range(2):
        t = ThreadFunc(target=funcs[i], args=(q, loops), name=funcs[i].__name__)
        thread.append(t)

    for i in range(2):
        thread[i].start()

    for i in range(2):
        thread[i].join()

    print("all DONE!")

if __name__=="__main__":
    main()
