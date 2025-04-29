N = int(input())
my_cards = sorted(map(int, input().split()))

M = int(input())
check_cards = list(map(int, input().split()))

def check_in_my_cards(target):
    left = 0
    right = N - 1
    while left <= right:
        mid = (left + right) // 2
        if my_cards[mid] == target:
            return "1"
        elif my_cards[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return "0"

answer = ' '.join([check_in_my_cards(target) for target in check_cards])
print(answer)
