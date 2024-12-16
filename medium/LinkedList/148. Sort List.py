# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        midNode = slow.next
        slow.next = None
        list1 = self.sortList(head)
        list2 = self.sortList(midNode)
        return self.sort(list1, list2)
    
    def sort(self, list1, list2):
        dummy = node = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        node.next = list1 if list1 else list2
        return dummy.next