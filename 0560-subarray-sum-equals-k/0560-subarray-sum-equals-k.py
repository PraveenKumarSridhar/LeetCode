class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_map = {0:1}
        prefix_sum = 0
        count = 0
        for val in nums:
            prefix_sum +=val
            count += hash_map.get(prefix_sum-k,0)
            hash_map[prefix_sum] = hash_map.get(prefix_sum,0)+1
            
        return count
                