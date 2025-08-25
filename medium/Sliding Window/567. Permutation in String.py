class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1Frequency = [0] * 26
        s2Frequency = [0] * 26

        for idx, char in enumerate(s1):
            s1Frequency[ord(char) - ord('a')] += 1
            s2Frequency[ord(s2[idx]) - ord('a')] += 1
        
        for idx in range(len(s1), len(s2)):
            if s1Frequency == s2Frequency:
                return True
            s2Frequency[ord(s2[idx]) - ord('a')] += 1
            s2Frequency[ord(s2[idx - len(s1)]) - ord('a')] -= 1
        return s1Frequency == s2Frequency 