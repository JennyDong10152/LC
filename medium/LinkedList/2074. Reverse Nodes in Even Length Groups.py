# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        length = 2

        while prev.next:
            node = prev
            count = 0
            for _ in range(length):
                if not node.next:
                    break
                count += 1
                node = node.next
            if count % 2:
                prev = node
            else:
                node = prev.next
                previous = None
                for _ in range(count):
                    nextNode = node.next
                    node.next = previous
                    previous = node
                    node = nextNode
                prev.next.next, prev.next, prev = node, previous, prev.next
            length += 1
        return head