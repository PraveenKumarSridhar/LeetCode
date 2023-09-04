class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        
        l_prod_arr = [1] * n
        for i in range(1,n):
            l_prod_arr[i] = l_prod_arr[i-1] * nums[i-1]
            
        r_prod_arr = [1] * n
        for i in range(n-2,-1,-1):
            # print(i,r_prod_arr)
            r_prod_arr[i] = r_prod_arr[i+1] * nums[i+1]
        
        for i in range(n):
            ans[i] = l_prod_arr[i] * r_prod_arr[i]
            
        return ans