# 문제
# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 
# 상근이는 숫자 카드 N개를 가지고 있다. 
# 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 
# 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 
# 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다. 
# 두 숫자 카드에 같은 수가 적혀있는 경우는 없다.

# 셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 
# 넷째 줄에는 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어지며, 
# 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다

# 출력
# 첫째 줄에 입력으로 주어진 M개의 수에 대해서, 
# 각 수가 적힌 숫자 카드를 상근이가 가지고 있으면 1을, 아니면 0을 공백으로 구분해 출력한다.

# input                     output
# 5                         1 0 0 1 1 0 0 1
# 6 3 2 10 -10
# 8
# 10 9 -5 2 3 4 5 -10


# version 2
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







# Time exceed
# the below code is O(NM) -> 500,000 * 500,000 = 250,000,000,000 = 25 * 10^10
# N = int(input())
# my_cards = list(map(int, input().split()))

# M = int(input())
# check_cards = list(map(int, input().split()))

# answer = ""
# for c in check_cards:
#     answer += str(int(c in my_cards)) + " "

# print(answer[:-1])




