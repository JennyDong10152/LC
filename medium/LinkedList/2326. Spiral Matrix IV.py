# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        left = top = 0
        right = n - 1
        bottom = m - 1

        while head and left <= right and top <= bottom:
            for i in range(left, right+1):
                if not head:
                    break
                matrix[top][i] = head.val
                head = head.next
            top += 1

            for i in range(top, bottom+1):
                if not head:
                    break
                matrix[i][right] = head.val
                head = head.next
            right -= 1

            if right >= left:
                for i in range(right, left-1, -1):
                    if not head:
                        break
                    matrix[bottom][i] = head.val
                    head = head.next
                bottom -= 1

            if top <= bottom:
                for i in range(bottom, top-1, -1):
                    if not head:
                        break
                    matrix[i][left] = head.val
                    head = head.next
                left += 1
                
        return matrix