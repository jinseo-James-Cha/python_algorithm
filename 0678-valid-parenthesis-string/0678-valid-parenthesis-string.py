class Solution:
    def checkValidString(self, s: str) -> bool:
        # ( ) *
        # the key point is *
        # * can be ( ) or ""
        # extra * is ok
        # () -> true
        # (*)) -> (()) 1 1 -1 -1
        # ((*) -> (()) 1 1 -1 -1
        # (**) -> () 1 0 0 1
        # if * shows up before half, it works as ( ? no
        # ()()(*)
        open_stack = []
        wildcard_stack = []
        for i, ch in enumerate(s):
            if ch == "(":
                open_stack.append(i)
            elif ch == "*":
                wildcard_stack.append(i)
            else:
                # if ch == ")"
                # use open as priority
                if open_stack:
                    open_stack.pop()
                elif wildcard_stack:
                    wildcard_stack.pop()
                else:
                    return False

        # use wildcard as )
        while open_stack and wildcard_stack:
            if open_stack.pop() > wildcard_stack.pop():
                return False
        
        return not open_stack
