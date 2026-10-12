class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        st = set()

        for i in range(len(nums)):
            x = target - nums[i]
            if x in st:
                idx = nums.index(x)
                return sorted([i, idx])
            st.add(nums[i])

        return []
