import time
from typing import Dict, List
from collections import defaultdict


def find_coins_greedy(amount: int, coins: List[int] = [50, 25, 10, 5, 2, 1]) -> Dict[int, int]:
    change = {}
    for coin in sorted(coins, reverse=True):
        if amount >= coin:
            count = amount // coin
            change[coin] = count
            amount -= coin * count
    return change


def find_min_coins(amount: int, coins: List[int] = [50, 25, 10, 5, 2, 1]) -> Dict[int, int]:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    if dp[amount] == float('inf'):
        return {}

    change = defaultdict(int)
    while amount > 0:
        coin = coin_used[amount]
        change[coin] += 1
        amount -= coin

    return dict(change)


def test_algorithms(amount: int) -> None:
    print(f"Testing for amount: {amount}")

    start_time = time.perf_counter()
    greedy_result = find_coins_greedy(amount)
    greedy_time = time.perf_counter() - start_time

    start_time = time.perf_counter()
    dp_result = find_min_coins(amount)
    dp_time = time.perf_counter() - start_time

    print("Greedy Algorithm Result:", greedy_result)
    print("Time taken:", greedy_time)

    print("Dynamic Programming Result:", dp_result)
    print("Time taken:", dp_time)
    print("-" * 10)


if __name__ == "__main__":
    test_algorithms(113)
    test_algorithms(1000)
    test_algorithms(10000)
    test_algorithms(50000)