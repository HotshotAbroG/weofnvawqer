import queue
class tree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    @staticmethod
    def build_tree(arr, index):
    
        if index >= len(arr):
            return
        head = None
        if arr[index] != -1014:
            head = tree(arr[index])
            head.left = tree.build_tree(arr, 2 * index + 1)
            head.right = tree.build_tree(arr, 2 * index + 2)
        return head
    
    @staticmethod
    def bfs(root):
        que = queue.Queue()
        que.put(root)
        res = []
        while (not que.empty()):
            tmp_list = []
            length = que.qsize()
            for i in range(length):
                tmp_node = que.get()
                tmp_list.append(tmp_node.val)
                if tmp_node.left:
                    que.put(tmp_node.left)
                if tmp_node.right:
                    que.put(tmp_node.right)
            res.append(tmp_list)
        for i in res:
            print(i)   
    