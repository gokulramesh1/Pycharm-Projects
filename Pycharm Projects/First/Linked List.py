
class Node:
    def __init__(self, data, nxt):
        self.data = data
        self.next = nxt


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def set_head(self, head):
        self.head = head

    def append(self, node):
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def insert(self, index, node):
        current = self.head
        i = 0
        if index == 0:
            node.next = current
            self.head = node
        else:
            while i < index-1:
                current = current.next
                i += 1
            before = current
            after = current.next
            before.next = node
            node.next = after

    def delete(self, index):
        current = self.head
        i = 0
        while i < index-1:
            current = current.next
            i += 1
        before = current
        node = current.next
        after = node.next.next
        before.next = after

    def size(self):
        current = self.head
        count = 1
        while current.next:
            current = current.next
            count += 1
        return count

    def reverse(self):
        current = self.head
        nxt = current.next
        head = nxt.next
        current.next = None
        while head.next:
            nxt.next = current
            current = nxt
            nxt = head
            head = head.next
        nxt.next = current
        head.next = nxt
        self.head = head

    def __str__(self):
        s = '['
        curr = self.head
        while curr:
            s += str(curr.data) + ', '
            curr = curr.next
        s = s[:-2]
        s += ']'
        return s

    def show(self):
        current = self.head
        while current.next:
            print(current.data, end=' ')
            current = current.next
        print(current.data)

ashwinsList = LinkedList()
ashwinsList.append(Node(3, None))
print(ashwinsList)

myList = LinkedList()
myList.append(Node(1, None))
myList.append(Node(2, None))
myList.append(Node(3, None))
myList.append(Node(4, None))
myList.append(Node(5, None))
myList.append(Node(6, None))
myList.append(Node(7, None))
myList.append(Node(8, None))
myList.show()
myList.insert(5, Node(12, None))
myList.show()
myList.delete(5)
myList.show()
myList.reverse()
myList.show()







































































































































































































































































