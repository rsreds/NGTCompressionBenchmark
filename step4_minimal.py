import FWCore.ParameterSet.Config as cms

process = cms.Process("LHCX")

process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('auto generated configuration'),
    name = cms.untracked.string('repack-config'),
    version = cms.untracked.string('none')
)


process.source = cms.Source("NewEventStreamFileReader",
    fileNames = cms.untracked.vstring(
        # 'file:/eos/cms/store/t0streamer/Data/ParkingVBF2/000/386/925/run386925_ls0001_streamParkingVBF2_StorageManager.dat',
        # 'file:/eos/cms/store/t0streamer/Data/ParkingVBF2/000/386/925/run386925_ls0002_streamParkingVBF2_StorageManager.dat'
        'file:test.dat'
    ),
    overrideCatalog = cms.untracked.string('T2_CH_CERN,,T0_CH_CERN,CERN_EOS_T0,XRootD')
)

process.output = cms.OutputModule( "PoolOutputModule",
                                   fileName = cms.untracked.string( "step4.root" )
)

process.end = cms.EndPath( process.output ) 