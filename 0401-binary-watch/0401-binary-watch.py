class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # 4 leds on top , hours, 0 ~ 11(not 1 - 12)
        # 8 4 2 1

        # 6 leds on bottom, minutes, 0 ~ 59(not 1 - 60)
        # 32 16 8 4 2 1

        # question
        # top light on + bottom light on == turnedOn
        # calculate with binary number of time and convert to time format
        
        # key points
        # 1. int -> binary
        # bin(integer) -> "0b"+binary number for the integer
        # bin(1) -> 0b1
        # bin(-5) -> -0b101
        # 2. int -> time str formating
        # f"{h}:{m:02d}"
        # {m:02d} m formating with 2digits, if not fill with 0

        res = []
        for h in range(12):
            for m in range(60):
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    res.append(f"{h}:{m:02d}")
        return res
        





