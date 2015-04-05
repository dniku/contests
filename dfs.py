from collections import defaultdict

def dfs(graph, start, cnum, lastcomp):
	stack = [start]
	while stack:
		next = stack.pop()
		if cnum[next] == -1:
			cnum[next] = lastcomp
			for neigh in graph[next]:
				if cnum[neigh] == -1:
					stack.append(neigh)


with open('connect2.in', 'r') as fin:
	with open('connect2.out', 'w') as fout:
		n, m = (int(v) for v in fin.readline().split())
		if n == 0:
			fout.write(str(0))
			exit()
		g = defaultdict(set)
		for line in fin:
			u, v = (int(v) for v in line.split())
			g[u - 1].add(v - 1)
			g[v - 1].add(u - 1)

		cnum = [-1] * n
		lastcomp = 0
		for node in xrange(n):
			if cnum[node] == -1:
				lastcomp += 1
				dfs(g, node, cnum, lastcomp)
		fout.write(str(lastcomp))