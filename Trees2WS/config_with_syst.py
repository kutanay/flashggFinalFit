# Input config file for running trees2ws

trees2wsCfg = {

  # Name of RooDirectory storing input tree
  'inputTreeDir':'DiphotonTree',

  # Variables to be added to dataframe: use wildcard * for common strings
  'mainVars':["CMS_hgg_mass","weight","dZ","weight_*"], # Var for the nominal RooDataSets
  'dataVars':["CMS_hgg_mass","weight"], # Vars to be added for data
  'stxsVar':'',
  'systematicsVars':["CMS_hgg_mass","weight"], # Variables to add to sytematic RooDataHists
  'theoryWeightContainers':{},

  # List of systematics: use string YEAR for year-dependent systematics
  'systematics':["Smearing"],

  # Analysis categories: python list of cats or use 'auto' to extract from input tree
  'cats':'auto'

}

