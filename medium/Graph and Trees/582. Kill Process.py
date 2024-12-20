class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        relation = defaultdict(list)
        for parent, child in zip(ppid, pid):
            relation[parent].append(child)
        
        self.process_deleting = []
        self.delete(kill, relation)
        return self.process_deleting
    
    def delete(self, current, relation):
        self.process_deleting.append(current)
        for child in relation[current]:
            self.delete(child, relation)