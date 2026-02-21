backgroundScriptCfg = {

  # Setup
  'inputWS':'/eos/home-t/takumar/gitcode/higgsdna_finalfits_tutorial_24/07_FinalFits/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs/may26/Data/ws/allData_Data2022C.root', # location of 'allData.root' file
  'cats':'auto', # auto: automatically inferred from input ws
  'catOffset':0, # add offset to category numbers (useful for categories from different allData.root files)  
  'ext':'datacard_may26_mva', # extension to add to output directory
  'year':'2022preEE', # Use combined when merging all years in category (for plots)

  # Job submission options
  'batch':'local', # [condor,SGE,IC,local]
  'queue':'espresso' # for condor e.g. microcentury

}
