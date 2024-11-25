from collections import defaultdict, deque
from typing import List

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        new_group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = new_group_id
                new_group_id += 1
        #each unasigned item becomes its own group
        #increment by one so they can be placed whereever convienient 

        item_graph = defaultdict(list)
        item_degree = [0] * n
        group_graph = defaultdict(list)
        group_degree = [0] * new_group_id

        for i in range(n):
            for prev in beforeItems[i]:
                item_graph[prev].append(i)
                item_degree[i] += 1

                if group[prev] != group[i]: 
                    group_graph[group[prev]].append(group[i])
                    group_degree[group[i]] += 1

        item_order = self.sort(item_graph, item_degree, n)
        group_order = self.sort(group_graph, group_degree, new_group_id)

        if not item_order or not group_order:
            return []

        grouped_items = defaultdict(list)
        for item in item_order:
            grouped_items[group[item]].append(item)

        result = []
        for g in group_order:
            result.extend(grouped_items[g])
        return result

    def sort(self, graph, degree, total_nodes):
        order = []
        q = deque()
        for i in range(total_nodes):
            if not degree[i]:
                q.append(i)

        while q:
            curr = q.popleft()
            order.append(curr)
            for neighbor in graph[curr]:
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    q.append(neighbor)
        return order if len(order) == total_nodes else []