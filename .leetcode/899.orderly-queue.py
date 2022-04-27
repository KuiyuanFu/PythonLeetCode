# @lc app=leetcode id=899 lang=python3
#
# [899] Orderly Queue
#
# https://leetcode.com/problems/orderly-queue/description/
#
# algorithms
# Hard (58.52%)
# Likes:    558
# Dislikes: 355
# Total Accepted:    25.8K
# Total Submissions: 44K
# Testcase Example:  '"cba"\n1'
#
# You are given a string s and an integer k. You can choose one of the first k
# letters of s and append it at the end of the string..
#
# Return the lexicographically smallest string you could have after applying
# the mentioned step any number of moves.
#
#
# Example 1:
#
#
# Input: s = "cba", k = 1
# Output: "acb"
# Explanation:
# In the first move, we move the 1^st character 'c' to the end, obtaining the
# string "bac".
# In the second move, we move the 1^st character 'b' to the end, obtaining the
# final result "acb".
#
#
# Example 2:
#
#
# Input: s = "baaca", k = 3
# Output: "aaabc"
# Explanation:
# In the first move, we move the 1^st character 'b' to the end, obtaining the
# string "aacab".
# In the second move, we move the 3^rd character 'c' to the end, obtaining the
# final result "aaabc".
#
#
#
# Constraints:
#
#
# 1 <= k <= s.length <= 1000
# s consist of lowercase English letters.
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定字符串与一个k，每一步可以选择当前字符串前k个字符中的一个，放在末尾，形成新字符串。求任意步后，字典序最小的结果。
# 如果k为1，那么就只能是一个简单旋转。
# 如果k大于1，那么就可以任意排序了。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            length = len(s)
            res = s
            ss = s + s
            for i in range(length):
                res = min(res, ss[i:i + length])
            return res
        else:
            return ''.join(sorted(list(s)))

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "cba", k = 1')
    print('Exception :')
    print('"acb"')
    print('Output :')
    print(str(Solution().orderlyQueue("cba", 1)))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "baaca", k = 3')
    print('Exception :')
    print('"aaabc"')
    print('Output :')
    print(str(Solution().orderlyQueue("baaca", 3)))
    print()

    pass
# @lc main=end