class Solution:
    def lengthLongestPath(self, input: str) -> int:
        # dir root
        #   subdir
        #   subdir
        
        
        # how many dot . -> file number?
        # file directory search .... dfs and check max
        # get all absolute path for all files
        # and return max(all_paths)
        """
        Input: input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
        levels = [dir, \tsubdir1, \tsubdir2, \t\tfile.ext]
        """
        depth_map = {0:0}
        max_len = 0

        levels = input.split('\n')
        for level in levels: # dir \tsubdir1 \tsubdir2 \t\tfile.ext
            name = level.lstrip('\t') # dir -> \t subdir
            depth = len(level) - len(name) # 전체 길이 - 이름 길이 = 탭의 개수(깊이) \tsubdir - subdir = 1 because \t is one ch

            # file case
            if "." in name:
                length = depth_map[depth] + len(name)
                max_len = max(max_len, length)
            else:
                # dir case
                depth_map[depth + 1] = depth_map[depth] + len(name) + 1 # + 1 for / about every depth
        return max_len