#==============================================
# Doubly Linked List
# - Have access to head and tail now
# - deleting in middle is sometimes O(1) because you have both next and prev
#==============================================

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

    def display(self, head):
        curr = head
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

dll = DoublyLinkedList()
dll.head = dll.tail = DoublyNode(1)
print("Tail")
dll.display(dll.tail)

dll.head = dll.insert_at_beginning(dll.head, 7)
print("Insert At Beginning")
dll.display(dll.head)

dll.head = dll.insert_at_position(dll.head, 9, 1)
print("Insert at Pos")
dll.display(dll.head)

dll.head = dll.insert_at_position(dll.head, 11, 3)
print("Insert at Pos")
dll.display(dll.head)
print("Tail: "+str(dll.tail))

print("Delete at Pos")
dll.head = dll.delete_at_pos(dll.head, 2)
dll.display(dll.head)

res = dll.search(dll.head, 11)
if res:
    dll.head = dll.delete_at_pos(dll.head, res)
    dll.display(dll.head)
else:
    print("Doesn't Exist")

print("Tail: "+str(dll.tail))