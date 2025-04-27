# enumerate를 하면 idx, value가 나오는구나!
# return [work for idx, work in enumerate(todo_list) if not finished[idx]]


def solution(todo_list, finished):
    return [todo_list[i] for i in range(len(todo_list)) if not finished[i]]