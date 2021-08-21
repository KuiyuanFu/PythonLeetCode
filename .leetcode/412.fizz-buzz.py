# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#
# https://leetcode.com/problems/fizz-buzz/description/
#
# algorithms
# Easy (64.60%)
# Likes:    1519
# Dislikes: 1700
# Total Accepted:    509.9K
# Total Submissions: 786.6K
# Testcase Example:  '3'
#
# Given an integer n, return a string array answer (1-indexed) where:
#
#
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i if non of the above conditions are true.
#
#
#
# Example 1:
# Input: n = 3
# Output: ["1","2","Fizz"]
# Example 2:
# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]
# Example 3:
# Input: n = 15
# Output:
# ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
#
#
# Constraints:
#
#
# 1 <= n <= 10^4
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 根据索引设置值。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        res = [str(i) for i in range(1, n + 1)]
        f, b, fb = "Fizz", 'Buzz', 'FizzBuzz'
        for i in range(2, n, 3):
            res[i] = f
        for i in range(4, n, 5):
            res[i] = b
        for i in range(14, n, 15):
            res[i] = fb
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 3')
    print('Exception :')
    print('["1","2","Fizz"]')
    print('Output :')
    print(str(Solution().fizzBuzz(3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 5')
    print('Exception :')
    print('["1","2","Fizz","4","Buzz"]')
    print('Output :')
    print(str(Solution().fizzBuzz(5)))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 15')
    print('Exception :')
    print(
        '["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]'
    )
    print('Output :')
    print(str(Solution().fizzBuzz(15)))
    print()

    pass
# @lc main=end