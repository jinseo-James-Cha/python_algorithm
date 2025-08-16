class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # 4 leds on top , hours, 0 ~ 11(not 1 - 12)
        # 8 4 2 1

        # 6 leds on bottom, minutes, 0 ~ 59(not 1 - 60)
        # 32 16 8 4 2 1

        res = []

        for h in range(12):
            for m in range(60):
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    res.append(f"{h}:{m:02d}")
        return res
        





