# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        head = current = PolyNode()

        while poly1 and poly2:
            power = coefficient = 0
            if poly1.power > poly2.power:
                power = poly1.power
                coefficient = poly1.coefficient
                poly1 = poly1.next

            elif poly1.power < poly2.power:
                power = poly2.power
                coefficient = poly2.coefficient
                poly2 = poly2.next

            else:
                power = poly1.power
                coefficient = poly1.coefficient + poly2.coefficient
                poly1 = poly1.next
                poly2 = poly2.next

            if power == current.power:
                current.coefficient += coefficient
            elif coefficient:
                current.next = PolyNode(coefficient, power)
                current = current.next
        if poly1:
            current.next = poly1
        if poly2:
            current.next = poly2
        return head.next