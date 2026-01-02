class Solution:
    def nextPermutation(self, nums) -> None:
        
        # 1. find decreasing point
        # 2. find slightly greater element
        # 3. sort the remaining array  
        
        index = -1
        n = len(nums)

        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                index = i
                break

        if index == -1:
            nums.reverse()
            return

            ''' maine return nums.reverse() kar diya tha
            but ye python me galat hai, kyuki nums.reverse()
            inplace list ko modify karta hai aur None retrun 
            karta hai. therefore my answer was coming wrong for 
            2nd test case'''

        for i in range(n-1, index, -1):
            if nums[i] > nums[index]:
                nums[i],nums[index] = nums[index], nums[i]
                break

        nums[index + 1:] = reversed(nums[index + 1:])