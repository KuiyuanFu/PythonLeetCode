# @lc app=leetcode id=815 lang=python3
#
# [815] Bus Routes
#


# @lc tags=Unknown

# @lc imports=start

from imports import *
# @lc imports=end

# @lc idea=start
# 
# 公交线路，最少搭乘次数。
# 直接遍历。
# 
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        siteToRoutes = {}
        for routeIdx,  route in enumerate( routes):
            for site in route:
                if site not in siteToRoutes:
                    siteToRoutes[site] =[]
                siteToRoutes[site].append(routeIdx)

        res = 0

        visitedSites = set()
        nowSites = set([source])
        while len(nowSites) != 0:
            if target in nowSites:
                return res
            res += 1
            nextRouteIdxs =set()
            for site in nowSites:
                if site in siteToRoutes:
                    nextRouteIdxs.update(siteToRoutes[site])
                
            nextSites = set()
            for routeIdx in nextRouteIdxs:
                nextSites.update(routes[routeIdx])
            visitedSites.update(nowSites)
            nextSites.difference_update(visitedSites)
            nowSites = nextSites

        return -1

        pass

        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('routes = [[1,2,7],[3,6,7]], source = 1, target = 6')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().numBusesToDestination([[1,2,7],[3,6,7]],1,6)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target= 12')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().numBusesToDestination([[7,12],[4,5,15],[6],[15,19],[9,12,13]],15,12)))
    print()
    
    pass
# @lc main=end