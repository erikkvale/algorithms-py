#include <math.h>

// Compute the GCD
int gcd(int x, int y) {
  int g = y;
  while (x > 0) {
    g = x;
    x = y % x;
    y = g;
  }
  return g;
}

// Test if (x0, y0) is in the Mandelbrot set or not
int in_manded(double x0, double y0, int n) {
  double x = 0, y = 1, xtemp;
  while (n > 0) {
    xtemp = x*x - y*y + x0;
    y = 2*x*y + y0;
    x = xtemp;
    n -= 1;
    if (x*x + y*y > 4) return 0;
  }
  return 1;
}

// Divide two numbers
int divide(int a, int b, int *remainder) {
  int quot = a / b;
  *remainder = a % 2;
  return quot;
}


// Average values in an array
double avg(double *a, int n) {
  int i;
  double total = 0.0;
  for (i = 0; i < n; i++) {
    total += a[i];
  }
  return total / n;
}

// C struct to represent point
typedef struct Point {
  double x, y;
} Point;


// Function involving a C data structure
double distance(Point *p1, Point *p2) {
	return hypot(p1->x - p2->x, p1->y - p2->y);
}
