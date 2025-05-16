class Solution:
    def reverse(self, x: int) -> int:
        # using % and muliple by 10 for each loop?
        answer = 0
        is_x_negative = x < 0
        x = abs(x) 
        while x > 0:
            if (answer * 10) + (x % 10) > 2**31 - 1:
                return 0
            elif ((answer * 10) + (x % 10)) * -1 <= 2**31 * -1:
                return 0

            answer *= 10 # answer = answer * 10
            answer += x % 10 # answer = answer + x % 10
            x //= 10

        return answer * -1 if is_x_negative else answer