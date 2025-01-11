class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split()
        words[0] = words[0].lower()

        arrange = defaultdict(list)
        for word in words:
            arrange[len(word)].append(word)
        
        sorted_words = []
        for length in sorted(arrange):
            sorted_words.extend(arrange[length])
        
        result = " ".join(sorted_words)
        return result.capitalize()
