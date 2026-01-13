class Solution:
    def separateSquares(self, squares) -> float:
        total_area = 0
        min_y = float("inf")
        max_y = float("-inf")

        for x, y, l in squares:
            total_area += l * l
            min_y = min(min_y, y)
            max_y = max(max_y, y + l)

        half = total_area / 2

        def area_below(Y):
            area = 0
            for x, y, l in squares:
                if Y <= y:
                    continue
                elif Y >= y + l:
                    area += l * l
                else:
                    area += l * (Y - y)
            return area

        left, right = min_y, max_y
        for _ in range(60):  # precision control
            mid = (left + right) / 2
            if area_below(mid) < half:
                left = mid
            else:
                right = mid

        return left
