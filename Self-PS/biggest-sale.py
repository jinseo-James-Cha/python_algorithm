shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    # 최대로 할인받으려면 최대값에 최대 할인율 적용 -> 내림차순 적용
    # 할인율도 내림차순 적용 후 for loop 돌림.
    # 그 다음 그 값을 저장
    answer = 0
    prices.sort(reverse=True)
    coupons.sort(reverse=True)
    print(prices)
    print(coupons)

    min_len = min(len(prices), len(coupons))
    index = 0
    while index < min_len:
        answer += int(prices[index] * ((100 - coupons[index]) / 100 ))
        index += 1

    if len(prices) > len(coupons):
        for p in prices[min_len:]:
            answer += p

    return answer


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))