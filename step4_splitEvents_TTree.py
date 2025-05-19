import FWCore.ParameterSet.Config as cms

import sys

if len(sys.argv) < 3:
    raise RuntimeError("Usage: cmsRun step3_PARKING.py filename num_events")

if int(sys.argv[2]) < 0:
    raise RuntimeError(f"Number of events to skip must be positive. Input was {sys.argv[1]}")

filename = sys.argv[1]
num_events = int(sys.argv[2])

process = cms.Process("SPLIT")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:../store/uncompressed/' + filename),
)

process.source.skipEvents = cms.untracked.uint32(num_events)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Output definition

process.RAWRNTupleoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(0),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string(f'file:../store/splitEvents/TTree/step3_RAW_TTree_{num_events}.root'),
    outputCommands = cms.untracked.vstring(
    'drop *',
    'keep FEDRawDataCollection_rawDataCollector_*_*'
    )
)

process.RNTupleRAWoutput_step = cms.EndPath(process.RAWRNTupleoutput)
