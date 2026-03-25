import ROOT
import os

ROOT.gROOT.SetBatch(True)

mass_points = range(15, 63)

base_path = (
    "/eos/home-t/takumar/gitcode/higgsdna_finalfits_tutorial_24/"
    "07_FinalFits/CMSSW_14_1_0_pre4/src/flashggFinalFit/Background/"
    "outdir_bdt-{}-2024/CMS-HGG_multipdf_CAT1.root"
)

output_file = "background_yields_115_135.txt"

def get_background_yield(file_path):
    f = ROOT.TFile.Open(file_path)
    w = f.Get("multipdf")
    mass = w.var("CMS_hgg_mass")
    pdf  = w.pdf("CMS_hgg_CAT1_2024_13TeV_bkgshape")
    norm = w.var("CMS_hgg_CAT1_2024_13TeV_bkgshape_norm")

    mass.setRange("FULL", 110.0, 180.0)
    mass.setRange("SR",   115.0, 135.0)

    int_sr = pdf.createIntegral(
        ROOT.RooArgSet(mass),
        ROOT.RooFit.Range("SR")
    )

    int_full = pdf.createIntegral(
        ROOT.RooArgSet(mass),
        ROOT.RooFit.Range("FULL")
    )

    frac = int_sr.getVal() / int_full.getVal()
    yield_sr = norm.getVal() * frac

    f.Close()

    return yield_sr

results = []

for m in mass_points:
    path = base_path.format(m)
    y = get_background_yield(path)
    results.append(y)
    print(f"MA{m} : {y}")

with open(output_file, "w") as f:
    f.write("Expected background yields in 115–135 GeV\n\n")
    for i, m in enumerate(mass_points):
        f.write(f"MA{m} : {results[i]}\n")
    f.write("\n\n# Python array (copy-paste ready)\n")
    f.write("bkg_yields = [\n")
    for y in results:
        f.write(f"    {y},\n")
    f.write("]\n")

print(f"\nSaved results to {output_file}")
