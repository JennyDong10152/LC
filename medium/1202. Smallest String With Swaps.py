class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = [i for i in range(n)]
        
        for x, y in pairs:
            self.union(parent, x, y)

        groups = defaultdict(list)
        for i in range(n):
            root = self.find(parent, i)
            groups[root].append(i)

        char_lst = list(s)
        for idx in groups.values():
            sorted_chars = sorted(char_lst[i] for i in idx)
            for i, char in zip(sorted(idx), sorted_chars):
                char_lst[i] = char
        return ''.join(char_lst)

    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y
    
    def find(self, parent, x):
        if x != parent[x]:
            parent[x] = self.find(parent, parent[x])
        return parent[x]