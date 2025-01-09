class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for word in strs:
            root = "".join(sorted(word))
            anagram[root].append(word)
        return list(anagram.values())