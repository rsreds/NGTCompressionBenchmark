import FWCore.ParameterSet.Config as cms

import sys

if len(sys.argv) < 3:
    raise RuntimeError("Usage: cmsRun step3_PARKING.py filename num_events")

if int(sys.argv[2]) < 0:
    raise RuntimeError(f"Number of events to skip must be positive. Input was {sys.argv[1]}")

filename = sys.argv[1]
num_events = int(sys.argv[2])

output_filename = filename.replace('TTree', 'RNTuple')

print(f"Input file: {filename}")
print(f"Number of events: {num_events}")
print(f"Output file: {output_filename}")

process = cms.Process("SPLIT")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:../store/splitEvents/TTree/' + filename),
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(num_events),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Output definition

process.RAWRNTupleoutput = cms.OutputModule("RNTupleOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(0),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string(f'file:../store/splitEvents/RNTuple/{output_filename}'),
    outputCommands = cms.untracked.vstring(
    'keep *',
    )
)

process.RNTupleRAWoutput_step = cms.EndPath(process.RAWRNTupleoutput)
