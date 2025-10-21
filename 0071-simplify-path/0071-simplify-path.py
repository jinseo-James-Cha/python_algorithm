class Solution:
    def simplifyPath(self, path: str) -> str:
        # begins with -> /
        # current dir -> .
        # previous dir -> ..
        # //, /// -> /

        rules = {'.', '..'}
        path_list = path.split('/')
        res_list = []

        for p in path_list:
            if p == "..":
                if res_list:
                    res_list.pop()
            elif p == "." or not p:
                continue
            else:
                res_list.append(p)
        
        res = "/" + "/".join(res_list)
        return res

