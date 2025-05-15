#!/bin/bash

# Output CSV file
output_file="../store/uncompressed/timing_results.csv"
echo "events,format,time_seconds" > "$output_file"

# List of event counts
for events in 1 10 100 1000 5000; do
    echo "Running with $events events in TTRee format ..."

    log_file="../store/uncompressed/log_step3_RAW_uncompressed_TTRee_${events}.txt"

    # Run command, save log, and time it
    time_output=$( ( /usr/bin/time -f "%e" cmsRun step3_RAW_uncompressed_TTRee.py "$events" ) &> "$log_file" 2>&1 )
    run_time=$(tail -1 $log_file)

    # Save timing to CSV
    echo "$events,TTRee,$run_time" >> "$output_file"

    # Notify completion
    notify-complete "step3_RAW_uncompressed_TTRee.py for "$events" events completed in "$run_time" seconds."



    echo "Running with $events events in RNTuple format ..."

    log_file="../store/uncompressed/log_step3_RAW_uncompressed_RNTuple_${events}.txt"

    # Run command, save log, and time it
    time_output=$( ( /usr/bin/time -f "%e" cmsRun step3_RAW_uncompressed_RNTuple.py "$events" ) &> "$log_file" 2>&1 )
    run_time=$(tail -1 $log_file)
    # Save timing to CSV
    echo "$events,RNTuple,$run_time" >> "$output_file"

    # Notify completion
    notify-complete "step3_RAW_uncompressed_RNTuple.py for "$events" events completed in "$run_time" seconds."

done
