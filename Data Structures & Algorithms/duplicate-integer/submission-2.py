class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        myset = set()
        myset.update(nums)

        return not (len(nums)==len(myset))