# python script that calls cmsRun step4_compression_test.py <compression> <level> <output_file> <num_events>
#
# Ten times for all compression algorithms LZMA, ZLIB, LZ4, ZSTD and levels 0 to 9
# for 1000 events
#
# The ouput file name will be of the form step4_<compression><level>_<num_events>.root

import os
import subprocess
import time
from itertools import product
import re
import json

def get_sizes_from_command(command):
    # Run the shell command and capture output
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = result.stdout

    # Parse JSON output
    data = json.loads(result.stdout)
    
    # Extract sizes
    uncompressed_size = data["total"]["size_uncompressed"]
    compressed_size = data["total"]["size_compressed"]
    
    return uncompressed_size, compressed_size

# Define the compression algorithms, levels, and number of events
compressions = ["LZMA", "ZLIB", "LZ4", "ZSTD"]
levels = range(10)  # Levels 0 to 9
# levels = [0,4,9]  # Levels 0 to 9
# num_events_list = [1, 5, 10, 50, 100]
num_events_list = [1000]

# Generate all combinations of compression algorithms, levels, and number of events
combinations = product(compressions, levels, num_events_list)

with open("cmssw_bench_output.csv", "w") as f:
    f.write(f"Algorithm,Level,Events,Uncompressed,Compressed,Time,Filename,Iteration\n")

# Iterate over all combinations
for compression, level, num_events in combinations:
    # Construct the output file name
    output_file = f"step4_{compression}{level}_{num_events}.root"
    
    # Construct the command
    command = ["cmsRun", "step4_compression_test.py", compression, str(level),  str(num_events), output_file]
    
    # Print the command (for debugging purposes)
    print(f"Running command: {' '.join(command)}")
    
    # Run the command 10 times, time it and save output_file, file size and time in a csv file
    for i in range(10):
        start = time.time()
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        end = time.time()
        elapsed_time = end - start
    
        file_size = os.path.getsize(output_file)
        uncompressed_size, compressed_size = get_sizes_from_command("edmEventSize -v -f json " + output_file)
        print(f"Run {i}")
        print(f"Elapsed time: {elapsed_time} seconds")
        print(f"Output file: {output_file}")
        print(f"Output file size: {os.path.getsize(output_file)} bytes")
        os.remove(output_file)
        with open("cmssw_bench_output.csv", "a") as f:
            f.write(f"{compression},{level},{num_events},{uncompressed_size},{compressed_size},{elapsed_time},{output_file},{i}\n")
    
