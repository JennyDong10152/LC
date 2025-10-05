class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.answer = []
        self.backtrack(s, 0, [])
        return self.answer
    
    def backtrack(self, s, start, temp):
        if start == len(s):
            self.answer.append(list(temp))
            return 
        
        for end in range(start+1, len(s)+1):
            word = s[start:end]
            if self.isPalindrome(word):
                temp.append(word)
                self.backtrack(s, end, temp)
                temp.pop()
    
    def isPalindrome(self, word):
        return word == word[::-1]