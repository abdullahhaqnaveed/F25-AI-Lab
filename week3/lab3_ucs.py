import heapq
from collections import deque

graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F", "G"], "D": [], "E": ["G"], "F": [], "G": []}
weights = {("A", "B"): 1, ("A", "C"): 2, ("B", "D"): 2, ("B", "E"): 1,
           ("C", "F"): 3, ("C", "G"): 10, ("E", "G"): 1}


def ucs(start, goal):
    count = 0
    heap = [(0, count, start, [start])]
    best = {start: 0}
    order = []
    while heap:
        cost, _, node, path = heapq.heappop(heap)
        if cost != best[node]:
            continue
        order.append(node)
        if node == goal:
            return path, cost, order
        for n in graph[node]:
            new_cost = cost + weights[(node, n)]
            if new_cost < best.get(n, 9999):
                best[n] = new_cost
                count += 1
                heapq.heappush(heap, (new_cost, count, n, path + [n]))
    return None, 0, order


def bfs_path(start, goal):
    q = deque([(start, [start])])
    seen = {start}
    while q:
        node, path = q.popleft()
        if node == goal:
            return path
        for n in graph[node]:
            if n not in seen:
                seen.add(n)
                q.append((n, path + [n]))
    return None


path, cost, order = ucs("A", "G")
print("UCS processing order:", order)
print("UCS path:", path)
print("UCS cost:", cost)

total = 0
for i in range(len(path) - 1):
    total = total + weights[(path[i], path[i + 1])]
print("Cost checked by adding edges again:", total)

broute = bfs_path("A", "G")
bcost = 0
for i in range(len(broute) - 1):
    bcost = bcost + weights[(broute[i], broute[i + 1])]
print("BFS path on the same graph:", broute)
print("BFS path cost:", bcost)
