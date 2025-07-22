import FWCore.ParameterSet.Config as cms

import sys

if len(sys.argv) < 2:
    raise RuntimeError("Usage: cmsRun step3_PARKING.py num_events")

if int(sys.argv[1]) < 0:
    raise RuntimeError(f"Number of events to skip must be positive. Input was {sys.argv[1]}")

num_events = int(sys.argv[1])

process = cms.Process("RAW")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:../store/772d714f-fda4-4a82-a98d-e1a07d65d36a.root'),
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(num_events),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Output definition

process.RAWRNTupleoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('uncompressed'),
    compressionLevel = cms.untracked.int32(0),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string(f'file:../store/uncompressed/data_RAW_TTree_{num_events}.root'),
    outputCommands = cms.untracked.vstring(
    'drop *',
    'keep FEDRawDataCollection_rawDataCollector_*_*'
    ),
    fastCloning = cms.untracked.bool(False)
)

process.options.numberOfThreads = 30

process.RNTupleRAWoutput_step = cms.EndPath(process.RAWRNTupleoutput)
