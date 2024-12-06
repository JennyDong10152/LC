class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        parent = {word[0] : word[0] for word in similarPairs}
        parent.update({word[1]: word[1] for word in similarPairs})

        for word1, word2 in similarPairs:
            self.union(parent, word1, word2)

        for word1, word2 in zip(sentence1, sentence2):
            root1 = self.find(parent, word1)
            root2 = self.find(parent, word2)
            if ((not root1 or not root2) and word1!=word2) or root1 != root2:
                return False
        return True
    
    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_y] = root_x

    def find(self, parent, x):
        if not x in parent:
            return None
        if x != parent[x]:
            parent[x] = self.find(parent, parent[x])
        return parent[x]