import heapq


def min_cost_cables(cables):
    if not cables:
        return 0

    heapq.heapify(cables)
    cost_total = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        cables_cost = first + second
        cost_total += cables_cost
        heapq.heappush(cables, cables_cost)

    return cost_total


cables = [3, 2, 1, 7, 8, 5]
print(min_cost_cables(cables))