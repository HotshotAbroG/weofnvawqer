from multiprocessing import Process, Queue
import time
import threading

number = 20
lock = threading.Lock()


def run():
    global number, lock

    while number > 0:
        lock.acquire()
        number -= 1
        print(threading.current_thread().name, "number value is ", str(number))
        time.sleep(1)
        lock.release()


def run1():
    global number, lock

    while number > 0:
        lock.acquire()
        number -= 1
        print(threading.current_thread().name, "number value is ", str(number))
        time.sleep(1)
        lock.release()


if __name__ == '__main__':

    # 默认带锁 GIL 全局解释器锁
    # 直接开启2个线程会有问题， 得自己加锁
    t1 = threading.Thread(target=run1, name='lagrange')
    t2 = threading.Thread(target=run, name='nyquist')
    t1.start()
    t2.start()
