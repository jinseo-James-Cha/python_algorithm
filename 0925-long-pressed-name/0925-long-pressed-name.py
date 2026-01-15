class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_idx = 0
        typed_idx = 0

        while name_idx < len(name) and typed_idx < len(typed):
            if name[name_idx] == typed[typed_idx]:
                name_idx += 1
                typed_idx += 1
            elif typed_idx > 0 and typed[typed_idx] == typed[typed_idx-1]:
                typed_idx += 1
            else:
                return False
        
        if name_idx != len(name):
            return False
        
        while typed_idx < len(typed):
            if typed[typed_idx] != typed[typed_idx-1]:
                return False
            typed_idx += 1
        
        return True