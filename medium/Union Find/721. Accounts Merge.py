class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        n = len(accounts)
        parent = [i for i in range(n)]
        ownership = defaultdict()
        
        for idx, account in enumerate(accounts):
            name = accounts[0]
            for email in account[1:]:
                if email in ownership:
                    self.union(parent, idx, ownership[email])
                ownership[email] = idx
        
        grouped = defaultdict(set)
        for email, owner in ownership.items():
            root = self.find(parent, owner)
            grouped[root].add(email)

        ans = []
        for owner, emails in grouped.items():
            name = accounts[owner][0]
            ans.append([name] + sorted(emails))
        return ans

    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_y] = root_x
    
    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]