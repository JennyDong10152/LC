class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = [i for i in range(n)]
        ownership = dict() #email : idx

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in ownership:
                    self.union(parent, i, ownership[email])
                ownership[email] = i
        
        merged = defaultdict(list)
        for email, owner in ownership.items():
            idx = self.find(parent, owner)
            merged[idx].append(email)

        ans = []
        for idx, emails in merged.items():
            name = accounts[idx][0]
            ans.append([name] + sorted(emails))
        return ans
    
    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_x] = root_y
    
    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]
