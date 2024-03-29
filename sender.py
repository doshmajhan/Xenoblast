import bitarray
import time
from unitcomp import unitcomp


"""
    Creates a high CPU load for 1.7 seconds
    to signify to the receiver that it is syncing
"""
def synchronization():
    
    # Run for 1.5 seconds
    end_time = time.time() + 1

    while time.time() <= end_time:
        
        unitcomp()


"""
    Transmit each bit of the data. 
    If transmitting a 1, run unitcomp for 1 second.
    If transmitting a 0, do nothing.
    Sleep for 1 second in between each transmission.
"""
def transmit_data(data):

    for x in data:
        # Run for 1 seconds
        end_time = time.time() + 1

        if x == 1:
            print("Sending 1")
            while time.time() <= end_time:

                unitcomp()
        else:
            print("Sending 0")
            time.sleep(end_time - time.time())

        # pause for 1 second
        time.sleep(1)


if __name__ == "__main__":
    
    data = "pass"
    ba = bitarray.bitarray()
    ba.frombytes(data.encode("utf-8"))   
    
    print("Starting sync")
    # Send synchronization
    synchronization()

    # Reset VCPU
    time.sleep(1)

    # Sleep again while receiver confirms
    time.sleep(1)

    # Pause for 1 more second to sync up
    time.sleep(0.7)

    print("Transmitting data")
    transmit_data(ba)
