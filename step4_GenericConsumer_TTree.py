import FWCore.ParameterSet.Config as cms

import sys

if len(sys.argv) < 2:
    raise RuntimeError("Usage: cmsRun step3_PARKING.py <filename>")

filename = sys.argv[1]
num_events = int(sys.argv[2])


process = cms.Process("READ")

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

