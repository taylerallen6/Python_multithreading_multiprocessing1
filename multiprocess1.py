import multiprocessing as mp
import time

def func(num):
	time.sleep(.2)
	print(num)

if __name__ == '__main__':
	for i in range(5):
		p = mp.Process(target=func, args=(i,))
		p.start()