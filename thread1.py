import threading
import time

def func(num):
	time.sleep(.2)
	print(num)

if __name__ == '__main__':
	threads = []

	for i in range(5):
		t = threading.Thread(target=func, args=(i,))
		t.daemon = True
		threads.append(t)
		t.start()

	for t in threads:
		t.join()

	print("done")