#!/bin/bash

for num_events in {0..99}; do
    echo "Running event $num_events in TTree format ..."

    filename="step3_RAW_TTree_100.root"
    # Run command, save log, and time it
    cmsRun step4_splitEvents_TTree.py "$filename"  $num_events

    filename="step3_RAW_TTree_$num_events.root"

    cmsRun step4_convert_RNTuple.py "$filename" 1

done

notify-complete "step4_splitEvents_TTree.py completed."