class Solution:
    def maximumSubarraySum(self, nums, k: int) -> int:
        l = 0  # left
        seen = set()
        curr_sum = 0
        ans = 0

        for r in range(len(nums)): # right
            while nums[r] in seen:
                seen.remove(nums[l])
                curr_sum -= nums[l]
                l += 1

            seen.add(nums[r])
            curr_sum += nums[r]

            if r - l + 1 == k:
                ans = max(ans, curr_sum)
                seen.remove(nums[l])
                curr_sum -= nums[l]
                l += 1

        return ans