# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (31.54%)
# Likes:    13784
# Dislikes: 714
# Total Accepted:    2.1M
# Total Submissions: 6.7M
# Testcase Example:  '"abcabcbb"'
#
# Given a string s, find the length of the longest substring without repeating
# characters.
#
#
# Example 1:
#
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
#
# Example 2:
#
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#
# Example 3:
#
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
#
#
# Example 4:
#
#
# Input: s = ""
# Output: 0
#
#
#
# Constraints:
#
#
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
#
#
#


# @lc tags=hash-table;two-pointers;string;sliding-window

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 目的是求字符串的没有重复字母的最长子字符串，使用左右两个索引变量指示现在子字符串的范围，一个 dic 存储现在子字符串的所有字符及其索引的键值对。
# 每次右移一次右索引，判断新字符是否已经出现过，若出现过，左索引需要移动到上次出现位置的右侧一个位置，同时在 dic 中移除这段中的字符。比较长度。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}

        lMax = 0
        l = 0
        left = 0
        for i, c in enumerate(s):
            if dic.__contains__(c):
                right = dic[c]
                # 将已经移除的部分的字符删除。
                for j in range(left, right):
                    dic.pop(s[j])
                l = i - right
                left = right+1
            else:
                l = l+ 1
            dic[c] = i
            if l > lMax:
                lMax = l
            # print(  l.__str__() + "\t" + lMax.__str__())
        return lMax
        
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "abcabcbb"')
    print('Output :')
    print(str(Solution().lengthOfLongestSubstring("abcabcbb")))
    print('Exception :')
    print('3')
    print()
    
    print('Example 2:')
    print('Input : ')
    print('s = "bbbbb"')
    print('Output :')
    print(str(Solution().lengthOfLongestSubstring("bbbbb")))
    print('Exception :')
    print('1')
    print()
    
    print('Example 3:')
    print('Input : ')
    print('s = "pwwkew"')
    print('Output :')
    print(str(Solution().lengthOfLongestSubstring("pwwkew")))
    print('Exception :')
    print('3')
    print()
    
    print('Example 4:')
    print('Input : ')
    print('s = ""')
    print('Output :')
    print(str(Solution().lengthOfLongestSubstring("")))
    print('Exception :')
    print('0')
    print()
    
    pass
# @lc main=end