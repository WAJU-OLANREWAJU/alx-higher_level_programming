#!/usr/bin/python3
""" This module is a script that reads stdin line by line and computes metric. """

import sys
import signal

# Define signal handler for keyboard interrupt (CTRL + C)
def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

# Register signal handler
signal.signal(signal.SIGINT, signal_handler)

# Initialize variables to store metrics
total_file_size = 0
status_codes = {}

# Define function to print statistics
def print_statistics():
    print("Total file size: File size:", total_file_size)
    sorted_status_codes = sorted(status_codes.keys())
    for status_code in sorted_status_codes:
        print(status_code, ":", status_codes[status_code])

# Read input from stdin line by line
for i, line in enumerate(sys.stdin):
    try:
        # Extract file size and status code from the input line
        _, _, _, _, _, _, file_size, status_code = line.strip().split()
        
        # Update total file size
        total_file_size += int(file_size)
        
        # Update status codes dictionary
        if status_code in status_codes:
            status_codes[status_code] += 1
        else:
            status_codes[status_code] = 1
    except ValueError:
        # Skip lines that do not conform to the expected input format
        pass

    # Print statistics every 10 lines
    if (i + 1) % 10 == 0:
        print_statistics()

# Print final statistics
print_statistics()
