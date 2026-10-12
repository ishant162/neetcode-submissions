class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        st = set()

        for i in range(len(nums)):
            x = target - nums[i]
            if x in st:
                return sorted([i, nums.index(x)])
            st.add(nums[i])

        return []
