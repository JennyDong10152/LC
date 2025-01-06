class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        parentMap = defaultdict(str)

        for region in regions:
            parent = region[0]
            for subRegion in region[1:]:
                parentMap[subRegion] = parent
        
        ancestors = set()
        while region1:
            ancestors.add(region1)
            region1 = parentMap[region1]
        
        while region2 not in ancestors:
            region2 = parentMap[region2]
        return region2
        