# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#
# https://leetcode.com/problems/remove-duplicate-letters/description/
#
# algorithms
# Medium (39.94%)
# Likes:    2871
# Dislikes: 206
# Total Accepted:    128.3K
# Total Submissions: 321.1K
# Testcase Example:  '"bcabc"'
#
# Given a string s, remove duplicate letters so that every letter appears once
# and only once. You must make sure your result is the smallest in
# lexicographical order among all possible results.
#
#
# Example 1:
#
#
# Input: s = "bcabc"
# Output: "abc"
#
#
# Example 2:
#
#
# Input: s = "cbacdcbc"
# Output: "acdb"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^4
# s consists of lowercase English letters.
#
#
#
# Note: This question is the same as 1081:
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
#
#

# @lc tags=stack;greedy

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 去掉重复的字母，并以字母表顺序排列返回。
# 每一次从后向前遍历，在将所有未加入到结果中的元素都找到后，记录最小的元素。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        nums = [ord(c) - ord('a') for c in s]

        needToVisit = [False] * 26
        times = [0] * 26
        res = []
        for n in nums:
            times[n] += 1
            needToVisit[n] = True
        diffCount = 0
        for t in times:
            diffCount += 1 if t != 0 else 0

        idxL, idxR = 0, len(nums)
        for dc in reversed(range(1, diffCount + 1)):
            needToVisitCopy = needToVisit.copy()
            smallest = 26
            for i in reversed(range(idxL, idxR)):
                n = nums[i]
                if needToVisitCopy[n]:
                    dc -= 1
                    needToVisitCopy[n] = False
                if needToVisit[n] and dc == 0 and n <= smallest:
                    smallest = n
                    idxL = i + 1
            res.append(smallest)
            needToVisit[smallest] = False

        return ''.join([chr(n + ord('a')) for n in res])


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(
        str(Solution().removeDuplicateLetters(
            "tknvntfipavdqjiyslpdlokuymbutpynnxqekoktlqzrhoyvbewklzuamhwtqygsiakymyqwqiqtouynaiowwf"
        )))
    print(str(Solution().removeDuplicateLetters("abacb")))
    print('Example 1:')
    print('Input : ')
    print('s = "bcabc"')
    print('Exception :')
    print('"abc"')
    print('Output :')
    print(str(Solution().removeDuplicateLetters("bcabc")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "cbacdcbc"')
    print('Exception :')
    print('"acdb"')
    print('Output :')
    print(str(Solution().removeDuplicateLetters("cbacdcbc")))
    print()

    pass
# @lc main=end