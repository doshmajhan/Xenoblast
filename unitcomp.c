#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include "unitcomp.h"

#define PI 3.14159265


// Represents an expensive computation that should 
// generate CPU load
// returns the time taken to execute
double unitcomp(){
    
    // Start clock
    clock_t t = clock();

    int count = 0;

    while (count < 696) {
        srand(time(NULL));
    
        double y = rand();
        double x = rand();
        double val = (fmod(pow(x, y), 90.0)) + 1.0;
    
        double degrees = (PI/180.0) * val;
        double res = cos(degrees);
        (void)res;

        count += 1;
    }

    // Get end time
    t = clock() - t;
    double time_taken = ((double)t)/CLOCKS_PER_SEC;
    return time_taken;
}

