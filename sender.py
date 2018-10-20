import time
from unitcomp import unitcomp

def initialization():
    while(True):
        time_taken = unitcomp()
        print(time_taken)

if __name__ == "__main__":
    initialization()
