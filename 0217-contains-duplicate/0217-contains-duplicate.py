from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map = Counter()
        for num in nums:
            if hash_map[num] > 0 :
                return True
            hash_map[num] += 1
        return False
            