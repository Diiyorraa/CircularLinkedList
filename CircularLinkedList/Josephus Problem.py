class Node:
    def __init__(self, data):
        self.data= data
        self.next = None
class CCL:
    def __init__(self):
        self.head = None
    def remove_node(self, node):
        if self.head == node :
            cur= self.head
            while cur.next != self.head:
                cur= cur.next
            if self.head == self.head.next:
                self.head = None
            else:
                cur.next = self.head.next
                self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur == node:
                    prev.next = cur.next
                    cur = cur.next

    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        return count
    def Josephus(self,  sword):
        cur = self.head
        length  = len(self)
        while length> 1:
            count =1
            while count != sword:
                cur= cur.next
                count +=1
            print("KILL: " + str(cur.data))
            self.remove_node(cur)
            cur = cur.next
            length-=1

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur= cur.next
            cur.next= new_node
            new_node.next= self.head
    def print(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

CCL1 = CCL()
CCL1.append(1)
CCL1.append(2)
CCL1.append(3)
CCL1.append(4)
CCL1.append(5)
CCL1.append(6)
CCL1.Josephus(2)
CCL1.print()



