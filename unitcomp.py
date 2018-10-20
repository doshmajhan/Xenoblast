import math
import random
import time


"""
    Represents an expensive computation that should 
    generate CPU load
    returns the time taken to execute
"""
def unitcomp():
    
    # Start clock
    t = time.time()
    
    y = random.getrandbits(17)
    x = random.getrandbits(17)
    x**y
    # Get end time
    time_taken = time.time() - t
    return time_taken

