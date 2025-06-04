import FWCore.ParameterSet.Config as cms

import sys

if len(sys.argv) < 3:
    raise RuntimeError("Usage: cmsRun step3_PARKING.py <filename> <num_events>")

filename = sys.argv[1]
num_events = int(sys.argv[2])


process = cms.Process("READ")

process.options.wantSummary = cms.untracked.bool(True)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:../store/uncompressed/' + filename),
    delayReadingEventProducts = cms.untracked.bool(False)
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(num_events)
)

process.consumer = cms.EDAnalyzer("GenericConsumer",
    eventProducts = cms.untracked.vstring("*")
)

