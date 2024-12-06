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
        for swap in groups.values():
            sorted_chars = sorted(char_lst[i] for i in swap)
            print(sorted_chars)
            for i, char in zip(sorted(swap), sorted_chars):
                char_lst[i] = char
                
        return "".join(char_lst)

    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_x] = root_y
    
    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]