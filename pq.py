from multiprocessing import Process,Queue


def f(q,n):
	q.put([n,'hello'])
	
	#print(q.get())
if __name__ == '__main__':
	q = Queue()
	q.put('ddd')
	for i in range(9):
		p = Process(target=f, args=(q,i))
		p.start()
		print(q.get())
	#进程间的数据交换  共享内存