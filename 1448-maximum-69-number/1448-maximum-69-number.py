class Solution:
    def maximum69Number (self, num: int) -> int:
        # find where is the lastest 6 
        latest_location_for_six = -1
        
        i = 0
        dummy_num = num
        while dummy_num > 0:
            remainder = dummy_num % 10
            if remainder == 6:
                latest_location_for_six = i
            dummy_num //= 10
            i += 1
        
        if latest_location_for_six > -1:
            num += 3 * 10**latest_location_for_six 
        return num