# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#
# https://leetcode.com/problems/find-common-characters/description/
#
# algorithms
# Easy (68.34%)
# Likes:    2620
# Dislikes: 214
# Total Accepted:    158.7K
# Total Submissions: 232.2K
# Testcase Example:  '["bella","label","roller"]'
#
# Given a string array words, return an array of all characters that show up in
# all strings within the words (including duplicates). You may return the
# answer in any order.
#
#
# Example 1:
# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:
# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]
#
#
# Constraints:
#
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of lowercase English letters.
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求所有字符串中都出现过的字符。
# 计数
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def commonChars(self, words: List[str]) -> List[str]:

        counter = [0] * 26

        for word in words:
            s = set(word)
            for c in s:
                counter[ord(c) - ord('a')] += 1
        res = []
        t = len(words)
        for i, c in enumerate(counter):
            if c == t:
                res.append(chr(i + ord('a')))
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('words = ["bella","label","roller"]')
    print('Exception :')
    print('["e","l","l"]')
    print('Output :')
    print(str(Solution().commonChars(["bella", "label", "roller"])))
    print()

    print('Example 2:')
    print('Input : ')
    print('words = ["cool","lock","cook"]')
    print('Exception :')
    print('["c","o"]')
    print('Output :')
    print(str(Solution().commonChars(["cool", "lock", "cook"])))
    print()

    pass
# @lc main=end