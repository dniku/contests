def G(x):
    return x & (x + 1)

def H(x):
    return x | (x + 1)

class Fenwick:
    def __init__(self, a):
        self.a = a
        self.t = [0] * len(a)
        for i, val in enumerate(a):
            self.update(i, val)

    def __getitem__(self, i):
        return self.a[i]

    def __setitem__(self, i, val):
        delta = val - self.a[i]
        self.a[i] = val
        self.update(i, delta)

    def __str__(self):
        return 'Fenwick(%s)' % str(self.a)

    def __repr__(self):
        return 'Fenwick(%s)' % repr(self.a)
        
    def sum_less(self, r):
        result = 0
        while r >= 0:
            result += self.t[r]
            r = G(r) - 1
        return result
    
    def sum_interval(self, l, r):
        return self.sum_less(r) - self.sum_less(l - 1)

    def update(self, i, delta):
        while i < len(self.t):
            self.t[i] += delta
            i = H(i)

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    f = Fenwick(a)
    print f
    print f.sum_interval(0, 2)
    f[1] = 3
    print f
    print f.sum_interval(0, 2)
