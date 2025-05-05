# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 -s DIGI:pdigi_valid,DATAMIX,L1,DIGI2RAW,HLT:@relval2025 --nThreads 1 --conditions auto:phase1_2025_realistic --datatier GEN-SIM-DIGI-RAW -n 1000 --eventcontent PREMIXRAW --geometry DB:Extended --era Run3_2025 --datamix PreMix --procModifiers premix_stage2 --filein file:step1.root --pileup_input file:step2.root --fileout file:step3.root --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_2025_cff import Run3_2025
from Configuration.ProcessModifiers.premix_stage2_cff import premix_stage2

import sys

if len(sys.argv) < 4:
    raise RuntimeError("Usage: cmsRun step3_PARKING.py <compression> <level> <num_events> <basedir>")

if sys.argv[1] not in ["LZMA", "ZLIB", "LZ4", "ZSTD"]:
    raise RuntimeError(f"Compression must be either LZMA, ZLIB, LZ4, or ZSTD. Input was {sys.argv[1]}")

if int(sys.argv[2]) < 0 or int(sys.argv[2]) > 9:
    raise RuntimeError(f"Compression level must be between 0 and 9. Input was {sys.argv[2]}")

if int(sys.argv[3]) <= 0:
    raise RuntimeError(f"Number of events must be greater than 0. Input was {sys.argv[3]}")

compression = sys.argv[1]
level = int(sys.argv[2])
num_events = int(sys.argv[3])
basedir = sys.argv[4]


process = cms.Process('PARKING',Run3_2025,premix_stage2)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.DigiDM_cff')
process.load('Configuration.StandardSequences.DataMixerPreMix_cff')
process.load('Configuration.StandardSequences.SimL1EmulatorDM_cff')
process.load('Configuration.StandardSequences.DigiToRawDM_cff')
process.load('HLTrigger.Configuration.HLT_GRun_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(num_events),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:step3_RAWSIM_UNCOMP.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    TryToContinue = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToCallForTryToContinue = cms.untracked.vstring(),
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:1000'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Daq director

# process.EvFDaqDirector = cms.Service( "EvFDaqDirector",
#     baseDir = cms.untracked.string( "." ),
#     buBaseDir = cms.untracked.string( "." ),
#     buBaseDirsAll = cms.untracked.vstring(  ),
#     buBaseDirsNumStreams = cms.untracked.vint32(  ),
#     runNumber = cms.untracked.uint32( 386925 ),
#     useFileBroker = cms.untracked.bool( True ),
#     fileBrokerHostFromCfg = cms.untracked.bool( True ),
#     fileBrokerHost = cms.untracked.string( "InValid" ),
#     fileBrokerPort = cms.untracked.string( "8080" ),
#     fileBrokerKeepAlive = cms.untracked.bool( True ),
#     fileBrokerUseLocalLock = cms.untracked.bool( True ),
#     fuLockPollInterval = cms.untracked.uint32( 2000 ),
#     outputAdler32Recheck = cms.untracked.bool( False ),
#     directorIsBU = cms.untracked.bool( False ),
#     hltSourceDirectory = cms.untracked.string( "" ),
#     mergingPset = cms.untracked.string( "" )
# )

process.EvFDaqDirector = cms.Service("EvFDaqDirector",
  runNumber= cms.untracked.uint32(1),
  baseDir = cms.untracked.string("./" + basedir),
  buBaseDir = cms.untracked.string("./" + basedir),
  # HLTD picks up HLT configuration and fffParameters.jsn from hltSourceDirectory (copied by newHiltonMenu.py)
  hltSourceDirectory = cms.untracked.string(""),
  directorIsBU = cms.untracked.bool(True),
)


process.FastMonitoringService = cms.Service( "FastMonitoringService",
    tbbMonitoringMode = cms.untracked.bool( True ),
    tbbConcurrencyTracker = cms.untracked.bool( True ),
    sleepTime = cms.untracked.int32( 1 ),
    fastMonIntervals = cms.untracked.uint32( 2 ),
    filePerFwkStream = cms.untracked.bool( False ),
    verbose = cms.untracked.bool( False )
)

# Output definition

process.PREMIXRAWoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step3.root'),
    outputCommands = process.PREMIXRAWEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition
process.RAWoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step3_RAW.root'),
    outputCommands = cms.untracked.vstring(
    'drop *',
    'keep FEDRawDataCollection_rawDataCollector_*_*'
    ),
    splitLevel = cms.untracked.int32(0)
)

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RAW'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step3_RAWSIM.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

process.ParkingLikeOutput = cms.OutputModule( "GlobalEvFOutputModule",
    use_compression = cms.untracked.bool( False if level == 0 else True ),
    compression_algorithm = cms.untracked.string( compression ),
    compression_level = cms.untracked.int32( level ),
    # dataset = cms.untracked.PSet(
    #     dataTier = cms.untracked.string( "GEN-SIM-RAW" ),
    #     filterName = cms.untracked.string( "" )
    # ),
    outputCommands = cms.untracked.vstring( 'drop *',
      'keep FEDRawDataCollection_rawDataCollector_*_*',
      'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
      'keep edmTriggerResults_*_*_*',
      'keep triggerTriggerEvent_*_*_*' ),
    psetMap = cms.untracked.InputTag( "hltPSetMap" ),
)

# Other statements
process.mix.digitizers = cms.PSet(process.theDigitizersValid)
process.mixData.input.fileNames = cms.untracked.vstring(['file:step2.root'])
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2025_realistic', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi_valid)
process.datamixing_step = cms.Path(process.pdatamix)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.PREMIXRAWoutput_step = cms.EndPath(process.PREMIXRAWoutput)
process.RAWoutput_step = cms.EndPath(process.RAWoutput)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)
process.ParkingLikeOutput_step = cms.EndPath(process.ParkingLikeOutput)

# Schedule definition
# process.schedule imported from cff in HLTrigger.Configuration
# process.schedule.insert(0, process.digitisation_step)
# process.schedule.insert(1, process.datamixing_step)
# process.schedule.insert(2, process.L1simulation_step)
# process.schedule.insert(3, process.digi2raw_step)
# process.schedule.extend([process.endjob_step,process.PREMIXRAWoutput_step,process.RAWoutput_step])
# process.schedule.extend([process.endjob_step,process.RAWSIMoutput_step])
# process.schedule.extend([process.endjob_step,process.RAWoutput_step])
process.schedule.extend([process.endjob_step,process.ParkingLikeOutput_step])
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# End of customisation functions


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
