#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include "unitcomp.h"

// Run unit comp 100 times to establish
// the average amount of time it should take to run
// returns the average time taken to run unitcomp
double initialization(){
    int count = 0;
    double total_time = 0.0;

    while(count < 100){ 
        total_time += unitcomp();
        count += 1;
    }

    printf("Total time taken: %lf\n", total_time);

    double avg_time = total_time / count;
    return avg_time;
}

int main(){
    
    printf("Starting initialization\n");
    
    double avg_time = initialization();
    printf("Average execution time: %lf\n", avg_time);

    return EXIT_SUCCESS;
}
