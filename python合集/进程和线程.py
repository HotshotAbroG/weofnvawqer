from multiprocessing import Process
import time
import os 

number = 0

def t1(name=None):
	global number
	while True:
		time.sleep(1)
		number += 1
		print("target I ........", os.getpid())
		print(str(number), "----->", name)
def t2(name=None):
	global number
	while True:
		time.sleep(1)
		number -= 1
		print("target II ........", os.getpid())
		print(str(number), "----->", name)


if __name__ == '__main__':
	
	p1 = Process(target=t1, args='2')
	p2 = Process(target=t2, args='1')
	p1.start()
	p2.start()
	while True:
		number += 1
		time.sleep(1)
		print(number)
		if number == 5:
			p1.terminate()
		if number == 10:
			p2.terminate()
			break