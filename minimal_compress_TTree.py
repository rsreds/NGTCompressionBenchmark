import FWCore.ParameterSet.Config as cms

process = cms.Process("reCompress")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:RAW_TTree_1000.root'),
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

process.output = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string("ZSTD"),
    compressionLevel = cms.untracked.int32(3),
    fileName = cms.untracked.string(f'file:RAW_TTree_1000_ZSTD3.root')
)

process.end_step = cms.EndPath(process.output)
