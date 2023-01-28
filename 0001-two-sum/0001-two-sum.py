class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for index,  num in enumerate(nums):
        #     other_num = target - num
        #     if other_num in nums[index+1:]:
        #         return [index, len(nums)-1-nums[::-1].index(other_num)]
        hash_map = {}
        for index, num in enumerate(nums):
            hash_map[num] = index
        for index, num in enumerate(nums):
            other_num = target - num
            # print(other_num)
            if other_num in hash_map and index != hash_map[other_num]:
                return [index, hash_map[other_num]]