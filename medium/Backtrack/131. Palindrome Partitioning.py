class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.answer = []
        self.backtrack(s, 0, [])
        return self.answer
    
    def backtrack(self, s, start, path):
        if start == len(s):
            self.answer.append(list(path))
            return 
        
        for end in range(start+1, len(s)+1):
            if self.isPalindrome(s[start:end]):
                self.backtrack(s, end, path + [s[start:end]])
    
    def isPalindrome(self, string):
        return string == string[::-1]