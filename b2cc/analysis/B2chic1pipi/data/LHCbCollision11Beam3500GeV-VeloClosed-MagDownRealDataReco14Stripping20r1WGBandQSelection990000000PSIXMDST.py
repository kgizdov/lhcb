#-- GAUDI jobOptions generated on Thu Feb 19 11:43:25 2015
#-- Contains event types : 
#--   90000000 - 58 files - 6600344 events - 283.09 GBytes


#--  Extra information about the data processing phases:


#--  Processing Pass Step-125603 

#--  StepId : 125603 
#--  StepName : Merging for WGBandQSelection 
#--  ApplicationName : DaVinci 
#--  ApplicationVersion : v33r6p1 
#--  OptionFiles : $APPCONFIGOPTS/Merging/DV-Stripping-Merging.py 
#--  DDDB : None 
#--  CONDDB : None 
#--  ExtraPackages : AppConfig.v3r177 
#--  Visible : N 

from Gaudi.Configuration import * 
from GaudiConf import IOHelper
IOHelper('ROOT').inputFiles(['LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000001_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000002_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000003_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000004_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000005_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000006_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000007_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000008_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000009_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000010_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000011_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000012_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000013_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000014_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000015_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000016_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000017_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000018_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000019_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000020_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000021_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000022_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000023_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000024_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000025_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000026_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000027_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000028_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000029_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000030_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000031_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000033_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000034_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000035_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000036_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000037_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000038_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000039_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000040_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000041_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000042_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000043_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000044_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000045_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000046_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000047_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000048_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000049_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000050_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000051_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000052_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000053_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000054_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000055_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000056_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000057_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000058_1.psix.mdst',
'LFN:/lhcb/LHCb/Collision11/PSIX.MDST/00041161/0000/00041161_00000059_1.psix.mdst'
], clear=True)
