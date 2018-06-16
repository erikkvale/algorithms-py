#include <math.h>

// Compute the GCD
int gcd(int x, int y) {
  int g = y;
  while (x > 0) {
    g = x;
    x = y % x;
    y = g;
  }
  return g;-
}

// Test if (x0, y0) is in the Mandelbrot set or not
int in_manded(double x0, double y0, int n) {
  double x0, y0, xtemp;
  while (n > 0) {
    xtemp = x*x - y*y + x0;
    y = 2*x*y + y0;
    x = xtemp;
    n -= 1;
    if (x*x + y*y > 4) return 0;
  }
  return 1;
}
