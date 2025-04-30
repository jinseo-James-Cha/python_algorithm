f = int(input())

fibo = [0] * (f + 1)
fibo[0] = 0
fibo[1] = 1

for num in range(2,f + 1):
    fibo[num] = fibo[num-1] + fibo[num-2]

print(fibo[f])