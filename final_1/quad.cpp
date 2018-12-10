#include <iostream>
#include <cmath>
#include <math.h>

int discriminant(int a, int b, int c) {
// this one works
    int d;
    d = pow(b,2) - 4*a*c;
    return d;
}

int quadsolve(int a, int b, int c) {

    int r;
    r = discriminant;
    if (d >= 0) { -b + pow(d, .5) / (2*a); }
    if (d < 0) return 0;
}

int main() {
    int r;
    r = discriminant (2,4,3);
    std::cout << r;
    int a = quadsolve;
    std::cout << a;
    return 0;
   
}