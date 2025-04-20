def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        candidates = [x for x in arr[s:e+1] if x > k]
        answer.append(min(candidates) if candidates else -1)
        # len_answer = len(answer)
        # for ar in arr:
        #     if ar > k:
        #         answer.append(ar)
        #         arr.remove(ar)
        #         break
        # if len_answer == len(answer):
        #     answer.append(-1)
            
    return answer