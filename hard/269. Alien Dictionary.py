class Solution:
    def alienOrder(self, words: List[str]) -> str:
        relation = defaultdict(list)#prequisite : list()
        degree = {c : 0 for word in words for c in word}

        for word1, word2 in zip(words, words[1:]):
            for c, d in zip(word1, word2):
                if c != d:
                    if d not in relation[c]:
                        relation[c].append(d)
                        degree[d] += 1
                    break
            else:
                if len(word1) > len(word2):
                    return ""
        
        q = deque()
        for i in degree:
            if not degree[i]:
                q.append(i)
        ans = ""
        while q:
            curr = q.popleft()
            ans += curr
            for neighbor in relation[curr]:
                degree[neighbor] -= 1
                if not degree[neighbor]:
                    q.append(neighbor)
        return ans if len(ans) == len(degree) else ""
