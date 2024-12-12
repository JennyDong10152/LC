# Reverse-related: 
# 24, 25, 61, 92, 143

# Circle/break-circle related: 
# 142

# Detecting Cycles
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

def reverseLinkedList(self, first = None, second = head):
    if not second:
        return first
    third = second.next
    second.next = first
    return self.recurse(second, third)

#Reverse first K nodes
def reverseFirstK(self, head: ListNode, k: int) -> ListNode:
    if k == 1 or not head:
        self.successor = head.next
        return head
    
    reversed_head = self.reverseFirstN(head.next, k - 1)
    head.next.next = head
    head.next = self.successor
    return reversed_head

def reverseFirstK(head: ListNode, k: int) -> ListNode:
    prev = None
    current = head
    while k > 0 and current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        k -= 1
    
    if head:
        head.next = current  
    return prev

#reverse between left and right (#92)
def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if not head or left == right:
        return head
    
    dummy = reverseTail = ListNode(0, head)
    for _ in range(left-1):
        reverseTail = reverseTail.next

    current = reverseTail.next
    prev = None
    for _ in range(right-left+1):
        nextNode = current.next
        current.next = prev
        prev = current
        current = nextNode
    
    reverseTail.next.next = current
    reverseTail.next = prev
    return dummy.next


#find midPoint
def findMidPoint(head):
        slow = head
        fast = head.next 
        #fast = head => picks the second is len(list) is even; fast = head.next => picks the first
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None

#merge two lists
def mergeTwoLists(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    if list1.val < list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2

def mergeTwoLists(list1, list2):
    dummy = ListNode(0)
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next 

    current.next = list1 if list1 else list2

    return dummy.next
