nums = []
for _ in range(9):
    nums.append(int(input()))

max_i = 0 
max_num = 0
for i,num in enumerate(nums):
    if num > max_num:
        max_i = i + 1
        max_num = num

print(max_num)
print(max_i)