# @lc app=leetcode id=524 lang=python3
#
# [524] Longest Word in Dictionary through Deleting
#
# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/
#
# algorithms
# Medium (50.49%)
# Likes:    1158
# Dislikes: 315
# Total Accepted:    114.8K
# Total Submissions: 227.1K
# Testcase Example:  '"abpcplea"\n["ale","apple","monkey","plea"]'
#
# Given a string s and a string array dictionary, return the longest string in
# the dictionary that can be formed by deleting some of the given string
# characters. If there is more than one possible result, return the longest
# word with the smallest lexicographical order. If there is no possible result,
# return the empty string.
#
#
# Example 1:
#
#
# Input: s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
# Output: "apple"
#
#
# Example 2:
#
#
# Input: s = "abpcplea", dictionary = ["a","b","c"]
# Output: "a"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# 1 <= dictionary.length <= 1000
# 1 <= dictionary[i].length <= 1000
# s and dictionary[i] consist of lowercase English letters.
#
#
#

# @lc tags=two-pointers;sort

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求字符串数组中是给定字符串的子字符串中的最长的。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def isSub(sub, str):
            if len(sub) > len(str):
                return False
            idx, length = 0, len(str)
            for sc in sub:
                while idx < length:
                    if str[idx] == sc:
                        break
                    idx += 1
                if idx == length:
                    return False
                idx += 1
            return True

        dictionary.sort(key=lambda e: (-len(e), e))

        for str in dictionary:
            if isSub(str, s):
                return str
        return ''
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]')
    print('Exception :')
    print('"apple"')
    print('Output :')
    print(
        str(Solution().findLongestWord("abpcplea",
                                       ["ale", "apple", "monkey", "plea"])))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "abpcplea", dictionary = ["a","b","c"]')
    print('Exception :')
    print('"a"')
    print('Output :')
    print(str(Solution().findLongestWord("abpcplea", ["a", "b", "c"])))
    print()

    pass
# @lc main=end