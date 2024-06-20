class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        def check(position, mid, m):
            n = len(position)
            force = mid
            ball_count = 1
            prev = 0
            for i in range(1, n):
                if position[i] - position[prev] >= force:
                    ball_count += 1
                    prev = i
            return ball_count >= m

        position.sort()
        low = 1
        high = position[-1] - 1

        while low <= high:
            mid = (low + high) // 2
            if check(position, mid, m):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans

