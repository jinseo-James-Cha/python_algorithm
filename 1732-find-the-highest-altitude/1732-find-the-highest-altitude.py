class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # road trip n + 1 altitudes
        # start 0 and altitude 0

        # gain[i] -> net gain in altitude between i and i + 1

        #              gain= [-5,1,5,0,-7]
        # The altitudes are [0,-5,-4,1,1,-6]

        # prefix + 0(1) space
        max_altitude = curr_altitude = 0
        for g in gain:
            curr_altitude += g
            max_altitude = max(max_altitude, curr_altitude)
        return max_altitude


        # prefix
        altitudes = [0]
        for g in gain:
            altitudes.append(g + altitudes[-1])
        
        return max(altitudes)