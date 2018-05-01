#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
#pragma GCC optimize("Ofast")

#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
using namespace std;

#ifdef DEV
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
#define eprintf(...)
#endif

#define forn(i, n) for (size_t i = 0; i < (n); ++i)
void timestamp(char const * const tag, bool absolute = false);

// </template>

void read() {

}

void solve() {

}

// <template>

void timestamp(char const * const tag, bool absolute) {
  static double last = 0;
  double now = (static_cast<double>(clock()) / CLOCKS_PER_SEC) * 1000;
  if (absolute) {
    eprintf("%s: %.2lf ms\n", tag, now);
  }
  else {
    eprintf("%s: %.2lf ms\n", tag, now - last);
    last = now;
  }
}

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);

  timestamp("start");
#ifdef DEV
  string fncpp = __FILE__;
  string fnbase = fncpp.substr(0, fncpp.find_last_of("."));
  string fnin = fnbase + ".in";
  assert(freopen(fnin.c_str(), "r", stdin));
  // string fnout = fnbase + ".out";
  // freopen(fnout.c_str(), "w", stdout);
  timestamp("freopen()");
#endif

  read();
  timestamp("read()");
  solve();
  timestamp("solve()");
  timestamp("total", true);
  return 0;
}
