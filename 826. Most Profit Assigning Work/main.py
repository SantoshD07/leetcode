class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        res = 0
        jobs = sorted(zip(difficulty, profit))
        worker.sort()

        j, maxProfit = 0, 0
        for i in range(len(worker)):
            while j < len(jobs) and jobs[j][0] <= worker[i]:
                maxProfit = max(maxProfit, jobs[j][1])
                j += 1

            res += maxProfit

        return res