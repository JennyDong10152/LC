class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)
        degree = {char: 0 for word in words for char in word}  

        for word1, word2 in zip(words, words[1:]):
            for c, d in zip(word1, word2):
                if c != d:
                    if d not in graph[c]: 
                        graph[c].add(d)
                        degree[d] += 1
                    break
            else:
                if len(word2) < len(word1):
                    return ""
        
        q = deque()
        for char in degree:
            if not degree[char]:
                q.append(char)
        ans = []

        while q:
            curr = q.popleft()
            ans.append(curr)
            for neighbor in graph[curr]:
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    q.append(neighbor)

        if len(ans) < len(degree):
            return ""

        return "".join(ans)