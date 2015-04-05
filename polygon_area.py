from __future__ import division

with open('area.in', 'r') as fin:
	with open('area.out', 'w') as fout:
		n = int(fin.readline())
		points = []
		for _ in xrange(n):
			x, y = (int(v) for v in fin.readline().split())
			points.append((x, y))
		area = 0
		for ((x1, y1), (x2, y2)) in zip(points, points[1:] + [points[0]]):
			area += (x2 - x1) * (y1 + y2)
		area = abs(area) / 2
		fout.write('%.1f' % area)
