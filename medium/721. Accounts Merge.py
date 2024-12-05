class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = [i for i in range(n)]
        all_email = dict()

        for i, emails in enumerate(accounts):
            for email in emails[1:]:
                if email in all_email:
                    self.union(parent, i, all_email[email])
                all_email[email] = i

        groups = defaultdict(set)
        for email, owner in all_email.items():
            idx = self.find(parent, owner)
            groups[idx].add(email)
        
        ans = []
        for idx, email in groups.items():
            name = accounts[idx][0]
            ans.append([name] + sorted(email))
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