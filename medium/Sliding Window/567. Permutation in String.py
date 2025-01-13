class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1Count = [0] * 26
        s2Count = [0] * 26
        
        for idx in range(len(s1)):
            s1Count[ord(s1[idx]) - ord('a')] += 1
            s2Count[ord(s2[idx]) - ord('a')] += 1
            
        for idx in range(len(s1), len(s2)):
            if s1Count == s2Count:
                return True
            s2Count[ord(s2[idx - len(s1)]) - ord('a')] -= 1
            s2Count[ord(s2[idx]) - ord('a')] += 1
        return s1Count == s2Count