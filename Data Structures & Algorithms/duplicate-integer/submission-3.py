class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        mymap = dict()
        for i in range(len(nums)):
            mymap[nums[i]] = mymap.get(nums[i],0) + 1

        for i in mymap.values():
            if i>=2:
                return True
        return False