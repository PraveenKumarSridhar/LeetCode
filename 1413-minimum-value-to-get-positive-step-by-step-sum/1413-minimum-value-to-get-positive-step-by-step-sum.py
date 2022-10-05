class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            nums[i] = prefix_sum
        print(nums)
        return abs(min(nums)) + 1 if min(nums) < 0 else 1