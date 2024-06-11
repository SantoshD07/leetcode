from typing import *


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        # res = []
        # sum = nums[0]

        # for i in range(1, len(nums)):

        #     if sum % k == 0 and sum != 0:
        #         return True
        #     else:
        #         sum += nums[i]
        #         if nums[i] != 0:
        #             print("Sum", sum)
        #             if  k % nums[i] != 0:
        #                 continue
        #         else:
        #             sum = nums[i]

        # print(sum)
        # if sum == 0:
        #     if nums.count(0)==1:
        #         return False
        #     return True

        # if sum % k == 0 and sum != 0:
        #     return True
        # else:
        #     return False

        map = {0: -1}
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]
            rem = sum % k

            if rem in map:
                if i - map[rem] > 1:
                    return True
            else:
                map[rem] = i

        return False


