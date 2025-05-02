# I wanted to get the minimun length word first
# and loop the word  - i for all string, but...
# its anyway O(N^2)...

# so back to the simplest anwer..check first letter ..to the end

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = 200
        min_str = ""
        for i in range(len(strs)):
            if len(strs[i]) < min_len:
                min_len = len(strs[i])
                min_str = strs[i]

        answer = ""
        for i in range(min_len):
            flag = True
            for s in strs: 
                if not min_str[i] in s or s[i] != min_str[i]:
                    flag = False
                    break
            if flag:
                answer += min_str[i]
            else:
                break
        
        return answer

        # answer = ""
        # for i range(min_length,0,-1):
        #     for j in range(len(strs) - 1):
        #         if strs[j][i] != strs[j+1][i]:
        #             break

        
        


        