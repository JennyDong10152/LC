class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = [i for i in range(n)]

        ownership = dict() #dict of emails : idx
        for i, emails in enumerate(accounts):
            for email in emails[1:]:
                if email in ownership:
                    self.union(parent, i, ownership[email])
                ownership[email] = i
        
        ans = defaultdict(list)
        for email, owner in ownership.items():
            root = self.find(parent, owner)
            ans[root].append(email)
        
        result = []
        for name, emails in ans.items():
            account = accounts[name][0]
            result.append([account] + sorted(emails))
        return result
    
    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_x] = root_y
    
    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x] 