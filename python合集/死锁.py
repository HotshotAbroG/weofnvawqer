import time
import threading

number = 20
lock1 = threading.Lock()
lock2 = threading.Lock()
# 死锁： 多个线程分别站有一部分资源，并且同时等待对方的资源释放，就会构成死锁 

class Mythread1(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.name = "lagrange"

    def run(self):
        if lock1.acquire():
            print(self.name, "acquire lock1")
            time.sleep(0.5)

            if lock2.acquire():
                print(self.name, "acquire lock2")
                lock2.release()
            else:
                print("lock2 have been used!")
            lock1.release()


class Mythread2(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.name = "nyquist"

    def run(self):
        if lock2.acquire():
            print(self.name, "acquire lock2")
            time.sleep(0.5)
            if lock1.acquire():
                print(self.name, "acquire lock1")
                lock1.release()
            lock2.release()


if __name__ == '__main__':
    my1 = Mythread1()
    my2 = Mythread2()
    my1.start()
    my2.start()
    # my1  my2互相请求，构成死锁
