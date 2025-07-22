import FWCore.ParameterSet.Config as cms

import sys
import glob

if len(sys.argv) < 2:
    raise RuntimeError("Usage: cmsRun step3_Phase2_uncompressed_TTree.py <num_events>")

if int(sys.argv[1]) <= 0:
    raise RuntimeError(f"Number of events must be greater than 0. Input was {sys.argv[1]}")

num_events = int(sys.argv[1])
files = glob.glob("../store/TTbar_step2/*.root")
file_list = ["file:" + f for f in files]

process = cms.Process("RAW")

# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring(*file_list),
    inputCommands = cms.untracked.vstring(
        'drop *',
        'keep *_simSiPixelDigis_*_*',
        'drop PixelDigiSimLinkedmDetSetVector_*_*_*',
        'keep *_mix_Tracker_*',
        'keep *_simEcalDigis_*_*',
        'keep *_simHcalDigis_*_*',
        'keep *_simHGCalUnsuppressedDigis_*_*',
        'keep *_mix_FTLBarrel_*',
        'keep *_mix_FTLEndcap_*',
    ),
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
    fileName = cms.untracked.string(f'file:../store/uncompressed/mc_Phase2_TTree_{num_events}.root'),
    fastCloning = cms.untracked.bool(False)
)

process.options.numberOfThreads = 30

process.RNTupleRAWoutput_step = cms.EndPath(process.RAWRNTupleoutput)
