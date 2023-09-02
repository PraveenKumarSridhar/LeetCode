class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for index, num in enumerate(nums):
            other_num = target - num
            if other_num in hash_map:
                return [hash_map[other_num], index]
            hash_map[num] = index
        