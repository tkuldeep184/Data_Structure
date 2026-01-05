class Solution:
    def sumFourDivisors(self, nums) -> int:
        total = 0

        for num in nums:
            cnt = 0
            sum = 0 
            
            for i in range(1,int(num ** 0.5) + 1):
                if num % i == 0:
                    other = num // i
                    if i == other:
                        cnt += 1
                        sum += i
                    else:
                        cnt +=2
                        sum += i + other

            if cnt == 4:
                total += sum


        return total

