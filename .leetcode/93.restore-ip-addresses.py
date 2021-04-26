# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#
# https://leetcode.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (37.95%)
# Likes:    1746
# Dislikes: 560
# Total Accepted:    233.2K
# Total Submissions: 613.5K
# Testcase Example:  '"25525511135"'
#
# Given a string s containing only digits, return all possible valid IP
# addresses that can be obtained from s. You can return them in any order.
#
# A valid IP address consists of exactly four integers, each integer is between
# 0 and 255, separated by single dots and cannot have leading zeros. For
# example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and
# "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP
# addresses.
#
#
# Example 1:
# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]
# Example 2:
# Input: s = "0000"
# Output: ["0.0.0.0"]
# Example 3:
# Input: s = "1111"
# Output: ["1.1.1.1"]
# Example 4:
# Input: s = "010010"
# Output: ["0.10.0.10","0.100.1.0"]
# Example 5:
# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
#
#
# Constraints:
#
#
# 0 <= s.length <= 3000
# s consists of digits only.
#
#
#

# @lc tags=string;backtracking

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个字符串s，其是一个合法的IP地址的十进制表示，没有点，求所有合法的点分十进制的解释。
# 递归算法，一共四位，在每一位上，都是读取所有可能取值，把剩下的部分传给下一位的解释函数。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.results = []
        self.s = s
        self.buff = [""] * 4
        self.recur(0, 0)
        return self.results
        pass

    def recur(self, i, l):
        if l >= len(self.s):
            return 0

        if i == 3:
            if self.valid(self.s[l:]):
                self.buff[i] = self.s[l:]
                self.results.append('.'.join(self.buff))
        else:
            rMin = len(self.s) - (3 - i) * 3
            rMin = max(l + 1, rMin)
            for r in range(rMin, l + 4):
                s = self.s[l:r]
                if self.valid(s):
                    self.buff[i] = s
                    self.recur(i + 1, r)

    def valid(self, s):
        if len(s) == 1:
            return True
        if s[0] == '0':
            return False
        if int(s) > 255:
            return False
        return True


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "25525511135"')
    print('Output :')
    print(str(Solution().restoreIpAddresses("25525511135")))
    print('Exception :')
    print('["255.255.11.135","255.255.111.35"]')
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "0000"')
    print('Output :')
    print(str(Solution().restoreIpAddresses("0000")))
    print('Exception :')
    print('["0.0.0.0"]')
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "1111"')
    print('Output :')
    print(str(Solution().restoreIpAddresses("1111")))
    print('Exception :')
    print('["1.1.1.1"]')
    print()

    print('Example 4:')
    print('Input : ')
    print('s = "010010"')
    print('Output :')
    print(str(Solution().restoreIpAddresses("010010")))
    print('Exception :')
    print('["0.10.0.10","0.100.1.0"]')
    print()

    print('Example 5:')
    print('Input : ')
    print('s = "101023"')
    print('Output :')
    print(str(Solution().restoreIpAddresses("101023")))
    print('Exception :')
    print('["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]')
    print()

    pass
# @lc main=end