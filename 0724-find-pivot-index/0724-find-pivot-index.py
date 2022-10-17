class Solution:
    def prefix_sum(self, nums:list[int])->int:
        for index in range(len(nums)):
            if index == 0:
                prev = 0
            else:
                prev = nums[index-1]
            nums[index] += prev
        return nums
    def pivotIndex(self, nums: List[int]) -> int:
        nums = self.prefix_sum(nums)
        print(nums)
        for index in range(len(nums)):
            if index == 0:
                left_sum = 0
            else:
                left_sum = nums[index-1]
            if index == len(nums)-1:
                right_sum = 0
            else:
                right_sum = nums[len(nums)-1] - nums[index]
            # print(index, left_sum,right_sum)
            if left_sum == right_sum:
                return index
        return -1