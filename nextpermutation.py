class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # 1. Find the first decreasing element from the right
        i = n - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        # If a decreasing element is found (i >= 0), proceed with swap
        if i >= 0:
            # 2. Find the first element larger than nums[i] from the right
            j = n - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1
            # Swap the elements
            nums[i], nums[j] = nums[j], nums[i]
        
        # 3. Reverse the subarray to the right of i
        # This handles the case where no pivot was found (i == -1) 
        # by reversing the entire array
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
