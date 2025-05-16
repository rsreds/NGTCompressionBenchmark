# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 -s GEN,SIM,DIGI:pdigi_valid --nThreads 30 -n 1000 --conditions auto:phase1_2025_realistic --beamspot DBrealistic --datatier PREMIX --eventcontent PREMIX --geometry DB:Extended --era Run3_2025 --pileup Run3_Flat55To75_PoissonOOTPU --pileup_input das:/RelValMinBias_14TeV/CMSSW_15_0_0_pre1-142X_mcRun3_2025_realistic_v1_STD_RegeneratedGS_2025_noPU-v1/GEN-SIM --procModifiers premix_stage1 --relval 100000,100 --evt_type SingleNuE10_cfi --fileout file:step2.root --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_2025_cff import Run3_2025
from Configuration.ProcessModifiers.premix_stage1_cff import premix_stage1

process = cms.Process('DIGI',Run3_2025,premix_stage1)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_Run3_Flat55To75_PoissonOOTPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(5000),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("EmptySource")

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
    annotation = cms.untracked.string('SingleNuE10_cfi nevts:1000'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.PREMIXoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('PREMIX'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:../store/step2_PUPremix_Run3.root'),
    outputCommands = process.PREMIXEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.input.fileNames = cms.untracked.vstring(['/store/relval/CMSSW_15_0_0_pre1/RelValMinBias_14TeV/GEN-SIM/142X_mcRun3_2025_realistic_v1_STD_RegeneratedGS_2025_noPU-v1/2590000/2fbe8484-6bf1-40e7-8d56-85b9979f76dc.root', '/store/relval/CMSSW_15_0_0_pre1/RelValMinBias_14TeV/GEN-SIM/142X_mcRun3_2025_realistic_v1_STD_RegeneratedGS_2025_noPU-v1/2590000/531b0b9f-913f-49e9-a85a-c8fb6d07ae33.root', '/store/relval/CMSSW_15_0_0_pre1/RelValMinBias_14TeV/GEN-SIM/142X_mcRun3_2025_realistic_v1_STD_RegeneratedGS_2025_noPU-v1/2590000/5b53992d-8591-4258-922a-209480377a90.root', '/store/relval/CMSSW_15_0_0_pre1/RelValMinBias_14TeV/GEN-SIM/142X_mcRun3_2025_realistic_v1_STD_RegeneratedGS_2025_noPU-v1/2590000/5d15e0d8-d832-4064-aa4c-211c21475f99.root', '/store/relval/CMSSW_15_0_0_pre1/RelValMinBias_14TeV/GEN-SIM/142X_mcRun3_2025_realistic_v1_STD_RegeneratedGS_2025_noPU-v1/2590000/764b6505-2927-4e62-a087-660999e39ee3.root', '/store/relval/CMSSW_15_0_0_pre1/RelValMinBias_14TeV/GEN-SIM/142X_mcRun3_2025_realistic_v1_STD_RegeneratedGS_2025_noPU-v1/2590000/c2e16bb3-3611-412b-908b-79c0e537a06c.root'])
if hasattr(process, "XMLFromDBSource"): process.XMLFromDBSource.label="Extended"
if hasattr(process, "DDDetectorESProducerFromDB"): process.DDDetectorESProducerFromDB.label="Extended"
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
process.mix.digitizers = cms.PSet(process.theDigitizersValid)
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2025_realistic', '')

process.generator = cms.EDProducer("FlatRandomEGunProducer",
    AddAntiParticle = cms.bool(False),
    PGunParameters = cms.PSet(
        MaxE = cms.double(10.01),
        MaxEta = cms.double(2.5),
        MaxPhi = cms.double(3.14159265359),
        MinE = cms.double(9.99),
        MinEta = cms.double(-2.5),
        MinPhi = cms.double(-3.14159265359),
        PartID = cms.vint32(12)
    ),
    Verbosity = cms.untracked.int32(0),
    firstRun = cms.untracked.uint32(1),
    psethack = cms.string('single Nu E 10')
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.digitisation_step = cms.Path(process.pdigi_valid)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.PREMIXoutput_step = cms.EndPath(process.PREMIXoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.digitisation_step,process.endjob_step,process.PREMIXoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads = 30
process.options.numberOfStreams = 0
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path).insert(0, process.generator)



# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
