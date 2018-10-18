#include <stdio.h>
#include <math.h>

#define PI 3.14159265

// Represents an expensive computation that should 
// generate CPU load
void compute(){
    double x = 60.0;
    double val = (PI/180.0) * x;
    double res = cos(val);

    printf("Cosine of %lf is %lf degrees\n", x, res);
}

int main(){
    compute();
}
