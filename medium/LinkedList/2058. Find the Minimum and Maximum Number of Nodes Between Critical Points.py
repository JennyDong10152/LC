# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next:
            return [-1, -1]
        index = 1
        critical_points = []
        prev = head.val
        node = head.next

        while node and node.next:
            if (prev < node.val and node.next.val < node.val) or (prev > node.val and node.next.val > node.val):
                critical_points.append(index)
            index += 1
            prev = node.val
            node = node.next
        
        if len(critical_points) <= 1:
            return [-1, -1]
            
        min_distance = index+1
        max_distance = critical_points[-1] - critical_points[0]

        for idx1, idx2 in zip(critical_points, critical_points[1:]):
            min_distance = min(min_distance, idx2-idx1)
        return [min_distance, max_distance]