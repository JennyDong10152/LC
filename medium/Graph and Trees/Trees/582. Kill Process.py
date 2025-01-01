class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        self.relation = defaultdict(list)
        for parent, child in zip(ppid, pid):
            self.relation[parent].append(child)
        
        self.deleted = []
        self.delete(kill)
        return self.deleted
    
    def delete(self, kill):
        self.deleted.append(kill)
        for child in self.relation[kill]:
            self.delete(child)