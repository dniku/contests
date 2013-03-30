class dseg {
	public double x1;
	public double y1;
	public double x2;
	public double y2;

	public dseg(double _x1, double _y1, double _x2, double _y2) {
		x1 = _x1;
		y1 = _y1;
		x2 = _x2;
		y2 = _y2;
	}

	public double a() {
		return y2-y1;
	}

	public double b() {
		return x1-x2;
	}

	public double c() {
		return y1*(x2-x1) + x1*(y1-y2);
	}
}

public class alg {

	// General algorithms

	public static int signum(double x) {
		if (x > 0)
			return 1;
		else if (x < 0)
			return -1;
		return 0;
	}

	// Numerical algorithms

	public static int gcd(int a, int b) {
		int tmp = 0;
		while (b != 0) {
			tmp = a % b;
			a = b;
			b = tmp;
		}
		return a;
	}

	// Array algorithms

	public static int lower_bound(long[] list, int first, int last, long val) {
		int len = last - first;
		int half;
		int middle;
		while (len > 0) {
			half = len >>> 1;
			middle = first + half;
			if (list[middle] < val) {
				first = middle + 1;
				len = len - half - 1;
			} else
				len = half;
		}
		return first;
	}

	public static int upper_bound(long[] list, int first, int last, long val) {
		int len = last - first;
		int half;
		int middle;
		while (len > 0) {
			half = len >>> 1;
			middle = first + half;
			if (val < list[middle])
				len = half;
			else {
				first = middle + 1;
				len = len - half - 1;
			}
		}
		return first;
	}

	// Geometry

	public static boolean onLine(int lx1, int ly1, int lx2, int ly2, int x, int y) {
		return (x - lx1) * (ly2 - ly1) == (y - ly1) * (lx2 - lx1);
	}

	public static boolean intersect(dseg s1, dseg s2) {
		double x1 = s1.x1; double y1 = s1.y1; double x2 = s1.x2; double y2 = s1.y2;
		double a2 = s2.a();	double b2 = s2.b();	double c2 = s2.c();
		int sg1 = signum(a2*x1 + b2*y1 + c2);
		int sg2 = signum(a2*x2 + b2*y2 + c2);
		if (sg1*sg2 > 0)
			return false;
		double x3 = s2.x2; double y3 = s2.y1; double x4 = s2.x2; double y4 = s2.y2;
		double a1 = s1.a(); double b1 = s1.b(); double c1 = s1.c();
		int sg3 = signum(a1*x3 + b1*y3 + c1);
		int sg4 = signum(a1*x4 + b1*y4 + c1);
		return sg3*sg4 <= 0;
	}
}