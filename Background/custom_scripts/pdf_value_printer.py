import ROOT
import numpy as np


file = ROOT.TFile.Open("CMS-HGG_multipdf_CAT1.root")
ws = file.Get("multipdf")

mass = ws.var("CMS_hgg_mass")
multipdf = ws.pdf("CMS_hgg_CAT1_2024_13TeV_bkgshape")
index_cat = ws.cat("pdfindex_CAT1_2024_13TeV")


n_pdfs = index_cat.numTypes()


for i in range(n_pdfs):
    index_cat.setIndex(i)
    pdf = multipdf.getCurrentPdf()
    name = pdf.GetName()
    short = name.split("_")[-1]  
    short_names.append(short)


mass_points = np.arange(110, 181, 5)


for m in mass_points:

    mass.setVal(m)
    print(f"\nMass : {m:.0f} GeV")

    for i in range(n_pdfs):
        index_cat.setIndex(i)
        val = multipdf.getVal(ROOT.RooArgSet(mass))
        print(f"{short_names[i]} : {val:.6e}")

file.Close()
