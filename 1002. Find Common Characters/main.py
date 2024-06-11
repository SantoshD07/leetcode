from typing import *

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        from collections import Counter

        res = []
        dic = defaultdict(list)
        for i in range(len(words)):
            dic[i] = Counter(words[i])

        for ch in words[0]:  # [b,e,l,l,a]
            same = True
            for i in range(len(words)):
                if dic[i][ch] <= 0:
                    same = False
                    break
                dic[i][ch] -= 1
            if same:
                res.append(ch)

        return res

    # import functools
    # def commonChars(self, words: List[str]) -> List[str]:

    #     chars = set(words[0])
    #     res = []
    #     for ch in chars:
    #         freq = min(word.count(ch) for word in words)
    #         res += ch * freq

    #     return res


from collections import Counter, defaultdict


def commonChars(self, words: List[str]) -> List[str]:
    words = [sorted(w) for w in words]
    res = words[0]

    for word in words[1:]:
        res = list((Counter(res) & Counter(word)).elements())

    return (res)