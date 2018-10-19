import time
from unitcomp import unitcomp

"""
    Run unit comp 100 times to establish
    the average amount of time it should take to run
    returns the average time taken to run unitcomp
"""
def initialization():
    count = 0;
    total_time = 0

    while(count < 100): 
        total_time += unitcomp()
        count += 1

    print("Total time taken: {}".format(total_time))

    avg_time = total_time / count
    return avg_time

"""
    Runs an indefinite operation to consistently run
    unitcomp until it is over 0.03 secs of the usual run time.
    If it is seen to running over the run time for at least 1.5 seconds
    then it means the sender is about to transmit

    :param avg_time: the average time unitcomp took to ran to compare against
"""
def synchronization(avg_time):
    while(True):
        start_time = time.time()

        # Get time taken for unitcomp
        time_taken = unitcomp()

        # Check if the time taken is greater than average
        if (time_taken >= (avg_time + 0.03)):
            
            print("Higher load noticed, checking if sync is in progress")

            # Time is greater than average so
            # see if it stays that way for at least 1.5s
            while time_taken >= (avg_time + 0.03):
                time_taken = unitcomp()
                end_time = time.time()

            # check if the time it lasted was at least 1.5 seconds
            if (end_time - start_time) >= 1.5:
                # time was at least 1.5 seconds so 
                # we can assume the sender is syncing with us
                # so break out of this function
                return

            # time was not long enough for sync phase
            # so keep looking
            continue


if __name__ == '__main__':
    
    # INIT
    print("Starting initialization")
    avg_time = initialization()
    print("Average execution time: {}".format(avg_time))
    
    # SYNC
    print("Listening for synchronization phase")
    synchronization(avg_time)
    print("Synchronization complete")

    # CONFIRM
    print("Confirming the higher load is from the sender")
    
    # RECEIVE DATA
