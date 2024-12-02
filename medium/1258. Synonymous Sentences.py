class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        parent = {}
        for x, y in synonyms:
            if not x in parent:
                parent[x] = x
            if not y in parent:
                parent[y] = y
            self.union(parent, x, y)
        
        syn_map = defaultdict(list)
        for key in parent:
            root = self.find(parent, key)
            syn_map[root].append(key)
        for key in syn_map:
            syn_map[key] = sorted(syn_map[key])
        
        words = text.split()
        ans = []
        self.makeSentence(parent, syn_map, words, 0, [], len(words), ans)
        
        return sorted(ans)

    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]
    
    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_x] = root_y

    def makeSentence(self, parent, syn_map, words, idx, curr_sentence, n, ans):
        if idx == n:
            ans.append(" ".join(curr_sentence))
            return
        
        word = words[idx]
        if word in parent:
            root_word = self.find(parent, word)
            for synonym in syn_map[root_word]:
                self.makeSentence(parent, syn_map, words, idx + 1, curr_sentence + [synonym], n, ans)
        else:
            self.makeSentence(parent, syn_map, words, idx + 1, curr_sentence + [word], n, ans) 