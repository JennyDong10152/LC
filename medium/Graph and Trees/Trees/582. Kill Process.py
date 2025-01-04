class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        self.relation = defaultdict(list)
        for child, parent in zip(pid, ppid):
            self.relation[parent].append(child)
        self.ids = []
        self.killing(kill)
        return self.ids
    
    def killing(self, target):
        self.ids.append(target)
        for child in self.relation[target]:
            self.killing(child)
