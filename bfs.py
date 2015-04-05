import heapq
from collections import defaultdict

def bfs(graph, n, start, finish):
	queue = [(0, start)]
	was = [False] * n
	while queue:
		dist, next = heapq.heappop(queue)
		if next == finish:
			return dist
		if was[next]:
			continue
		was[next] = True
		for neigh in graph[next]:
			heapq.heappush(queue, (dist + 1, neigh))
	return 0

with open('bfs.in', 'r') as fin:
	with open('bfs.out', 'w') as fout:
		n, s, f = (int(v) for v in fin.readline().split())
		s -= 1
		f -= 1
		graph = defaultdict(set)
		for i in xrange(n):
			for j, v in enumerate(int(s) for s in fin.readline().split()):
				if v == 1:
					graph[i].add(j)
		fout.write(str(bfs(graph, n, s, f)))