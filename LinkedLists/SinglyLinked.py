#==============================================
# Linked Lists
# - Non-Contiguous block of memory
# - end of list is None
# - to get element in linked list we must traverse, no indices
# - Add node in position 2 (for example) is O(n)
# - Add node at beginning is O(1)
# - Delete node in position 2 (for example) is O(n)
# - Delete node in beginning is O(1)
# - Access node in position 2 (for example) is O(n)
# - Lookup at position 2 (for example) is O(n)
#==============================================

class SinglyNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    #Print method
    def __str__(self):
        return str(self.val)

# create elements
Head = SinglyNode(1)
A = SinglyNode(2)
B = SinglyNode(3)
C = SinglyNode(4)
# insert at end
Head.next = A
A.next = B
B.next = C

#traversal O(n)
current = Head
while current:
    print(str(current.val))
    current = current.next

#print list O(n)
def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print('->'.join(elements))

display(Head)
# insert at beginning
def insert_at_beginning(head, val): #O(1)
    new_node = SinglyNode(val)
    new_node.next = head
    return new_node

Head = insert_at_beginning(Head, 7)
display(Head)

#insert in middle
def insert_at_pos(head, val, pos): #O(n)
    if pos == 0:
        return insert_at_beginning(head, val)
    new_node = SinglyNode(val)
    curr = head
    idx = 1
    while curr:
        if idx == pos:
            break
        curr = curr.next
        idx+=1
    if curr is None:
        raise IndexError("Position out of bounds")
    new_node.next = curr.next
    curr.next = new_node
    return head

Head = insert_at_pos(Head, 6, 4)
display(Head)

#insert after node
def insert_after(node, val): #O(1)
    if node is None:
        print("Previous node cannot be None")
        return
    new_node = SinglyNode(val)
    new_node.next = node.next
    node.next = new_node

insert_after(C, 10)
display(Head)

#insert at end
def insert_at_end(head, val): #O(1)
    new_node = SinglyNode(val)
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node

insert_at_end(Head, 11)
display(Head)

#search for node value O(n)
def search(head, val):
    curr = head
    while curr:
        if curr.val == val:
            return True
        curr = curr.next
    return False

print(search(Head, 9))

def display_reversed(head):
    if not head:
        return
    display_reversed(head.next)
    print(head)



def reverse_list(head):
    curr = head
    prev = None
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

new_list = reverse_list(Head)
display(new_list)
