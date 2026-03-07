class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        Optimise idea: Greedy
        
        3 30 34 5 9
        compare the leftmost number
        if leftmost is greater, it should be the front

        3 30 34 5 9
        3 3  3  5 9 -> 9 pop

        3 30 34 5
        3 3  3  5 -> 5 pop
        
        3 30 34 
        3 3  3 -> all the same
           0  4 -> 34 pop
        
        3 30
        3 3 -> all the smae
        x  0 -> 3 pop 
        """

        # int -> str and reverse order -> and join them all
        # .sort() -> o(n log n)
        # time complexity = o(n log n)
        s_num = []
        for num in nums:
            s_num.append(str(num))

        s_num.sort(key=lambda x: x * 10, reverse=True) # 3, 30 compare as 30 and 300

        # edge case [0, 0]
        if s_num[0] == "0":
            return "0"

        return "".join(s_num)

        """
        brute force -> backtracking -> TLE
        intuitive solution
        backtrack checking all combination and return the largest
        """
        def backtrack(curr, used):
            nonlocal largest
            if len(used) == len(nums):
                largest = max(largest, int("".join(curr)))
            
            for i in range(len(nums)):
                if i not in used:
                    curr.append(str(nums[i]))
                    used.add(i)
                    
                    backtrack(curr, used)

                    curr.pop()
                    used.remove(i)
        largest = 0
        backtrack([], set())
        return str(largest)

