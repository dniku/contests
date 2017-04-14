#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
using namespace std;

#define eprintf(...) fprintf(stderr, __VA_ARGS__)
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
  timestamp("start");
#ifdef DEV
  string taskname = "";
  string fnin = taskname + ".in";
  assert(freopen(fnin.c_str(), "r", stdin));
  timestamp("freopen()");
#endif
  
  read();
  timestamp("read()");
  solve();
  timestamp("solve()");
  timestamp("total", true);
  return 0;
}
