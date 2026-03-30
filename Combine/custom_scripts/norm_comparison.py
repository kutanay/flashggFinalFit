import ROOT
import os
import sys
import array

ROOT.gROOT.SetBatch(True)

start = int(sys.argv[1])
stop  = int(sys.argv[2])

mass_points = range(start, stop + 1)

x1, y1 = [], []
x2, y2 = [], []

for m in mass_points:

    f1 = ROOT.TFile.Open(f"background/{m}_GeV/CMS-HGG_multipdf_CAT1.root")
    ws1 = f1.Get("multipdf")
    n1 = ws1.var("CMS_hgg_CAT1_2024_13TeV_bkgshape_norm")
    x1.append(float(m))
    y1.append(n1.getVal())
    f1.Close()

    f2 = ROOT.TFile.Open(f"badder_bkg/CMS-HGG_multipdf_fullrun2_M{m}.root")
    ws2 = f2.Get("multipdf")
    n2 = ws2.var("CMS_hgg_H4GTag_Cat0_13TeV_bkgshape_norm")
    x2.append(float(m))
    y2.append(n2.getVal())
    f2.Close()

c = ROOT.TCanvas()

y_all = y1 + y2

ymin = min(y_all)
ymax = max(y_all)

yrange = ymax - ymin if ymax > ymin else 1.0

ymin -= 0.1 * yrange
ymax += 0.25 * yrange

g1 = ROOT.TGraph(len(x1), array.array('d', x1), array.array('d', y1))
g1.SetMarkerStyle(20)
g1.SetMarkerColor(ROOT.kBlue)
g1.SetLineColor(ROOT.kBlue)
g1.SetTitle("Background Norm;Mass (GeV);Norm")
g1.SetMinimum(ymin)
g1.SetMaximum(ymax)
g1.Draw("ALP")

g2 = ROOT.TGraph(len(x2), array.array('d', x2), array.array('d', y2))
g2.SetMarkerStyle(21)
g2.SetMarkerColor(ROOT.kRed)
g2.SetLineColor(ROOT.kRed)
g2.Draw("LP SAME")

leg = ROOT.TLegend(0.6, 0.8, 0.88, 0.9)
leg.AddEntry(g1, "Run 3", "lp")
leg.AddEntry(g2, "Run 2", "lp")
leg.Draw()

os.makedirs("plots_compare", exist_ok=True)
c.SaveAs("plots_compare/norm_simple.png")
