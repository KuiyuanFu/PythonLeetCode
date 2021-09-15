# @lc app=leetcode id=468 lang=python3
#
# [468] Validate IP Address
#
# https://leetcode.com/problems/validate-ip-address/description/
#
# algorithms
# Medium (25.61%)
# Likes:    557
# Dislikes: 2155
# Total Accepted:    109.5K
# Total Submissions: 426.8K
# Testcase Example:  '"172.16.254.1"'
#
# Given a string IP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP
# is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.
#
# A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255
# and xi cannot contain leading zeros. For example, "192.168.1.1" and
# "192.168.1.0" are valid IPv4 addresses but "192.168.01.1", while
# "192.168.1.00" and "192.168@1.1" are invalid IPv4 addresses.
#
# A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8"
# where:
#
#
# 1 <= xi.length <= 4
# xi is a hexadecimal string which may contain digits, lower-case English
# letter ('a' to 'f') and upper-case English letters ('A' to 'F').
# Leading zeros are allowed in xi.
#
#
# For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and
# "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses, while
# "2001:0db8:85a3::8A2E:037j:7334" and
# "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.
#
#
# Example 1:
#
#
# Input: IP = "172.16.254.1"
# Output: "IPv4"
# Explanation: This is a valid IPv4 address, return "IPv4".
#
#
# Example 2:
#
#
# Input: IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
# Output: "IPv6"
# Explanation: This is a valid IPv6 address, return "IPv6".
#
#
# Example 3:
#
#
# Input: IP = "256.256.256.256"
# Output: "Neither"
# Explanation: This is neither a IPv4 address nor a IPv6 address.
#
#
# Example 4:
#
#
# Input: IP = "2001:0db8:85a3:0:0:8A2E:0370:7334:"
# Output: "Neither"
#
#
# Example 5:
#
#
# Input: IP = "1e1.4.5.6"
# Output: "Neither"
#
#
#
# Constraints:
#
#
# IP consists only of English letters, digits and the characters '.' and ':'.
#
#
#

# @lc tags=string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断是否是合法的IP地址。
# 分段，依次判断。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def validIPAddress(self, IP: str) -> str:
        hs = set('1234567890abcdefABCDEF')

        def v4():
            ss = IP.split('.')
            if len(ss) != 4:
                return False
            for s in ss:

                if not s.isdigit():
                    return False
                i = int(s)
                if not 0 <= i <= 255:
                    return False
                if len(s) != 1 and s[0] == '0':
                    return False

            return True

        def v6():
            ss = IP.split(':')
            if len(ss) != 8:
                return False
            for s in ss:
                if not 0 < len(s) <= 4:
                    return False
                for c in s:
                    if c not in hs:
                        return False
            return True

        if '.' in IP and v4():
            return 'IPv4'
        elif ':' in IP and v6():
            return 'IPv6'
        else:
            return 'Neither'
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('IP = "172.16.254.1"')
    print('Exception :')
    print('"IPv4"')
    print('Output :')
    print(str(Solution().validIPAddress("172.16.254.1")))
    print()

    print('Example 2:')
    print('Input : ')
    print('IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"')
    print('Exception :')
    print('"IPv6"')
    print('Output :')
    print(str(Solution().validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334")))
    print()

    print('Example 3:')
    print('Input : ')
    print('IP = "256.256.256.256"')
    print('Exception :')
    print('"Neither"')
    print('Output :')
    print(str(Solution().validIPAddress("256.256.256.256")))
    print()

    print('Example 4:')
    print('Input : ')
    print('IP = "2001:0db8:85a3:0:0:8A2E:0370:7334:"')
    print('Exception :')
    print('"Neither"')
    print('Output :')
    print(str(Solution().validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334:")))
    print()

    print('Example 5:')
    print('Input : ')
    print('IP = "1e1.4.5.6"')
    print('Exception :')
    print('"Neither"')
    print('Output :')
    print(str(Solution().validIPAddress("1e1.4.5.6")))
    print()
    print(str(Solution().validIPAddress("01.01.01.01")))
    pass
# @lc main=end