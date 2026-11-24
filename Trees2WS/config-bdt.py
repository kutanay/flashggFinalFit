# Input config file for running trees2ws

trees2wsCfg = {

  # Name of RooDirectory storing input tree
  'inputTreeDir':'DiphotonTree',
 #CMS_hgg_mass, is the 4-photon invariant mass, name was left unchanged
  # Variables to be added to dataframe: use wildcard * for common strings
  #'mainVars':["CMS_hgg_mass","weight","weight_*","dZ"],
  'mainVars':["CMS_hgg_mass","weight","weight_central","weight_nominal","dZ","weight_*Up","weight_*Down"], # Var for the nominal RooDataSets, -kt dZ is not required for the analysis but is kept for technical reasons based on how the code is written later on for finalfits
  'dataVars':["CMS_hgg_mass","weight"], # Vars to be added for data
  'stxsVar':'', # -kt, not used
  'systematicsVars':["CMS_hgg_mass","weight"], # Variables to add to sytematic RooDataHists, 
  #'theoryWeightContainers':{},
  'theoryWeightContainers':{'weight_LHEPdf': 99, 'weight_LHEScale_muF' : 3 , 'weight_LHEScale_muR' : 3},
  # List of systematics: use string YEAR for year-dependent systematics
  'systematics':["FNUF","Material","SmearingIJaZ","ScaleIJaZ"],

  # Analysis categories: python list of cats or use 'auto' to extract from input tree
  'cats':'auto'

}
