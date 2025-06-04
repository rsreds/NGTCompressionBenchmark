#!/bin/bash

# Output CSV file
output_file="../results/complete_timing_results_recompress.csv"
echo "type,events,format,algo,level,time_seconds,filesize_byte" > "$output_file"

# List of event counts
for events in 1 10 100 1000; do
    for type in "data" "mc"; do
        for format in "TTree" "RNTuple"; do
            for algo in "LZMA" "ZSTD" "ZLIB" "LZ4"; do
                for level in 1 2 3 4 5 6 7 8 9; do
                    echo "Running $type with $events events in $format format with $algo compression level $level ..."

                    log_file="../store/compressed/logs/${type}_compress_${format}_${events}_${algo}_${level}.log"
                    filename="${type}_RAW_${format}_${events}.root"
                    # Run command, save log, and time it
                    time_output=$( ( /usr/bin/time -f "%e" cmsRun step4_compress_"$format".py "$filename" "$algo" "$level"  ) &> "$log_file" 2>&1 )
                    run_time=$(tail -1 $log_file)
                    outfilename="../store/compressed/${type}/${type}_RAW_${format}_${events}_${algo}_${level}.root"
                    file_size=$(du "$outfilename" | cut -f1)
                    # Save timing to CSV
                    echo "$type,$events,$format,$algo,$level,$run_time,$file_size">> "$output_file"

                    # Notify completion
                done
            done
        done
    done
done
notify-complete "step4_recompress.sh for mc completed."
