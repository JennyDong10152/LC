class Solution:
    def alienOrder(self, words: List[str]) -> str:
        relation = defaultdict(list)
        degree = {c : 0 for word in words for c in word}

        for word1, word2 in zip(words, words[1:]):
            for char1, char2 in zip(word1, word2):
                if char1 != char2:
                    if char2 not in relation[char1]:
                        relation[char1].append(char2)
                        degree[char2] += 1
                    break
            else:
                if len(word1) > len(word2):
                    return ""
        
        queue = deque()
        order = ""
        for char in degree:
            if not degree[char]:
                queue.append(char)
            
        while queue:
            char = queue.popleft()
            order += char
            for nextChar in relation[char]:
                degree[nextChar] -= 1
                if not degree[nextChar]:
                    queue.append(nextChar)
        return order if len(order) == len(degree) else ""