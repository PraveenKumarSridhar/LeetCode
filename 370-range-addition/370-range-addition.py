class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        
        arr = [0] * length
        
        prefix_update = [0] * (length + 1)
        
        for st, end, inc in updates:
            prefix_update[st] += inc
            prefix_update[end+1] += -inc
        
        prefix_sum = 0
        for i in range(length):
            prefix_sum+=prefix_update[i]
            arr[i] = prefix_sum
        
        return arr