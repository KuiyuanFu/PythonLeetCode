# @lc app=leetcode id=929 lang=python3
#
# [929] Unique Email Addresses
#
# https://leetcode.com/problems/unique-email-addresses/description/
#
# algorithms
# Easy (67.29%)
# Likes:    1798
# Dislikes: 245
# Total Accepted:    361K
# Total Submissions: 536.4K
# Testcase Example:  '["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]'
#
# Every valid email consists of a local name and a domain name, separated by
# the '@' sign. Besides lowercase letters, the email may contain one or more
# '.' or '+'.
#
#
# For example, in "alice@leetcode.com", "alice" is the local name, and
# "leetcode.com" is the domain name.
#
#
# If you add periods '.' between some characters in the local name part of an
# email address, mail sent there will be forwarded to the same address without
# dots in the local name. Note that this rule does not apply to domain
# names.
#
#
# For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the
# same email address.
#
#
# If you add a plus '+' in the local name, everything after the first plus sign
# will be ignored. This allows certain emails to be filtered. Note that this
# rule does not apply to domain names.
#
#
# For example, "m.y+name@email.com" will be forwarded to "my@email.com".
#
#
# It is possible to use both of these rules at the same time.
#
# Given an array of strings emails where we send one email to each emails[i],
# return the number of different addresses that actually receive mails.
#
#
# Example 1:
#
#
# Input: emails =
# ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually
# receive mails.
#
#
# Example 2:
#
#
# Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
# Output: 3
#
#
#
# Constraints:
#
#
# 1 <= emails.length <= 100
# 1 <= emails[i].length <= 100
# emails[i] consist of lowercase English letters, '+', '.' and '@'.
# Each emails[i] contains exactly one '@' character.
# All local and domain names are non-empty.
# Local names do not start with a '+' character.
# Domain names end with the ".com" suffix.
#
#
#

# @lc tags=string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 整理邮箱地址。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()

        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            email = local + '@' + domain
            res.add(email)
        return len(res)

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'emails =["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]'
    )
    print('Exception :')
    print('2')
    print('Output :')
    print(
        str(Solution().numUniqueEmails([
            "test.email+alex@leetcode.com",
            "test.e.mail+bob.cathy@leetcode.com",
            "testemail+david@lee.tcode.com"
        ])))
    print()

    print('Example 2:')
    print('Input : ')
    print('emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]')
    print('Exception :')
    print('3')
    print('Output :')
    print(
        str(Solution().numUniqueEmails(
            ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"])))
    print()

    pass
# @lc main=end