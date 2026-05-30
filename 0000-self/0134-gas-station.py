"""
Description: There are $n$ gas stations along a circular route, 
where the amount of gas at the $i$-th station is gas[i]. 
You have a car with an unlimited gas tank and 
it costs cost[i] of gas to travel from the $i$-th station to its next $(i + 1)$-th station. 
You begin the journey with an empty tank at one of the gas stations.
 Given two integer arrays gas and cost, 
 return the starting gas station's index 
 if you can travel around the circuit once in the clockwise direction, otherwise return -1.  

Example:
Input: gas = [1,2,3,4,5], 
cost = [3,4,5,1,2]
Output: 3
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return - 1
        
        start = tank = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            if tank < 0:
                start = i + 1
                tank = 0
        return start