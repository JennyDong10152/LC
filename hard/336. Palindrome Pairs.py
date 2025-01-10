class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        backward = {}
        answer = []

        for idx, word in enumerate(words):
            backward[word[::-1]] = idx
        
        for idx, word in enumerate(words):
            if word in backward and backward[word] != idx:
                answer.append([idx, backward[word]])
        
            if word != "" and "" in backward and word == word[::-1]:
                answer.append([idx, backward[""]])
                answer.append([backward[""], idx])
            
            for j in range(len(word)):
                if word[j:] in backward and word[:j] == word[j-1::-1]:
                    answer.append([backward[word[j:]], idx])
                if word[:j] in backward and word[j:] == word[:j-1:-1]:
                    answer.append([idx, backward[word[:j]]])
        return answer