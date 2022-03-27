# @lc app=leetcode id=860 lang=python3
#
# [860] Lemonade Change
#
# https://leetcode.com/problems/lemonade-change/description/
#
# algorithms
# Easy (52.31%)
# Likes:    1166
# Dislikes: 119
# Total Accepted:    92.8K
# Total Submissions: 177.2K
# Testcase Example:  '[5,5,5,10,20]'
#
# At a lemonade stand, each lemonade costs $5. Customers are standing in a
# queue to buy from you and order one at a time (in the order specified by
# bills). Each customer will only buy one lemonade and pay with either a $5,
# $10, or $20 bill. You must provide the correct change to each customer so
# that the net transaction is that the customer pays $5.
#
# Note that you do not have any change in hand at first.
#
# Given an integer array bills where bills[i] is the bill the i^th customer
# pays, return true if you can provide every customer with the correct change,
# or false otherwise.
#
#
# Example 1:
#
#
# Input: bills = [5,5,5,10,20]
# Output: true
# Explanation:
# From the first 3 customers, we collect three $5 bills in order.
# From the fourth customer, we collect a $10 bill and give back a $5.
# From the fifth customer, we give a $10 bill and a $5 bill.
# Since all customers got correct change, we output true.
#
#
# Example 2:
#
#
# Input: bills = [5,5,10,10,20]
# Output: false
# Explanation:
# From the first two customers in order, we collect two $5 bills.
# For the next two customers in order, we collect a $10 bill and give back a $5
# bill.
# For the last customer, we can not give the change of $15 back because we only
# have two $10 bills.
# Since not every customer received the correct change, the answer is
# false.
#
#
#
# Constraints:
#
#
# 1 <= bills.length <= 10^5
# bills[i] is either 5, 10, or 20.
#
#
#

# @lc tags=design;queue

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 找零
# 只能用顾客给的钱。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        n5 = 0
        n10 = 0

        for b in bills:
            if b == 5:
                n5 += 1
            elif b == 10:
                if n5 == 0:
                    return False
                n5 -= 1
                n10 += 1
            else:
                if n10 > 0 and n5 > 0:
                    n5 -= 1
                    n10 -= 1
                elif n5 >= 3:
                    n5 -= 3
                else:
                    return False
        return True

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('bills = [5,5,5,10,20]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().lemonadeChange([5, 5, 5, 10, 20])))
    print()

    print('Example 2:')
    print('Input : ')
    print('bills = [5,5,10,10,20]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().lemonadeChange([5, 5, 10, 10, 20])))
    print()

    pass
# @lc main=end