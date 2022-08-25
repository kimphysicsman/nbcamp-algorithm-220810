# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
#
# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
#
# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

from collections import deque


def bfs_order(graph_dict, start_num):

    visited_list = []

    queue = deque()
    queue.append(start_num)
    visited_list.append(start_num)

    while len(queue) != 0:
        visited_num = queue.popleft()

        neighbor_list = graph_dict.get(visited_num, None)

        if neighbor_list is not None:
            neighbor_list.sort()
            for neighbor_num in neighbor_list:
                if neighbor_num not in visited_list:
                    queue.append(neighbor_num)
                    visited_list.append(neighbor_num)

    return visited_list


def dfs_order(graph_dict, start_num):

    visited_list = []
    stack = [start_num]

    while len(stack) != 0:
        visited_num = stack.pop()
        if visited_num in visited_list:
            continue

        visited_list.append(visited_num)

        neighbor_list = graph_dict.get(visited_num, None)

        if neighbor_list is not None:
            neighbor_list.sort(reverse=True)
            for neighbor_num in neighbor_list:
                if neighbor_num not in visited_list:
                    stack.append(neighbor_num)

    return visited_list


def main():
    [n, m, v] = [int(item) for item in input("input N, M, V : ").split()]

    graph = dict()

    for _ in range(m):
        [s, e] = [int(item) for item in input("input Edge (V1, V2) : ").split()]

        edge_list = graph.get(s, None)
        if edge_list is None:
            graph[s] = [e]
        else:
            graph[s].append(e)

        edge_list = graph.get(e, None)
        if edge_list is None:
            graph[e] = [s]
        else:
            graph[e].append(s)

    print(dfs_order(graph, v))
    print(bfs_order(graph, v))


main()