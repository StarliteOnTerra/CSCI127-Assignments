#include <iostream>
#include <cmath>
#include <math.h>

int discriminant(int a, int b, int c) {
// this one works
    int d;
    d = pow(b,2) - 4*a*c;
    return d;
}

int quadSolve(int a, int b, int c) {
    int d;
    int e;
    d = pow(b,2) - 4*a*c;
    if (d >= 0)
    	e = -b + pow(d, .5)/(2*a);
	return e;
    std::cout << e;
    if (d < 0) 
	return 0;
}

int main() {
    int r;
    r = discriminant (2,4,3);
    std::cout << r;
    int f;
    f = quadSolve (4, 5, 3);
    std::cout << f;

 return 0;   
}