class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        key_map = {}
        i = ord('a')
        for k in key:
            if k == " ":
                continue
            
            if k in key_map:
                continue

            key_map[k] = chr(i)
            i += 1

        res = ""
        for m in message:
            if m == " ":
                res += " "
            else:
                res += key_map[m]
        return res
