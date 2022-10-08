class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums)-1
        
        if nums[right] >= nums[left]:
            return nums[left]
        
        while left <= right:
            mid = (right-left)//2 + left
            print(left, right, mid)
            
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            
            if nums[mid-1]> nums[mid]:
                return nums[mid]
            
            if nums[mid] < nums[left] :
                right = mid -1
            elif nums[mid] > nums[right]:
                left = mid +1
            
        
        # return output
                