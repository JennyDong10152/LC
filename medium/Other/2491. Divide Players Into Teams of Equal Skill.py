class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        chemistry = 0
        target = skill[0] + skill[n-1]
        for idx in range(n//2):
            if skill[idx] + skill[n-1-idx] != target:
                return -1
            chemistry += (skill[idx] * skill[n-1-idx])
        return chemistry