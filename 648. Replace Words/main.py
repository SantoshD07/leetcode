from typing import *

class TrieNode():
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end_of_word = True

    def check_shortest_word(self, word: str):
        node = self.root
        prefix_root = ""
        for ch in word:

            if ch not in node.children:
                break

            node = node.children[ch]
            prefix_root += ch

            if node.end_of_word:
                return prefix_root

        return word

    # def __repr__(self):
    #     def recur(node, indent):
    #         return "".join(indent + key + ("$" if child.end_of_word else "")
    #                        + recur(child, indent + "  ")
    #                        for key, child in node.children.items())
    #
    #     return recur(self.root, "\n")


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # x = sentence.split(" ")
        # for root in dictionary:
        #     for i, word in enumerate(x):
        #         if word.startswith(root):
        #             x[i]=root

        # return " ".join(x)
        res = []
        x = sentence.split(" ")
        trie = Trie()

        for root in dictionary:
            trie.insert(root)

        for word in x:
            res.append(trie.check_shortest_word(word))

        print(trie)

        return " ".join(res)


