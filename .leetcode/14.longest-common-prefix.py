# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (36.20%)
# Likes:    3969
# Dislikes: 2195
# Total Accepted:    993.7K
# Total Submissions: 2.7M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# 
# Example 1:
# 
# 
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.
# 
# 
#

# @lc tags=string

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 最长公共前缀，直接遍历就可以了。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 :
            return ''
        length = min ( [len(s) for s in strs])
        for i in range(length):
            c = strs[0][i]
            for j in range(1,len(strs)):
                if strs[j][i] != c:
                    return strs[0][:i]
        return strs[0][:length]

        
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('strs = ["flower","flow","flight"]')
    print('Output :')
    print(str(Solution().longestCommonPrefix(["flower","flow","flight"])))
    print('Exception :')
    print('"fl"')
    print()
    
    print('Example 2:')
    print('Input : ')
    print('strs = ["dog","racecar","car"]')
    print('Output :')
    print(str(Solution().longestCommonPrefix(["dog","racecar","car"])))
    print('Exception :')
    print('""')
    print()
    
    pass
# @lc main=end