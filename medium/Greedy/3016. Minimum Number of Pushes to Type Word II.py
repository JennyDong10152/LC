class Solution:
    def minimumPushes(self, word: str) -> int:
        frequency = [0] * 26
        for char in word:
            frequency[ord(char) - ord("a")] += 1

        frequency.sort(reverse = True)
        total = 0

        for char in range(26):
            if not frequency[char]:
                break
            total += (char // 8 + 1) * frequency[char]
        return total