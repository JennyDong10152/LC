class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        queue = deque([(beginWord, [beginWord])])
        lists = []
        visited = set()
        found = False
        localVisited = set()

        while queue and not found:
            size = len(queue)
            localVisited.clear()

            for _ in range(size):
                word, path = queue.popleft()
                if word == endWord:
                    lists.append(path)
                    found = True

                for nextWord in wordSet:
                    if self.isNext(word, nextWord) and nextWord not in visited:
                        localVisited.add(nextWord)
                        queue.append((nextWord, path + [nextWord]))

            visited.update(localVisited)

        return lists

    def isNext(self, word: str, nextWord: str) -> bool:
        oneDiff = False
        for char1, char2 in zip(word, nextWord):
            if char1 != char2:
                if oneDiff:
                    return False
                oneDiff = True
        return True