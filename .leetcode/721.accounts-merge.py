# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#
# https://leetcode.com/problems/accounts-merge/description/
#
# algorithms
# Medium (53.56%)
# Likes:    3087
# Dislikes: 573
# Total Accepted:    184.5K
# Total Submissions: 340.9K
# Testcase Example:  '[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]'
#
# Given a list of accounts where each element accounts[i] is a list of strings,
# where the first element accounts[i][0] is a name, and the rest of the
# elements are emails representing emails of the account.
#
# Now, we would like to merge these accounts. Two accounts definitely belong to
# the same person if there is some common email to both accounts. Note that
# even if two accounts have the same name, they may belong to different people
# as people could have the same name. A person can have any number of accounts
# initially, but all of their accounts definitely have the same name.
#
# After merging the accounts, return the accounts in the following format: the
# first element of each account is the name, and the rest of the elements are
# emails in sorted order. The accounts themselves can be returned in any
# order.
#
#
# Example 1:
#
#
# Input: accounts =
# [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Output:
# [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Explanation:
# The first and second John's are the same person as they have the common email
# "johnsmith@mail.com".
# The third John and Mary are different people as none of their email addresses
# are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary',
# 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']]
# would still be accepted.
#
#
# Example 2:
#
#
# Input: accounts =
# [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
# Output:
# [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
#
#
#
# Constraints:
#
#
# 1 <= accounts.length <= 1000
# 2 <= accounts[i].length <= 10
# 1 <= accounts[i][j] <= 30
# accounts[i][0] consists of English letters.
# accounts[i][j] (for j > 0) is a valid email.
#
#
#

# @lc tags=depth-first-search;union-find

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 合并账户，以邮箱为准。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        mailToIdx = {}
        names = []
        mails = []
        for account in accounts:
            name = account[0]
            idx = None
            for i in range(1, len(account)):
                mail = account[i]
                if mail in mailToIdx:
                    if idx is None:
                        idx = mailToIdx[mail]
                    else:
                        idxOld = mailToIdx[mail]
                        if idx != idxOld:
                            names[idxOld] = None
                            for m in mails[idxOld]:
                                mails[idx].add(m)
                                mailToIdx[m] = idx

            if idx == None:
                idx = len(names)
                names.append(name)
                mails.append(set())
            s = mails[idx]
            for i in range(1, len(account)):
                mail = account[i]
                mailToIdx[mail] = idx
                s.add(mail)
        res = []
        for i in range(len(mails)):
            if names[i] != None:
                res.append([names[i]] + sorted(list(mails[i])))

        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'accounts =[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]'
    )
    print('Exception :')
    print(
        '[["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]'
    )
    print('Output :')
    print(
        str(Solution().accountsMerge(
            [["John", "johnsmith@mail.com", "john_newyork@mail.com"],
             ["John", "johnsmith@mail.com", "john00@mail.com"],
             ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]])))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'accounts =[["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]'
    )
    print('Exception :')
    print(
        '[["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]'
    )
    print('Output :')
    print(
        str(Solution().accountsMerge(
            [["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
             ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
             ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
             ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
             ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]])))
    print()
    print(
        str(Solution().accountsMerge(
            [["Alex", "Alex5@m.co", "Alex4@m.co", "Alex0@m.co"],
             ["Ethan", "Ethan3@m.co", "Ethan3@m.co", "Ethan0@m.co"],
             ["Kevin", "Kevin4@m.co", "Kevin2@m.co", "Kevin2@m.co"],
             ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe2@m.co"],
             ["Gabe", "Gabe3@m.co", "Gabe4@m.co", "Gabe2@m.co"]])))
    print()
    print(
        str(Solution().accountsMerge([["David", "David0@m.co", "David1@m.co"],
                                      ["David", "David3@m.co", "David4@m.co"],
                                      ["David", "David4@m.co", "David5@m.co"],
                                      ["David", "David2@m.co", "David3@m.co"],
                                      ["David", "David1@m.co",
                                       "David2@m.co"]])))
    print()
    pass
# @lc main=end