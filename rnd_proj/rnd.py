import multiprocessing
import time

done = True

def add():
    while True:
        print (1)
        time.sleep(2)

def sud():
	num = 0
	while True:
		num += 1
		print num
		if num > 5:
			p1.shutdown()
		time.sleep(2)

if __name__ == '__main__':
	p1 = multiprocessing.Process(name='p1', target=add)
	p = multiprocessing.Process(name='p', target=sud)
	p1.start()
	p.start()