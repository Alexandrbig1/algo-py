def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    selected_items = []
    total_cost = 0
    total_calories = 0

    for item, data in sorted_items:
        if total_cost + data['cost'] <= budget:
            selected_items.append(item)
            total_cost += data['cost']
            total_calories += data['calories']

    return selected_items, total_calories


def dynamic_programming(items, budget):
    item_list = list(items.items())
    n = len(item_list)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, data = item_list[i - 1]
        cost, calories = data['cost'], data['calories']
        for j in range(budget + 1):
            if cost > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + calories)

    selected_items = []
    j = budget
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            name, data = item_list[i - 1]
            selected_items.append(name)
            j -= data['cost']

    return selected_items, dp[n][budget]


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 60
print("Greedy Algorithm:", greedy_algorithm(items, budget))
print("Dynamic Programming:", dynamic_programming(items, budget))

budget2 = 30
print("Greedy Algorithm:", greedy_algorithm(items, budget2))
print("Dynamic Programming:", dynamic_programming(items, budget2))