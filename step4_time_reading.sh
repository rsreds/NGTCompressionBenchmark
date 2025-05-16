#!/bin/bash

# Output CSV file
output_file="../store/uncompressed/timing_results_reading.csv"
echo "events,format,time_seconds" > "$output_file"

# List of event counts
for events in 1 10 100 1000 5000; do
    echo "Running with $events events in TTRee format ..."

    log_file="../store/uncompressed/log_step4_GenericConsumer_TTRee_${events}.txt"
    filename="step3_RAW_TTRee_${events}.root"
    # Run command, save log, and time it
    time_output=$( ( /usr/bin/time -f "%e" cmsRun step4_GenericConsumer_TTree.py "$filename" ) &> "$log_file" 2>&1 )
    run_time=$(tail -1 $log_file)

    # Save timing to CSV
    echo "$events,TTRee,$run_time" >> "$output_file"

    # Notify completion
    notify-complete "step4_GenericConsumer_TTree.py for "$events" events completed in "$run_time" seconds."

    echo "Running with $events events in RNTuple format ..."

    log_file="../store/uncompressed/log_step4_GenericConsumer_RNTuple_${events}.txt"
    filename="step3_RAW_RNTuple_${events}.root"
    # Run command, save log, and time it
    time_output=$( ( /usr/bin/time -f "%e" cmsRun step4_GenericConsumer_RNTuple.py "$filename" ) &> "$log_file" 2>&1 )
    run_time=$(tail -1 $log_file)

    # Save timing to CSV
    echo "$events,RNTuple,$run_time" >> "$output_file"

    # Notify completion
    notify-complete "step4_GenericConsumer_RNTuple.py for "$events" events completed in "$run_time" seconds."

done
