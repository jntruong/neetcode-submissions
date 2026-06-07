class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = {}
        for n in nums:
            if n in hmap:
                return True
            hmap[n] = True
        return False