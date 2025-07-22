import FWCore.ParameterSet.Config as cms

import sys
import re

if len(sys.argv) < 4:
    raise RuntimeError("Usage: cmsRun step4_compression_TTree.py filename compression_algorithm compression_level")

filename = sys.argv[1]
compression_algorithm = sys.argv[2]
compression_level = int(sys.argv[3])
if compression_algorithm not in ["LZMA", "ZLIB", "LZ4", "ZSTD", "uncompressed"]:
    raise RuntimeError(f"Compression must be either LZMA, ZLIB, LZ4, ZSTD or uncompressed. Input was {compression_algorithm}")

if compression_level < 0 or compression_level > 9:
    raise RuntimeError(f"Compression level must be between 0 and 9. Input was {compression_level}")

# filename = data_RAW_RNTuple_1000.root

match = re.match(r"(.*)_(\d+)\.root", filename)
if match:
    name_prefix = match.group(1)
    num_events = int(match.group(2))

output_filename = name_prefix + '_' + str(num_events) + '_' +  compression_algorithm + '_' + str(compression_level) + '.root'
if compression_algorithm == "uncompressed":
    output_filename = name_prefix + '_' + str(num_events) + '_' +  compression_algorithm + '.root'

process = cms.Process("reCompress")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:../store/uncompressed/' + filename),
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(num_events),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

process.consumer = cms.EDAnalyzer("GenericConsumer",
    eventProducts = cms.untracked.vstring("*")
)

# Output definition

process.output = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string(compression_algorithm),
    compressionLevel = cms.untracked.int32(compression_level),
    fileName = cms.untracked.string(f'file:../store/compressed/phase2/{output_filename}'),
    fastCloning = cms.untracked.bool(False)
)

process.end_step = cms.EndPath(process.output)