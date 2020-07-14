from multiprocessing import Process, Queue
import time

def download(q):
	images = ['a.jpg', 'b.jpg','c.jpg']
	for img in images:
		print("正在下载......", img)
		time.sleep(1)
		q.put(img)


def getfile(q):
	while True:
		try:
			file = q.get(timeout=3)
			print("保存成功.....", file)
		except:
			print("保存完毕")
			break

if __name__ == '__main__':
	q = Queue(5)
	p1 = Process(target = download, args=(q,))
	p2 = Process(target = getfile, args=(q,))
	print("OK")
	p1.start()
	p1.join()
	p2.start()
	p2.join()



if(phead == )
class Solution:
	def copyRandomList(self, head):
		if not head:
			return None
			new_head = Node(head.val)
			cur_node = head 
			copy_node = new_node
			record = {head:new_head}
			cur_node = cur_node.next

			while cur_node:
				tmp = Node (cur_node.val)
				record[cur_node] = tmp
				
















































