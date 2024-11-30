class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(list)
        degree = {c : 0 for word in words for c in word}

        for word1, word2 in zip(words, words[1:]):
            for c, d in zip(word1, word2):
                if c != d:
                    if not d in graph[c]:
                        graph[c].append(d)
                        degree[d] += 1
                    break
            else:
                if len(word1) > len(word2):
                    return ""
        
        q = deque()
        order = ""
        for c in degree:
            if not degree[c]:
                q.append(c)
        
        while q:
            curr = q.popleft()
            order += curr
            for char in graph[curr]:
                degree[char] -= 1
                if not degree[char]:
                    q.append(char)
        return order if len(order) == len(degree) else ""