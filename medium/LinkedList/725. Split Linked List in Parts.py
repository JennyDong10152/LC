# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        node = head

        while node:
            length += 1
            node = node.next

        quotient, remainder = divmod(length, k)
        result = []
        prev = None
        node = head

        for _ in range(k):
            tempHead = node
            for i in range(quotient + (remainder > 0) - 1):
                if node:
                    node = node.next
            if node:
                prev = node
                node = node.next
                prev.next = None
            result.append(tempHead)
            remainder -= 1
        return result