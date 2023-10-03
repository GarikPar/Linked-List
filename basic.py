class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node
    
    def length(self):
        cur = self.head
        total = 0
        while cur.next!=None:
            total+=1
            cur = cur.next
        return total
    
    def display(self):
        elements = []
        cur = self.head
        while cur.next!=None:
            cur = cur.next
            elements.append(cur.data)
        print(elements)
    
    def get(self, index):
        if index>=self.length():
            print("ERROR: Get Index out of range!")
            return None
        cur = self.head
        cur_indx = 0
        while True:
            cur = cur.next
            if cur_indx==index:
                return cur.data
            cur_indx += 1 

    def erase(self, index):
        if index>=self.length():
            print("ERROR: Get Index out of range!")
            return None
        cur = self.head
        print(cur.data)
        cur_indx = 0
        while True:
            last_node = cur
            cur = cur.next
            if cur_indx==index:
                last_node.next = cur.next
                return 
            cur_indx += 1 
    
    def maximum(self):
        elements = []
        cur = self.head
        while cur.next!=None:
            cur = cur.next
            elements.append(cur.data)
        print(max(elements))
    
    def post(self,item):
        cur = self.head
        while cur.next!=None:
            if item==cur.data:
                return f"{item} is in list"
            else:
                cur = cur.next
        return f"{item} is not in list"
    
    def update_in_value(self,item,index):
        if index>=self.length():
            print("ERROR: Get Index out of range!")
            return None
        cur = self.head
        cur_indx = 0
        while cur.next!=None:
            cur = cur.next
            if cur_indx==index:
                cur.data = item
                return item
            cur_indx+=1


