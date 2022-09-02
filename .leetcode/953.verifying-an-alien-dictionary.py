# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#
# https://leetcode.com/problems/verifying-an-alien-dictionary/description/
#
# algorithms
# Easy (52.63%)
# Likes:    3049
# Dislikes: 979
# Total Accepted:    367K
# Total Submissions: 697.3K
# Testcase Example:  '["hello","leetcode"]\n"hlabcdefgijkmnopqrstuvwxyz"'
#
# In an alien language, surprisingly, they also use English lowercase letters,
# but possibly in a different order. The order of the alphabet is some
# permutation of lowercase letters.
#
# Given a sequence of words written in the alien language, and the order of the
# alphabet, return true if and only if the given words are sorted
# lexicographically in this alien language.
#
#
# Example 1:
#
#
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is
# sorted.
#
#
# Example 2:
#
#
# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] >
# words[1], hence the sequence is unsorted.
#
#
# Example 3:
#
#
# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is
# shorter (in size.) According to lexicographical rules "apple" > "app",
# because 'l' > '∅', where '∅' is defined as the blank character which is less
# than any other character (More info).
#
#
#
# Constraints:
#
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters in words[i] and order are English lowercase letters.
#
#
#

# @lc tags=string

# @lc imports=start

from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断给定字符串是否按照给定的字典序排列。
# 重新映射， 直接比较即可。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orda = ord('a')
        maps = [0] * 26

        def getOrd(c):
            return ord(c) - orda

        for i, c in enumerate(order):
            maps[getOrd(c)] = i

        def getAlienOrd(c):
            return maps[getOrd(c)]

        def compare(c1, c2):
            length = min(len(c1), len(c2))
            for idx in range(length):
                m1, m2 = getAlienOrd(c1[idx]), getAlienOrd(c2[idx])
                if m1 == m2:
                    continue
                return m1 < m2
            return len(c1) <= len(c2)

        for c1, c2 in pairwise(words):
            if not compare(c1, c2):
                return False
        return True

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"')
    print('Exception :')
    print('true')
    print('Output :')
    print(
        str(Solution().isAlienSorted(["hello", "leetcode"],
                                     "hlabcdefgijkmnopqrstuvwxyz")))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"')
    print('Exception :')
    print('false')
    print('Output :')
    print(
        str(Solution().isAlienSorted(["word", "world", "row"],
                                     "worldabcefghijkmnpqstuvxyz")))
    print()

    print('Example 3:')
    print('Input : ')
    print('words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"')
    print('Exception :')
    print('false')
    print('Output :')
    print(
        str(Solution().isAlienSorted(["apple", "app"],
                                     "abcdefghijklmnopqrstuvwxyz")))
    print()

    pass
# @lc main=end