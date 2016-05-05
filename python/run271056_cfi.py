import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( ['/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/046FE964-FD08-E611-A8C8-02163E0139BA.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/06066B66-0909-E611-A688-02163E0146A9.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/0867B60F-0C09-E611-BAF6-02163E012209.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/08F4DE41-0609-E611-9E11-02163E0146F6.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/0A218E0C-1C09-E611-B1C8-02163E014308.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/0A8ED6DD-0D09-E611-982E-02163E012AA8.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/0C30BBDB-FF08-E611-A2CE-02163E012B4D.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/0CB3B3A2-1C09-E611-93D3-02163E0144F0.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/0E31F1C3-0B09-E611-B0F1-02163E0120F6.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/105ECFE9-F608-E611-8B6D-02163E0141C3.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/14439FC1-0B09-E611-A8CF-02163E014308.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/1A87C00F-0C09-E611-BB2E-02163E011AC3.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/22160A6E-0909-E611-B29A-02163E0140D5.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/22D89252-FD08-E611-BE4E-02163E013462.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/2A163FFA-0309-E611-95B0-02163E01436C.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/2A3943B9-FF08-E611-AE47-02163E012AA8.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/30860853-FD08-E611-A591-02163E0145E6.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/348E77AE-F408-E611-AFBE-02163E011CDA.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/3681ABED-FF08-E611-8DDB-02163E01413C.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/368FDBCA-1B09-E611-8923-02163E011999.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/3A970824-0C09-E611-B2D9-02163E01452B.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/3CD03DEE-0309-E611-915D-02163E0140F8.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/40F80966-FD08-E611-83CC-02163E011E3C.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/40FF4EA5-0D09-E611-B48D-02163E012B1F.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/4253DE06-1C09-E611-BD3C-02163E0140E2.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/42D015A7-F408-E611-AB46-02163E0138AC.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/464C9BDC-0909-E611-84B9-02163E011E2A.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/4A76F680-0909-E611-B621-02163E011CA3.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/4C28DFA3-0D09-E611-9DD5-02163E013745.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/4E449F0D-0C09-E611-B057-02163E011DF9.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/4E6715C9-1B09-E611-945D-02163E011D1E.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/56C334E8-0A09-E611-8F6E-02163E013513.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/56EEBDB0-0B09-E611-9D9A-02163E01340D.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/589561E8-0909-E611-80B4-02163E014179.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/5A096037-0009-E611-86B0-02163E014330.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/5A1B61CE-0A09-E611-88F3-02163E0146F6.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/5C0A411C-0509-E611-BB87-02163E0140F8.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/5CE1C518-0C09-E611-88C8-02163E0133AE.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/60101DE3-1B09-E611-8C8C-02163E011DB6.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/6270A7FC-0B09-E611-9289-02163E012642.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/6477B255-0309-E611-8D67-02163E0146F6.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/66ACB107-0C09-E611-92C0-02163E01359B.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/66C411FB-0909-E611-9DD6-02163E0140F8.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/6AD3991C-0C09-E611-9CD7-02163E01436C.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/6EB0B222-0C09-E611-9313-02163E01370C.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/722BE11A-0C09-E611-9798-02163E0146A9.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/767E58BE-0D09-E611-8EBB-02163E0141C3.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/76F6C4C4-0909-E611-8474-02163E013959.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/7AA3AA35-0C09-E611-9CA6-02163E013513.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/7C3C76C3-0D09-E611-8B5D-02163E012B1F.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/84CE48D6-0B09-E611-AF1C-02163E011A01.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/869A29E5-1B09-E611-AF63-02163E0144F4.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/8AA80EB6-0D09-E611-A856-02163E011DB6.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/8E9CCB4B-0909-E611-A155-02163E01340D.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/92EA39D5-0A09-E611-8924-02163E0140D5.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/9471E5CD-0A09-E611-9B05-02163E0133B8.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/9A81B6C9-FF08-E611-ADDF-02163E014539.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/9CD8B852-FD08-E611-9F0A-02163E011A88.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/A04F9113-0C09-E611-B890-02163E0143FC.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/A2E76905-0C09-E611-BF8E-02163E01391D.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/A680A6CE-0909-E611-B687-02163E0133B8.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/A865CFCA-1B09-E611-A9C0-02163E011A71.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/AA9DEDA3-0D09-E611-ACED-02163E011DF9.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/AA9F5E4E-0909-E611-BFA0-02163E011FE5.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/AAC4D8BB-0B09-E611-8B08-02163E0133B8.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/AADA3997-0909-E611-A7E3-02163E0120F6.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/B4707913-1C09-E611-8738-02163E012A7C.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/B8365F5D-0909-E611-81BC-02163E013489.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/B8BFAF8F-FD08-E611-B176-02163E013984.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/BC5C16DC-0D09-E611-A883-02163E01340D.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/BCB118FF-0B09-E611-9577-02163E0135CD.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/C6C11120-0509-E611-ACE4-02163E013959.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/CEE5D8CF-1B09-E611-A54D-02163E0128EB.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/D2D6AE3D-0609-E611-8F7D-02163E013906.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/D6608654-FD08-E611-95C0-02163E0141F4.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/D881B7EB-1B09-E611-9DBD-02163E0141B5.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/DC71DEE4-1B09-E611-99D2-02163E0146F6.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/DCAFBCD2-1B09-E611-B5C8-02163E0140D5.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/DCF922BF-0B09-E611-BF00-02163E011CA3.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/DE119AC2-F408-E611-9F64-02163E013955.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/E4B6DABB-0A09-E611-ABFE-02163E011E2A.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/E6BFC36B-FD08-E611-86E4-02163E013575.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/E8C188A6-0D09-E611-9AEA-02163E01340D.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/EAC2BD88-FD08-E611-86F8-02163E01236F.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/EE45553F-0509-E611-8C95-02163E014308.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/F27F15D2-0A09-E611-A880-02163E014179.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/F2828137-0E09-E611-99D4-02163E014665.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/F43A4E07-1C09-E611-B50B-02163E0144F0.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/F4892C07-1C09-E611-A040-02163E011E2A.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/F6901826-1C09-E611-91E3-02163E01466D.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/F8024C8C-0909-E611-BCDD-02163E0140F8.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/FA2DF708-0A09-E611-BFBD-02163E0120F6.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/FCDD62D6-0A09-E611-881A-02163E0138EC.root',
       '/store/data/Run2016A/MinimumBias/RAW/v1/000/271/056/00000/FE0774AF-0D09-E611-86AE-02163E011A01.root'
                   ]);
secFiles.extend( [
        ] )
