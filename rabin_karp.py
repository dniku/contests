def search_substring(haystack, needle):
	# Rabin-Karp
	p = 31
	m = 2**31 - 1
	hashes = [0] * len(haystack)
	for i, c in enumerate(haystack):
		hashes[i] = ord(c) - ord('a') + ((hashes[i - 1] * p) % m if i > 0 else 0)
	cur_hash = 0
	for c in needle:
		cur_hash = (cur_hash * p + ord(c) - ord('a')) % m
	result = []
	maxp = 1
	for _ in xrange(len(needle)):
		maxp = (maxp * p) % m
	for i in xrange(len(needle) - 1, len(haystack)):
		hash_haystack = (hashes[i] - (maxp * hashes[i - len(needle)] if i >= len(needle) else 0)) % m
		if cur_hash == hash_haystack:
			result.append(i - len(needle) + 2)
		# cur_hash = (cur_hash * p) % m
	return result

with open('strings.in', 'r') as fin:
	with open('strings.out', 'w') as fout:
		t = fin.readline().strip()
		s = fin.readline().strip()
		positions = search_substring(t, s)
		if positions:
			fout.write(' '.join(str(v) for v in positions))
		else:
			fout.write('none')