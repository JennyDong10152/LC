class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.answer = []
        self.search(s, 0, [])
        return self.answer
    
    def search(self, s, start, temp):
        if start == len(s):
            self.answer.append(list(temp))

        for end in range(start+1, len(s)+1):
            word = s[start: end]
            if self.isPalindrome(word):
                temp.append(word)
                self.search(s, end, temp)
                temp.pop()
                
    def isPalindrome(self, string):
        return string == string[::-1]