import time
from unitcomp import unitcomp

"""
    Run unit comp 100 times to establish
    the average amount of time it should take to run
    returns the average time taken to run unitcomp
"""
def initialization():
    count = 0
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
        if time_taken > (avg_time + 0.03):
            
            print("Higher load noticed, checking if sync is in progress")
            print(time_taken - (avg_time + 0.03))
            # Time is greater than average so
            # see if it stays that way for at least 1.5s
            while time_taken > (avg_time + 0.03):
                time_taken = unitcomp()
                end_time = time.time()
                print("Above average loop")

            # check if the time it lasted was at least 1.5 seconds
            if (end_time - start_time) >= 1.5:
                print("Lasted atleast 1.5")
                # time was at least 1.5 seconds so 
                # we can assume the sender is syncing with us
                # so break out of this function
                return

            # time was not long enough for sync phase
            # so keep looking
            print("Continue")
            continue

"""
    Confirms that the rise in CPU load occured from the sender.
    Will determine how many times unitcomp can be run in 1 second. 
    If during this period, any of the execution times of unitcomp
    is greater than the precalculated average (plus the threshold)
    then it is determine that something else was causing the CPU load
    on the system, not the sender.

    :param avg_time: the average time unitcomp should execute for

    :returns zero if it finds it was a false, sync otherwise 
             it runs the count of unitcomp execs
"""
def confirmation(avg_time):
    count = 0
 
    # Run for 1 second
    end_time = time.time() + 1

    while time.time() <= end_time:
        
        time_taken = unitcomp()
        count += 1

        if time_taken > (avg_time + 0.03):
            # High CPU load is still occuring meaning
            # it wasn't the sender creating it
            return 0
    
    return count


"""
    Attempts to recieve 64 bits of data from sender. 
    Will measure number of unitcomp executions during 1 second.
    If it is less than 90% of standard number, a 1 is recieved.
    Otherwise a 0 is recieved. It will pause for 1 second between
    bits to prevent VCPU state as being viewed as "over". 
"""
def recieve_data(standard_number):
    num_bits = 0
    data = ""

    while num_bits < 64:

        # Run for 1 second
        end_time = time.time() + 1
        count = 0
        while time.time() <= end_time:
        
            unitcomp()
            count += 1

        if count < (standard_number * 0.9):
            # It was less than 90% so it was a 1
            data += "1"
        else:
            data += "0"

        num_bits += 1

        # pause for 1 second
        time.sleep(1)
    
    return data

if __name__ == '__main__':
    
    # INIT
    print("Starting initialization")
    avg_time = initialization()
    print("Average execution time: {}".format(avg_time))
    
    confirmed = False
    standard_number = 0

    while not confirmed:
        # SYNC
        print("Listening for synchronization phase")
        synchronization(avg_time)
        print("Synchronization complete")

        # Sleep after sync
        time.sleep(1)
        
        # CONFIRM
        print("Confirming the higher load is from the sender")
        standard_number = confirmation(avg_time)
        print("Standard number: {}".format(confirmed))
        if standard_number > 0:
            confirmed = True

    
    # Pause to reset state of vcpus
    time.sleep(1)
    
    # RECIEVE DATA
    data = recieve_data(standard_number)

    # convert bit string to hex string then to regular string
    hex_string = hex(int(data, 2))
    phrase = hex_string.decode('hex')
    print("Recieved data: {}".format(phrase))

