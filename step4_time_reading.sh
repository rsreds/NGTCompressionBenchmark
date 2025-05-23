#!/bin/bash

# Output CSV file
output_file="../results/fixed_data_timing_results_reading.csv"
# echo "events,format,time_seconds" > "$output_file"

# List of event counts
for events in 1 10 100 1000 2000 3000 4000 5000; do
    for format in TTree RNTuple; do
        total_time=0
        for run in {1..10}; do
            echo "Running with $events events in $format format (run $run/10)..."
            log_file="../store/uncompressed/logs/log_step4_GenericConsumer_${format}_${events}_run${run}.txt"
            filename="data_RAW_${format}_5000.root"
            # Run command, save log, and time it
            run_time=$( /usr/bin/time -f "%e" cmsRun step4_GenericConsumer_${format}.py "$filename" "$events" 2>&1 | tail -1 )
            echo "$run_time" > "$log_file"
            total_time=$(echo "$total_time + $run_time" | bc)
        done
        avg_time=$(echo "scale=3; $total_time / 10" | bc)
        # Save average timing to CSV
        echo "$events,$format,$avg_time" >> "$output_file"
        # Notify completion
        notify-complete "step4_GenericConsumer_${format}.py for $events events (average of 10 runs: $avg_time seconds)."
    done
done
