class Solution:
    def minimumSteps(self, s: str) -> int:
        black = swap = 0 # 0(white)...1(black)
        for char in s:
            if char == "0":
                swap += black
            else:
                black += 1
        return swap