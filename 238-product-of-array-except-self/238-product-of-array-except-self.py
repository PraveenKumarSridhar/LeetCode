class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left_prod, right_prod = [1],[1]
        
        for val in nums:
            prefix_prod = left_prod[-1] * val
            left_prod.append(prefix_prod)
            
        for val in reversed(nums):
            postfix_prod = right_prod[-1] * val
            right_prod.append(postfix_prod)
        
        n = len(nums)
        output = []
        
        for i in range(n):
            result_elm = left_prod[i]* right_prod[n-1-i]
            output.append(result_elm)
        
        return output
            
        
        