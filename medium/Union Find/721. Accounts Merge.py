class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = [i for i in range(n)]
        ownership = defaultdict()
        grouped = defaultdict(set)
        ans = []

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in ownership:
                    self.union(parent, i, ownership[email])
                ownership[email] = i

        for email, owner in ownership.items():
            root = self.find(parent, owner)
            grouped[root].add(email)
        
        for owner, emails in grouped.items():
            account = accounts[owner][0]
            ans.append([account] + sorted(emails))
        return ans
    
    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_y] = root_x
    
    def find(self, parent, x):
        if x != parent[x]:
            parent[x] = self.find(parent, parent[x])
        return parent[x]