import threading
import time

def func(lock, num):
	global total
	time.sleep(.2)

	lock.acquire()
	total += num
	lock.release()

	print(total)

if __name__ == '__main__':
	threads = []
	lock = threading.Lock()
	total = 0

	for i in range(5):
		t = threading.Thread(target=func, args=(lock, i))
		t.daemon = True
		threads.append(t)
		t.start()

	for t in threads:
		t.join()

	print("done")