class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        count = 1
        visited = set()
        queue = deque([beginWord])
        if endWord not in wordList:
            return 0
            
        while queue:
            size = len(queue)
            for _ in range(size):
                word = queue.popleft()
                if word == endWord:
                    return count
                if word in visited:
                    continue
                visited.add(word)
                for nextWord in wordList:
                    if self.isNext(word, nextWord) and (not nextWord in visited):
                        queue.append(nextWord)
            count += 1
        return 0
    
    def isNext(self, word, nextWord):
        oneDiff = False
        for char1, char2 in zip(word, nextWord):
            if char1 != char2:
                if oneDiff:
                    return False
                oneDiff = True
        return True