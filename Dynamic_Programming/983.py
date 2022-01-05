# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 11:32:32 2022

@author: Lenovo

"""

def mincostTickets( days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """

        days = [day-days[0] for day in days]
        dp = [-1]*(days[-1]-days[0]+1)
        dp[0] = min(costs)
        for i in range(1, len(dp)):
            if i not in days:
                dp[i] = dp[i-1]
            else:
                if i >= 30:
                    dp[i] = min(dp[i-1]+costs[0],dp[i-7]+costs[1],dp[i-30]+costs[2])
                elif i>=7:
                    dp[i] = min(dp[i-1]+costs[0],dp[i-7]+costs[1],costs[2])
                else:
                    dp[i] = min(dp[i-1]+costs[0],costs[1])
                    
        return dp[-1]


def mincostTickets( days, costs):
    
    

days = [1,2,3,4,6,8,9,10,13,14,16,17,19,21,24,26,27,28,29]
costs = [3,14,50]

output = mincostTickets( days, costs)

                    
            
            
            