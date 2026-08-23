class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    #Print method
    def __str__(self):
        return str(self.val)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        curr = self.head
        elements = []
        while curr:
            elements.append(str(curr.val))
            curr = curr.next
        print("<->".join(elements))

    # insert at beginning O(1)
    def insert_at_beginning(self, head, val):
        new_node = DoublyNode(val)
        head.prev = new_node
        new_node.next = head
        return new_node

    # insert at position O(n)
    def insert_at_position(self, head, val, pos):
        new_node = DoublyNode(val)
        if pos == 0:
            return self.insert_at_beginning(head, val)
        curr = head
        idx = 0
        while curr:
            if idx == pos:
                nxt = curr
                prev = curr.prev
                prev.next = new_node
                nxt.prev = new_node
                new_node.prev = prev
                new_node.next = nxt
                return head
            curr = curr.next
            idx += 1
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        return head

    # delete at beginning
    def delete_at_beginning(self, head: DoublyNode):
        curr = head.next
        curr.prev = None
        return curr

    # delete node
    def delete_at_pos(self, head, pos):
        if pos == 0:
            return self.delete_at_beginning(head)
        curr = head
        idx = 0
        while curr:
            if idx == pos:
                prev = curr.prev
                nxt = curr.next
                prev.next = nxt
                if nxt is not None:
                    nxt.prev = prev
                else:
                    self.tail = prev
                return head
            curr = curr.next
            idx += 1

        if curr is None:
            raise IndexError("Position out of bounds")
        return curr

    def search(self, head: DoublyNode, val):
        curr = head
        idx = 0
        while curr:
            if curr.val == val:
                return idx
            curr = curr.next
            idx += 1
        return None

class Queue:
    def __init__(self):
        self.queue = DoublyLinkedList()

    def enqueue(self, val):
        new_node = DoublyNode(val)
        if self.queue.head is None:
            self.queue.head = self.queue.tail = new_node
        else:
            prev = self.queue.tail.prev
            self.queue.tail.next = new_node
            self.queue.tail = new_node
            self.queue.tail.prev = prev

    def dequeue(self):
        node = self.queue.head
        nxt = self.queue.head.next
        nxt.prev = None
        self.queue.head = nxt
        return node

    def peek(self):
        return self.queue.head

    def is_empty(self):
        if self.queue.head is None:
            return True
        else:
            return False


queue = Queue()
print(queue.is_empty())

queue.enqueue(7)
queue.enqueue(8)
queue.enqueue(9)
queue.queue.display()

print(queue.dequeue())
queue.queue.display()

print(queue.peek())