class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # answer[i] == the number of days you have to wait for a warmer temp
        # default 0

        """
        [73,74,75,71,69,72,76,73]
        stack value is the temperatures..
        answer is the index..
        like i < j and temp[i] < temp[j]
        answer[i] = j - i
        """
        n = len(temperatures)
        answer = [0] * n
        stack = []
        for curr_day, curr_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop() # found i
                answer[prev_day] = curr_day - prev_day
            stack.append(curr_day)
        return answer




        




        answer = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)-1, -1, -1):
            days = 0
            while stack and stack[-1] < temperatures[i]:
                days += 1
                stack.pop()
            
            # there is something is warmer than current temp
            if stack:
                if temperatures[i] > temperatures[i+1]:
                    answer[i] = days + answer[i+1]
                else:
                    answer[i] = 1
            stack.append(temperatures[i])
        return answer




        # answer = [0] * len(temperatures)
        # stack = []
        # for i in range(len(temperature)-1, -1, -1):
        #     if stack:
        #         if stack[-1] > temperature[i]:
        #             answer[i] = 1
        #             stack.append(temperature[i])
        #         else:
        #             days = 1
        #             while stack and stack[-1] < temperature[i]:
        #                 days += 1
        #                 stack.pop()
        #             if not stack:
        #                 answer[i] = 0
        #             else:
        #                 answer[i] = days
        #             stack.append(temperature[i])
        #     else:
        #         answer[i] = 0
        #         stack.append(temperature)
            