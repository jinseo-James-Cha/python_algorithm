class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        # nums1[i] = [id, val]
        # each nums1 and nums2 has unique ids and ASCENDING ORDER by id
    
        # using while loop with i for nums1 and j for nums2
        # like two pointers on each arrays.
        # id1, val1 = nums1[i] and id2, val2 = nums2[j]
        # if id1 < id2 and insert res with val1 i +=1
        # if id1 == id2 and insert with val1+val2 i, j += 1
        # else insert val2 j += 1

        # another loop check len(nums1) == j and len(nums2)== j
        # if different, insert the tails

        res = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            id1, val1 = nums1[i]
            id2, val2 = nums2[j]

            if id1 < id2:
                res.append([id1,val1])
                i += 1
            elif id1 > id2:
                res.append([id2, val2])
                j += 1
            else:
                res.append([id1, val1 + val2])
                i += 1
                j += 1
        
        # now i or j is not the end
        print(i, j)
        if i != len(nums1):
            res += nums1[i:]
        elif j != len(nums2):
            res += nums2[j:]
        
        print(res)
        return res