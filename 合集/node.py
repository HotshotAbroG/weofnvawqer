class listNode:
    def __init__(self, x):
        
        self.val = x
        self.next = None

    @staticmethod
    def build_listNode(arr):
        
        dummy_head = listNode(0)
        head = dummy_head
        for value in arr:
            tmp_node = listNode(value)
            dummy_head.next = tmp_node
            dummy_head = dummy_head.next
        return head.next
    
    def show(root):
        dummy_head = root
        while (dummy_head):
            print(dummy_head.val, end='  ')
            dummy_head = dummy_head.next
        print()
    
        
