class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        chemistry = 0

        target = skill[0] + skill[-1]
        for i in range(n//2):
            if skill[i] + skill[n-i-1] != target:
                return -1
            chemistry += skill[i] * skill[n-i-1]
        return chemistry