def prim(graph, start):
    n = len(graph)
    visited = [False] * n
    visited[start] = True

    mst = []
    total = 0

    for _ in range(n - 1):
        minimum = float("inf")
        u = -1
        v = -1

        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if not visited[j] and graph[i][j] != 0:
                        if graph[i][j] < minimum:
                            minimum = graph[i][j]
                            u = i
                            v = j

        if v == -1:
            print("MST not possible")
            return

        mst.append((u, v, minimum))
        total += minimum
        visited[v] = True

    print("Edges in Minimum Spanning Tree:")
    for u, v, weight in mst:
        print(locations[u], "-", locations[v], ":", weight)

    print("Total Minimum Time:", total)


locations = ["A", "B", "C", "D"]

graph = [
    [0, 4, 3, 0],
    [4, 0, 2, 5],
    [3, 2, 0, 7],
    [0, 5, 7, 0]
]

prim(graph, 0)
