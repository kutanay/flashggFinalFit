#!/bin/bash
ulimit -s unlimited
set -e
cd /eos/home-t/takumar/gitcode/higgsdna_finalfits_tutorial_24/07_FinalFits/CMSSW_14_1_0_pre4/src
export SCRAM_ARCH=el9_amd64_gcc12
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`
cd /eos/home-t/takumar/gitcode/higgsdna_finalfits_tutorial_24/07_FinalFits/CMSSW_14_1_0_pre4/src/flashggFinalFit/Background
export PYTHONPATH=$PYTHONPATH:/eos/home-t/takumar/gitcode/higgsdna_finalfits_tutorial_24/07_FinalFits/CMSSW_14_1_0_pre4/src/flashggFinalFit/tools:/eos/home-t/takumar/gitcode/higgsdna_finalfits_tutorial_24/07_FinalFits/CMSSW_14_1_0_pre4/src/flashggFinalFit/Background/tools

/eos/home-t/takumar/gitcode/higgsdna_finalfits_tutorial_24/07_FinalFits/CMSSW_14_1_0_pre4/src/flashggFinalFit/Background/runBackgroundScripts.sh -i /eos/home-t/takumar/gitcode/higgsdna_finalfits_tutorial_24/07_FinalFits/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs/2024_data/30_GeV/Data/ws/allData_Data2024.root -p none -f CAT1 --ext bdt-30-2024 --catOffset 0 --intLumi 109.0 --year 2024 --batch local --queue espresso --sigFile none --isData --fTest
