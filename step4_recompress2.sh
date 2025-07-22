#!/bin/bash

# Output CSV file
output_file="../results/complete_timing_results_Phas2_AVERAGED.csv"
echo "type,events,format,algo,level,avg_time_seconds,stdev_time,avg_filesize_kB,stdev_size" > "$output_file"

# List of event counts
for events in 500; do
    for type in "mc"; do
        for format in "RNTuple"; do
            # do a few reads for caching using step4_GenericConsumer_<format>.py <file_in> <num_events> without logs
            echo "Running pre-caching for $type with $events events in $format format ..."

            for i in {1..3}; do
                filename="${type}_Phase2_${format}_${events}.root"
                cmsRun step4_GenericConsumer_"$format".py "$filename" "$events" &> /dev/null
            done

            for algo in "LZMA" "ZSTD" "ZLIB" "LZ4"; do
                for level in 1 2 3 4 5 6 7 8 9; do
                    echo "Running $type with $events events in $format format with $algo compression level $level ..."

                    log_file="../store/compressed/logs/${type}_compress_Phase2_${format}_${events}_${algo}_${level}.log"
                    filename="${type}_Phase2_${format}_${events}.root"
                    runs=5
                    times=()
                    sizes=()
                    for run in $(seq 1 $runs); do
                        # Run command, save log, and time it
                        time_output=$( ( /usr/bin/time -f "%e" cmsRun step4_compress_"$format".py "$filename" "$algo" "$level" ) &> "$log_file" 2>&1 )
                        run_time=$(tail -1 "$log_file")
                        outfilename="../store/compressed/phase2/${type}_Phase2_${format}_${events}_${algo}_${level}.root"
                        file_size=$(du "$outfilename" | cut -f1)
                        rm "$outfilename"
                        times+=("$run_time")
                        sizes+=("$file_size")
                    done
                    # Calculate average and stdev for time and size
                    avg_time=$(printf "%s\n" "${times[@]}" | awk '{sum+=$1} END {printf "%.3f", sum/NR}')
                    stdev_time=$(printf "%s\n" "${times[@]}" | awk '{x[NR]=$1; sum+=$1} END {mean=sum/NR; for(i=1;i<=NR;i++)s+=(x[i]-mean)^2; printf "%.3f", sqrt(s/NR)}')
                    avg_size=$(printf "%s\n" "${sizes[@]}" | awk '{sum+=$1} END {printf "%d", sum/NR}')
                    stdev_size=$(printf "%s\n" "${sizes[@]}" | awk '{x[NR]=$1; sum+=$1} END {mean=sum/NR; for(i=1;i<=NR;i++)s+=(x[i]-mean)^2; printf "%d", sqrt(s/NR)}')
                    # Save timing to CSV
                    echo "$type,$events,$format,$algo,$level,$avg_time,$stdev_time,$avg_size,$stdev_size" >> "$output_file"

                    # Notify completion
                    notify-complete "step4_recompress.sh completed for Phase2 $type with $events events in $format format with $algo compression level $level."
                done
            done
        done
    done
done
notify-complete "step4_recompress.sh completed."
