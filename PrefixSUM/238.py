class Solution:
    def productExceptSelf(self, nums) :
        n = len(nums)
        left = [1] * n
        right = [1] * n
        answer = [1] * n

        for i in range(1,n):
            left[i] = left[i-1]* nums[i-1]

        for i in range(n-2,-1,-1):
            right[i] = right[i+1]* nums[i+1]

        for i in range(n):
            answer[i] = left[i] * right[i]

        return answer

if __name__ == "__main__":
    nums = [1, 2, 3, 4]  # Example input
    solution = Solution()
    result = solution.productExceptSelf(nums)
    print("Output:", result)