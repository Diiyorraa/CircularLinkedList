class Node:
    def __init__(self, data):
        self.data=data
        self.next= None
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
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
    def prepend(self, data):
        new_node= Node(data)
        cur= self.head
        new_node.next = self.head
        if not self.head:
            new_node.next=new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next= new_node
        self.head=new_node
    def remove(self, key_val):
        if self.head:
            if self.head.data == key_val:
                cur = self.head
                while cur.next!= self.head:
                    cur = cur.next
                if self.head == self.head.next:
                    self.head= None
                else:
                    cur.next = self.head.next
                    self.head = self.head.next
            else:
                cur = self.head
                prev_val = None
                while cur.next != self.head:
                    prev_val = cur
                    cur = cur.next
                    if cur.data == key_val:
                        prev_val.next = cur.next
                        cur = cur.next
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break


cirlist = CircularLinkedList()
cirlist.append(input("Please enter your name: "))
cirlist.append("A")
cirlist.append("b")
cirlist.prepend("name is")
cirlist.prepend("My")
cirlist.print_list()
cirlist.remove("b")
cirlist.print_list()