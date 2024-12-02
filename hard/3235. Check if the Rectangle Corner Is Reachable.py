import math
from typing import List

class Solution:
    def canReachCorner(self, xCorner: int, yCorner: int, circles: List[List[int]]) -> bool:
        step = 1
        points = []
        point_index = {}
        idx = 0

        for x in range(0, xCorner + 1, step):
            for y in range(0, yCorner + 1, step):
                if self.isValidPoint(x, y, circles):
                    points.append((x, y))
                    point_index[(x, y)] = idx
                    idx += 1

        if (0, 0) not in point_index or (xCorner, yCorner) not in point_index:
            return False

        n = len(points)
        parent = list(range(n))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for x, y in points:
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if (new_x, new_y) in point_index:
                    self.union(parent, point_index[(x, y)], point_index[(new_x, new_y)])

        return self.find(parent, point_index[(0, 0)]) == self.find(parent, point_index[(xCorner, yCorner)])

    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]

    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_x] = root_y

    def isValidPoint(self, x, y, circles):
        for cx, cy, r in circles:
            if abs(x - cx) > r or abs(y - cy) > r:
                continue
            if math.sqrt((x - cx) ** 2 + (y - cy) ** 2) <= r:
                return False
        return True