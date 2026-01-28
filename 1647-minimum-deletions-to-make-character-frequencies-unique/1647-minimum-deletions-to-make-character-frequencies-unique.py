class Solution:
    def minDeletions(self, s: str) -> int:
        """
        s -> good -> if there are no two different character that have the same frequency
        -> unique frequency per character 
        
        return minimum number of deletion


        example
        aab -> a2 b1 -> good

        aaabbbcc -> a3 b3 c2 -> not good -> a-1 and a-1 -> answer 2 deletions

        ceabaacb -> c2e1a3b2 -> c-1 and c-1 => answer 2 deletions



        # count all alphabet
        ceabaacb -> c2e1a3b2
        3 - a
        2 - c b
        e - 1

        if count len > 1 pop

        b count -=1 -> in set 1
        then -1 -> not in set 0 add 0 :b
        total deletion 2


        ceabaacb -> c2e1a3b2
        count
        a - 3
        b - 2
        c - 2
        e - 1

        num_occupied = 1 2 3
        deleting_ch = [c]
        """
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        num_occupied = set()
        deleting_ch = []
        for k, v in count.items():
            if v in num_occupied:
                deleting_ch.append(k) # c
            else:
                num_occupied.add(v)

        res = 0
        while deleting_ch:
            curr = deleting_ch.pop() # c
            curr_num = count[curr] # 2
            while curr_num > 0 and curr_num in num_occupied: # 2 > 0 and 2 in num_occupied
                res += 1
                curr_num -= 1
            
            if curr_num > 0:
                num_occupied.add(curr_num)
        
        return res
