# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:

    def __init__(self, head: Optional[ListNode]):
        current = head
        self.list = []
        self.size = 0
        while current:
            self.size += 1
            self.list.append(current.val)
            current = current.next

    def getRandom(self) -> int:
        target = random.randint(0, self.size-1)
        return self.list[target]

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()