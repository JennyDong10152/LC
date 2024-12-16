# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next:
            return [-1,-1]
        critical_points = []
        index = 1
        prev = head.val
        node = head.next

        while node and node.next:
            if (prev < node.val and node.next.val < node.val) or (prev > node.val and node.next.val > node.val):
                critical_points.append(index)
            prev = node.val
            index += 1
            node = node.next

        if len(critical_points) <= 1:
            return [-1,-1]
        maxLength = critical_points[-1] - critical_points[0]
        minLength = index+1

        for idx1, idx2 in zip(critical_points, critical_points[1:]):
            minLength = min(minLength, idx2-idx1)
        return [minLength, maxLength]