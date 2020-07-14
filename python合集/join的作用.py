import threading
import time


def run(n):
    time.sleep(1)
    for i in range(n):
        time.sleep(1)
        print("current thread name is : ", threading.current_thread().name)


if __name__ == '__main__':
    thread_list = []
    start_time = time.time()
    for i in range(5):
        thread_list.append(threading.Thread(target=run, name=str(i), args=(3, )))

    for t in thread_list:
        t.start()

    for t in thread_list:
        t.join()
    # 加上之后，等所有线程执行完毕，主线程才结束
    print("all thread excuse finished! ", threading.current_thread().name)
    print("cost total time are : ", time.time()-start_time)
