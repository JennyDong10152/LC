# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        frequency = defaultdict(int)
        node = head
        while node:
            frequency[node.val] += 1
            node = node.next

        ansNode = dummy = ListNode(0)
        for value in frequency.values():
            ansNode.next = ListNode(value)
            ansNode = ansNode.next
        return dummy.next