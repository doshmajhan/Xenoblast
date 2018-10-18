#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include "unitcomp.h"

#define PI 3.14159265

// Represents an expensive computation that should 
// generate CPU load
void compute(){
    
    // Seed our RNG
    srand(time(NULL));

    // Get a random number between 0 and 90
    double x = (rand() % 90) + 1;
    
    // Get the cosine of our number
    double val = (PI/180.0) * x;
    double res = cos(val);

    printf("Cosine of %lf is %lf degrees\n", x, res);
}

