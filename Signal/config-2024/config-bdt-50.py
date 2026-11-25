# Config file: options for signal fitting

_year = '2024'

signalScriptCfg = {

  # Setup
  'inputWSDir':'/eos/home-t/takumar/gitcode/higgsdna_finalfits_tutorial_24/07_FinalFits/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs/2024_full_nov9_qcd_pdf/50_GeV/forws/ws_ma50',
  'procs':'auto', # if auto: inferred automatically from filenames
  'cats':'auto', # if auto: inferred automatically from (0) workspace
  'ext':'bdt-50-2024_aug28',
  'analysis':'tutorial', # To specify which replacement dataset mapping (defined in ./python/replacementMap.py)
  'year':'2024', # Use 'combined' if merging all years: not recommended
  'massPoints':'125',

  #Photon shape systematics  
  'scales':'ScaleIJaZ,FNUF,Material' , # separate nuisance per year
  'scalesCorr':'', # correlated across years
  'scalesGlobal':'NonLinearity', # affect all processes equally, correlated across years
  'smears':'SmearingIJaZ' , # separate nuisance per year

  # Job submission options
  'batch':'local', # ['condor','SGE','IC','local']
  'queue':'espresso',

}

