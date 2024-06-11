class Solution:
    def longestPalindrome(self, s: str) -> int:
        temp = set()
        length = 0
        for i in s:
            if i in temp:
                temp.remove(i)
                length += 2
            else:
                temp.add(i)

        if temp:
            length += 1

        return length