class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Sliding Window
        left = 0
        num_whites = 0
        num_recolors = float("inf") # will use min()

        for right in range(len(blocks)):
            if blocks[right] == "W":
                num_whites += 1
            
            if right - left + 1 == k:
                num_recolors = min(num_recolors, num_whites)

                if blocks[left] == "W":
                    num_whites -= 1
                
                left += 1
        return num_recolors


        # blocks[i] == W or B -> white and black
        # k == num of B in a row
        # recolor ONE white block -> black
        # how many recolor operation I need to make K equals to num of B
        
        # WBBWWBBWBW
        # Block -> block for W or B?
        # -1 2 -2 2 -1 1 -1 -> 7
        # L
        # R 
        # I feel like sliding window
        # colors = {"W": -1, "B": 1}
        # groups = []
        # curr_num = colors[blocks[0]]
        # curr_color = blocks[0]
        # for i in range(1, len(blocks)) :
        #     if blocks[i] == curr_color:
        #         curr_num += colors[curr_color]
        #     else:
        #         groups.append(curr_num)
        #         curr_num = 1 * colors[blocks[i]]
        #         curr_color = blocks[i]
        #     # for the last color
        #     if i == len(blocks) - 1:
        #         if groups[-1] > 0 and curr_color == "B":
        #             groups[-1] += 1
        #         else:
        #             groups.append(curr_num)
        
        # # W BB WW BB W B W
        # # [-1, 2, -2, 2, -1, 1, -1]
        # # minimum operations
        # operations = len(groups)
        # cur_o = 0
        # cur_k = 0
        # left = 0
        # for right in range(len(groups)):
        #     if groups[right] >= k:
        #         return 0
        #     else:
        #         # num of B
        #         if groups[right] > 0:
        #             cur_k += groups[right]
        #         # if group for W
        #         else:
        #             cur_o += 1
        #             cur_k += (groups[right] * -1)
        #     if cur_k >= k:
        #         operations = min(cur_o, operations)
        # return operations
                
                    


        

