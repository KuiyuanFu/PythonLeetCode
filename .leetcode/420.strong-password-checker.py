# @lc app=leetcode id=420 lang=python3
#
# [420] Strong Password Checker
#
# https://leetcode.com/problems/strong-password-checker/description/
#
# algorithms
# Hard (13.76%)
# Likes:    380
# Dislikes: 1085
# Total Accepted:    20.4K
# Total Submissions: 147.7K
# Testcase Example:  '"a"'
#
# A password is considered strong if the below conditions are all met:
#
#
# It has at least 6 characters and at most 20 characters.
# It contains at least one lowercase letter, at least one uppercase letter, and
# at least one digit.
# It does not contain three repeating characters in a row (i.e., "...aaa..." is
# weak, but "...aa...a..." is strong, assuming other conditions are met).
#
#
# Given a string password, return the minimum number of steps required to make
# password strong. if password is already strong, return 0.
#
# In one step, you can:
#
#
# Insert one character to password,
# Delete one character from password, or
# Replace one character of password with another character.
#
#
#
# Example 1:
# Input: password = "a"
# Output: 5
# Example 2:
# Input: password = "aA1"
# Output: 3
# Example 3:
# Input: password = "1337C0d3"
# Output: 0
#
#
# Constraints:
#
#
# 1 <= password.length <= 50
# password consists of letters, digits, dot '.' or exclamation mark '!'.
#
#
#

# @lc tags=Unknown

# @lc imports=start
import builtins
from imports import *

# @lc imports=end

# @lc idea=start
#
# 将一个密码转换为强密码的最小步骤。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def strongPasswordChecker(self, password: str) -> int:

        buffer = [False] * 3
        for p in password:
            if '0' <= p <= '9':
                buffer[0] = True
            if 'a' <= p <= 'z':
                buffer[1] = True
            if 'A' <= p <= 'Z':
                buffer[2] = True
        # 缺少的类型数
        types = buffer.count(False)
        # 多余的长度
        needDeletes = max(0, len(password) - 20)
        # 缺少的长度
        needAdds = max(0, 6 - len(password))
        # 如果需要添加，那么就可以添加缺少的类型
        types = max(0, types - needAdds)

        pre = ''
        password += ' '
        l = 0

        buffer = [0] * 3
        # 计算各个类型的数量
        for p in password:
            if p == pre:
                l += 1
            else:
                if l >= 3:
                    # 需要多少个替换
                    buffer[2] += l // 3
                    # 一个删除就可以抵得上一个替换
                    if l % 3 == 0:
                        buffer[0] += 1
                    # 两个删除才能抵得上一个替换
                    elif l % 3 == 1:
                        buffer[1] += 1
                l = 1
            pre = p
        steps = 0

        for i in range(3):

            c = min(needDeletes // (i + 1), buffer[i])
            needDeletes -= c * (i + 1)
            buffer[2] -= c
            steps += c * (i + 1)

        steps += needDeletes
        if needAdds:
            steps += needAdds
            # 去掉一个添加后，需要的替换数
            buffer[2] = max(0, buffer[2] - needAdds)
        # 替换也可以减少类型缺少数
        steps += max(buffer[2], types)

        return steps
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().strongPasswordChecker("bbaaaaaaaaaaaaaaacccccc")))
    print('Example 1:')
    print('Input : ')
    print('password = "a"')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().strongPasswordChecker("a")))
    print()

    print('Example 2:')
    print('Input : ')
    print('password = "aA1"')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().strongPasswordChecker("aA1")))
    print()

    print('Example 3:')
    print('Input : ')
    print('password = "1337C0d3"')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().strongPasswordChecker("1337C0d3")))
    print()

    pass
# @lc main=end