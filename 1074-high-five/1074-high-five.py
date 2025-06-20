from collections import defaultdict
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # scores in items
        # items[i] = [ID, score]
        # get top 5 score students
        # return result -> result[j] = [ID, topFiveAverage]
        # sort by id ASC

        # one id has 1 or more scors and get avg with top 5 scors
        # hashmap? [] defaultdict(list)? and then put one
        # during sum up, if len > 5, deduct min value from the sum and add new value?
        # 12345 6 -> 23456 -> but we dont know the second minimum if len 7
        # sort and save again get [:5] / len(list) 5->5 6->5 7->5
        # For each IDi, there will be at least five scores.
        # so need top 5 scores and divide by 5 always and get int val
        
        students = defaultdict(list)
        for id, score in items:
            students[id].append(score)
        
        # sorting top five scores
        # get only five
        for id, score in students.items():
            students[id] = sorted(score,reverse=True)[:5]

        # calculate avg
        # and save in result
        # 1 <= IDi <= 1000 -> len + 1
        result = []
        for id, score in students.items():
            result.append([id, int(sum(score) / 5)])
        
        # last sort by id asc
        result.sort(key= lambda x: x[0])
        return result