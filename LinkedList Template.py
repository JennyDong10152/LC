#Detecting Cycles
def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

#reverse a linkedlist
def reverseLinkedList(head):
    prev = None
    current = head
    while current:
        next_node = current.next 
        current.next = prev
        prev = current
        current = next_node
    return prev  

def reverseLinkedList(head):
    if not head or not head.next:
        return head  
    new_head = reverseLinkedList(head.next)
    head.next.next = head
    head.next = None
    return new_head
