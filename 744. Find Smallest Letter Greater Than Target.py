class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters)-1
        ans = letters[0]

        while left <= right:
            mid = left+(right-left)//2
            midV = letters[mid]
            if ord(midV) > ord(target):
                ans = midV
                right = mid - 1
            else:
                left = mid + 1
        return ans 