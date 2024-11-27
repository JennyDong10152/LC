class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        new_group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = new_group_id
                new_group_id += 1
        
        item_graph = defaultdict(list)
        item_degree = [0] * n
        group_graph = defaultdict(list)
        group_degree = [0] * new_group_id
        
        for item in range(n):
            for prev in beforeItems[item]:
                item_graph[prev].append(item)
                item_degree[item] += 1

                if group[prev] != group[item]:
                    group_graph[group[prev]].append(group[item])
                    group_degree[group[item]] += 1
        
        group_order = self.sort(group_graph, group_degree, new_group_id)
        item_order = self.sort(item_graph, item_degree, n)

        if not group_order or not item_order:
            return []

        grouped_items = defaultdict(list)
        for item in item_order:
            grouped_items[group[item]].append(item)

        ans = []
        for g in group_order:
            ans.extend(grouped_items[g])
        return ans

    def sort(self, graph, degree, n):
        q = deque()
        ans = []
        for i in range(n):
            if not degree[i]:
                q.append(i)
        
        while q:
            curr = q.popleft()
            ans.append(curr)
            for neighbor in graph[curr]:
                degree[neighbor] -= 1
                if not degree[neighbor]:
                    q.append(neighbor)

        return ans if len(ans) == n else []