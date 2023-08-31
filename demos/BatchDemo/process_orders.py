import time
import threading

BATCH_TIME_IN_SECONDS = 5
BATCH_SIZE = 5
input_file_path = 'pending_orders.txt'

# Read 5 lines from the input file and print to std out.
while True:
    with open(input_file_path, 'rw') as input_file:
        lines = input_file.readlines()[:5]
        input_file_path.writelines
        for line in lines:
            print( line )
    time.sleep(BATCH_TIME_IN_SECONDS)

