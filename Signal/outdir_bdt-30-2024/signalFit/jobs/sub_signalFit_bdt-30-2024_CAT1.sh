#!/bin/bash
ulimit -s unlimited
set -e
cd /eos/home-t/takumar/gitcode/higgsdna_finalfits_tutorial_24/07_FinalFits/CMSSW_14_1_0_pre4/src
export SCRAM_ARCH=el9_amd64_gcc12
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`
cd /eos/home-t/takumar/gitcode/higgsdna_finalfits_tutorial_24/07_FinalFits/CMSSW_14_1_0_pre4/src/flashggFinalFit/Signal
export PYTHONPATH=$PYTHONPATH:/eos/home-t/takumar/gitcode/higgsdna_finalfits_tutorial_24/07_FinalFits/CMSSW_14_1_0_pre4/src/flashggFinalFit/tools:/eos/home-t/takumar/gitcode/higgsdna_finalfits_tutorial_24/07_FinalFits/CMSSW_14_1_0_pre4/src/flashggFinalFit/Signal/tools

python3 /eos/home-t/takumar/gitcode/higgsdna_finalfits_tutorial_24/07_FinalFits/CMSSW_14_1_0_pre4/src/flashggFinalFit/Signal/scripts/signalFit.py --inputWSDir /eos/home-t/takumar/gitcode/higgsdna_finalfits_tutorial_24/07_FinalFits/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs/2024/30_GeV/forws/ws_ma30 --ext bdt-30-2024 --proc ma30 --cat CAT1 --year 2024 --analysis tutorial --massPoints 125 --scales 'ScaleIJaZ,FNUF,Material' --scalesCorr '' --scalesGlobal 'NonLinearity,Geant4' --smears 'SmearingIJaZ' --doPlots --nBins 640 --skipVertexScenarioSplit

