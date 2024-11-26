class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)
        degree = {char : 0  for word in words for char in word}

        for word1, word2 in zip(words, words[1:]):
            for c, d in zip(word1, word2):
                if c != d:
                    if d not in graph[c]:
                        graph[c].add(d)
                        degree[d] += 1
                    break
            else:
                if len(word1) > len(word2):
                    return ""
        
        q = deque()
        for c in degree:
            if not degree[c]:
                q.append(c)
        
        ans = ""
        while q:
            char = q.popleft()
            ans += char
            for c in graph[char]:
                degree[c] -= 1
                if not degree[c]:
                    q.append(c)
        return ans if len(ans) == len(degree) else ""