class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.subset = []
        self.search(0, [], nums)
        return self.subset
    
    def search(self, start, temp, nums):
        if start == len(nums):
            self.subset.append(list(temp))
            return 

        temp.append(nums[start])
        self.search(start+1, temp, nums)
        temp.pop()
        self.search(start+1, temp, nums)