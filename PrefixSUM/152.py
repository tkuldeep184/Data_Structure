class Solution:
    def maxProduct(self, nums) -> int:
        curr_max = curr_min = ans = nums[0]

        for i in range(1,len(nums)):
            temp = curr_max
            curr_max = max(nums[i], nums[i] * curr_max, nums[i] * curr_min)
            curr_min = min (nums[i], nums[i] * temp, nums[i] * curr_min)
            ans = max(ans, curr_max)

            #tricky while implementing and dry run 

        return ans
