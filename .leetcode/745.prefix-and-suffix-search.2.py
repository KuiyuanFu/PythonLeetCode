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
# 两棵树，去重。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class fix:
    def __init__(self, ) -> None:
        self.idx = []
        self.children = [None] * 26


orda = ord('a')


def insert(p: fix, word: str, idx: int):
    for c in word:
        if p.children[ord(c) - orda] is None:
            p.children[ord(c) - orda] = fix()
        p = p.children[ord(c) - orda]
        p.idx.append(idx)


def search(p: fix, word: str):
    for c in word:
        if p.children[ord(c) - orda] is None:
            return []
        p = p.children[ord(c) - orda]
    return p.idx


class WordFilter:
    def __init__(self, words: List[str]):
        d = defaultdict(int)
        for i, word in enumerate(words):
            d[word] = i
        self.pre = fix()
        self.suf = fix()
        for word in d.keys():
            i = d[word]
            insert(self.pre, word, i)
            insert(self.suf, word[::-1], i)
        self.buff = {}

    def f(self, prefix: str, suffix: str) -> int:
        k = prefix + '{' + suffix
        if k in self.buff:
            return self.buff[k]

        res = -1

        preList = search(self.pre, prefix)
        sufList = search(self.suf, suffix[::-1])
        pi, si = len(preList) - 1, len(sufList) - 1
        while pi >= 0 and si >= 0:
            p, s = preList[pi], sufList[si]
            if p == s:
                res = p
                break
            if p > s:
                pi -= 1
            else:
                si -= 1
        self.buff[k] = res
        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    o = WordFilter(["apple"])

    print(o.f("b", "e"))
    print()

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