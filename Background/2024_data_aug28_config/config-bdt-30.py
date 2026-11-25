backgroundScriptCfg = {

  # Setup
  'inputWS':'/eos/home-t/takumar/gitcode/higgsdna_finalfits_tutorial_24/07_FinalFits/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs/2024_data_aug28/30_GeV/Data/ws/allData_Data2024.root', # location of 'allData.root' file
  'cats':'auto', # auto: automatically inferred from input ws
  'catOffset':0, # add offset to category numbers (useful for categories from different allData.root files)  
  'ext':'bdt-30-2024_aug28', # extension to add to output directory
  'year':'2024', # Use combined when merging all years in category (for plots)

  # Job submission options
  'batch':'local', # [condor,SGE,IC,local]
  'queue':'espresso' # for condor e.g. microcentury

}
