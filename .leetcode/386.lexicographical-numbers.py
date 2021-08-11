# @lc app=leetcode id=386 lang=python3
#
# [386] Lexicographical Numbers
#
# https://leetcode.com/problems/lexicographical-numbers/description/
#
# algorithms
# Medium (55.77%)
# Likes:    867
# Dislikes: 102
# Total Accepted:    69.8K
# Total Submissions: 124.6K
# Testcase Example:  '13'
#
# Given an integer n, return all the numbers in the range [1, n] sorted in
# lexicographical order.
#
# You must write an algorithm that runs in O(n) time and uses O(1) extra
# space.
#
#
# Example 1:
# Input: n = 13
# Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
# Example 2:
# Input: n = 2
# Output: [1,2]
#
#
# Constraints:
#
#
# 1 <= n <= 5 * 10^4
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定n，将1-n以字典序排列。
# 优先级：加0，尾数加一，尾数为9时退位。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        i = 1
        n = n + 1
        res = []
        while True:
            res.append(i)
            f = False
            if i * 10 < n:
                i = i * 10
            elif i % 10 < 9:
                if i + 1 < n:
                    i += 1
                else:
                    f = True
            elif i % 10 == 9:
                f = True
            else:
                break
            if f:
                i = i // 10
                while i % 10 == 9:
                    i = i // 10
                i = i + 1
                if i == 1:
                    break
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().lexicalOrder(133)))
    print(str(Solution().lexicalOrder(1345)))
    print(str(Solution().lexicalOrder(1367)))
    print('Example 1:')
    print('Input : ')
    print('n = 13')
    print('Exception :')
    print('[1,10,11,12,13,2,3,4,5,6,7,8,9]')
    print('Output :')
    print(str(Solution().lexicalOrder(13)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 2')
    print('Exception :')
    print('[1,2]')
    print('Output :')
    print(str(Solution().lexicalOrder(2)))
    print()

    pass
# @lc main=end