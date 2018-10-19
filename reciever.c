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

// Runs an indefinite operation to consitatantly run
// unitcomp until it is over 0.03 secs of the usual run time.
// If it is seen to running over the run time for atleast 1.5 seconds
// then it means the sender is about to transmit
void synchronization(double avg_time) {
    while(1) {
        clock_t start_time = clock();
        clock_t end_time;

        // Get time taken for unitcomp
        double time_taken = unitcomp();

        // Check if the time taken is greater than average
        if (time_taken >= (avg_time + 0.03)){
            
            printf("Higher load noticed, checking if sync is in progress\n");

            // Time is greater than average so
            // see if it stays that way for atleast 1.5s
            while (time_taken >= (avg_time + 0.03)) {
                time_taken = unitcomp();
                end_time = clock();
            }

            // check if the time it lasted was atleast 1.5 seconds
            if ((end_time - start_time) >= 1.5){
                // time was atleast 1.5 seconds so 
                // we can assume the sender is syncing with us
                // so break out of this function
                break;
            }

            // time was not long enough for sync phase
            // so keep looking
            continue;
        }
    }
}



int main(){
    
    // INIT
    printf("Starting initialization\n");
    double avg_time = initialization();
    printf("Average execution time: %lf\n", avg_time);
    
    // SYNC
    printf("Listening for synchronization phase\n");
    synchronization(avg_time);
    printf("Synchronization complete\n");

    // CONFIRM
    printf("Confirming the higher load is from the sender\n");
    
    // RECIEVE DATA

    return EXIT_SUCCESS;
}
