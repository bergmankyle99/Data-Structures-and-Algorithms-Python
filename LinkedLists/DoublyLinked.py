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


Head = Tail = DoublyNode(1)

def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print("<->".join(elements))

print("Tail")
display(Tail)

#insert at beginning O(1)
def insert_at_beginning(head,  val):
    new_node = DoublyNode(val)
    head.prev = new_node
    new_node.next = head
    return new_node
Head = insert_at_beginning(Head, 7)
print("Insert At Beginning")
display(Head)

#insert at position O(n)
def insert_at_position(head, val, pos):
    new_node = DoublyNode(val)
    if pos == 0:
        return insert_at_beginning(head, val)
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
    if curr is None:
        raise IndexError("Position out of bounds")
    return head

Head = insert_at_position(Head, 9, 1)
print("Insert at Pos")
display(Head)

#delete at beginning
def delete_at_beginning(head):
    curr = head.next
    curr.prev = None
    return curr

#delete node
def delete_at_pos(head, pos):
    if pos == 0:
        return delete_at_beginning(head)
    curr = head
    idx = 0
    while curr:
        if idx == pos:
            prev = curr.prev
            nxt = curr.next
            prev.next = nxt
            if nxt is not None:
                nxt.prev = prev
            return head
        curr = curr.next
        idx += 1
    if curr is None:
        raise IndexError("Position out of bounds")
    return curr
print("Delete at Pos")
Head = delete_at_pos(Head, 4)
display(Head)