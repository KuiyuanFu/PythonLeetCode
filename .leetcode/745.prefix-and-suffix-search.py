# @lc app=leetcode id=745 lang=python3
#
# [745] Prefix and Suffix Search
#
# https://leetcode.com/problems/prefix-and-suffix-search/description/
#
# algorithms
# Hard (35.39%)
# Likes:    879
# Dislikes: 309
# Total Accepted:    43.9K
# Total Submissions: 123.2K
# Testcase Example:  '["WordFilter","f"]\n[[["apple"]],["a","e"]]'
#
# Design a special dictionary with some words that searchs the words in it by a
# prefix and a suffix.
#
# Implement the WordFilter class:
#
#
# WordFilter(string[] words) Initializes the object with the words in the
# dictionary.
# f(string prefix, string suffix) Returns the index of the word in the
# dictionary, which has the prefix prefix and the suffix suffix. If there is
# more than one valid index, return the largest of them. If there is no such
# word in the dictionary, return -1.
#
#
#
# Example 1:
#
#
# Input
# ["WordFilter", "f"]
# [[["apple"]], ["a", "e"]]
# Output
# [null, 0]
#
# Explanation
# WordFilter wordFilter = new WordFilter(["apple"]);
# wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix =
# "a" and suffix = 'e".
#
#
#
# Constraints:
#
#
# 1 <= words.length <= 15000
# 1 <= words[i].length <= 10
# 1 <= prefix.length, suffix.length <= 10
# words[i], prefix and suffix consist of lower-case English letters only.
# At most 15000 calls will be made to the function f.
#
#
#

# @lc tags=binary-search

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 前后缀匹配。
# 树。
# 使用‘{’符标志分割，对于每一个前缀的节点，增加一个后缀的子树。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class fix:
    def __init__(self, idx=0) -> None:
        self.idx = idx
        self.children = [None] * 27


orda = ord('a')


def insertSuffic(p: fix, word: str, idx: int):
    for c in word:
        if p.children[ord(c) - orda] is None:
            p.children[ord(c) - orda] = fix()
        p = p.children[ord(c) - orda]
        p.idx = idx


def insertPrefix(p: fix, word: str, idx: int):
    su = str('{' + str(word[::-1]))

    for c in word:
        if p.children[ord(c) - orda] is None:
            p.children[ord(c) - orda] = fix()
        p = p.children[ord(c) - orda]
        p.idx = idx
        insertSuffic(p, su, idx)


def search(p: fix, word: str):
    for c in word:
        if p.children[ord(c) - orda] is None:
            return -1
        p = p.children[ord(c) - orda]
    return p.idx


class WordFilter:
    def __init__(self, words: List[str]):
        self.root = fix()
        for i, word in enumerate(words):
            insertPrefix(self.root, word, i)

    def f(self, prefix: str, suffix: str) -> int:

        return search(self.root, prefix + '{' + str(suffix[::-1]))


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    o = WordFilter([
        "cabaabaaaa", "ccbcababac", "bacaabccba", "bcbbcbacaa", "abcaccbcaa",
        "accabaccaa", "cabcbbbcca", "ababccabcb", "caccbbcbab", "bccbacbcba"
    ])
    print(o.f("bccbacbcba", "a"))
    print(o.f("ab", "abcaccbcaa"))
    print(o.f("a", "aa"))
    print(o.f("cabaaba", "abaaaa"))
    print(o.f("cacc", "accbbcbab"))
    print(o.f("ccbcab", "bac"))
    print(o.f("bac", "cba"))
    print(o.f("ac", "accabaccaa"))
    print(o.f("bcbb", "aa"))
    print(o.f("ccbca", "cbcababac"))

# @lc main=end