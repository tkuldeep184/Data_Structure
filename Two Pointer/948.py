class Solution:
    def bagOfTokensScore(self, tokens, power) -> int:
        result = 0
        score = 0
        tokens.sort()

        left, right = 0 , len(tokens)-1
        while left <= right :
            if power >= tokens[left]:
                power = power - tokens[left]
                left += 1
                score += 1
                result = max(result,score)

            elif score > 0:
                power = power + tokens[right]
                right -= 1
                score -= 1
            
            else:
                break

        return result