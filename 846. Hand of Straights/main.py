from collections import Counter
from typing import *


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        freq = Counter(hand)
        for card in hand:
            start_card = card

            while freq[start_card - 1]:
                start_card -= 1

            while start_card <= card:
                while freq[start_card]:

                    for next_card in range(start_card, start_card + groupSize):
                        if not freq[next_card]:
                            return False
                        freq[next_card] -= 1

                start_card += 1

        return True

# class Solution(object):
#     def find_successors(self, hand, groupSize, i, n):
#         next_val = hand[i] + 1
#         hand[i] = -1  # Mark as used
#         count = 1
#         i += 1
#         while i < n and count < groupSize:
#             if hand[i] == next_val:
#                 next_val = hand[i] + 1
#                 hand[i] = -1
#                 count += 1
#             i += 1
#         return count == groupSize

#     def isNStraightHand(self, hand, groupSize):
#         n = len(hand)
#         if n % groupSize != 0:
#             return False
#         hand.sort()
#         for i in range(n):
#             if hand[i] >= 0:
#                 if not self.find_successors(hand, groupSize, i, n):
#                     return False
#         return True