from collections import deque

graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["G"], "F": [], "G": []}


def bfs(start, goal):
    q = deque([(start, [start])])
    seen = {start}
    order = []
    while q:
        node, path = q.popleft()
        order.append(node)
        if node == goal:
            return path, order
        for n in graph[node]:
            if n not in seen:
                seen.add(n)
                q.append((n, path + [n]))
    return None, order


def dfs(start, goal):
    stack = [(start, [start])]
    seen = set()
    order = []
    while stack:
        node, path = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        order.append(node)
        if node == goal:
            return path, order
        for n in reversed(graph[node]):
            stack.append((n, path + [n]))
    return None, order


bfs_path, bfs_order = bfs("A", "G")
dfs_path, dfs_order = dfs("A", "G")
print("BFS path:", bfs_path)
print("BFS visit order:", bfs_order)
print("DFS path:", dfs_path)
print("DFS visit order:", dfs_order)
