import FWCore.ParameterSet.Config as cms

import sys

if len(sys.argv) < 2:
    raise RuntimeError("Usage: cmsRun step3_PARKING.py <filename>")

filename = sys.argv[1]

process = cms.Process("READ")

process.source = cms.Source("RNTupleSource",
    fileNames = cms.untracked.vstring('file:../store/uncompressed/' + filename),
    delayReadingEventProducts = cms.untracked.bool(False)
)

process.consumer = cms.EDAnalyzer("GenericConsumer",
    eventProducts = cms.untracked.vstring("*")
)

