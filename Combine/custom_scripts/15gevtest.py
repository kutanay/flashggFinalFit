import ROOT
import array

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)

# --- X values ---
x = [0, 1, 2, 3]
x_arr = array.array('d', x)

# --- Quantiles ---
y_2p5  = [1.01901, 0.966379, 0.977906, 0.89342]
y_16   = [1.08509, 1.06931, 1.0287,   1.08424]
y_50   = [1.37178, 1.34188, 1.32804,  1.4111]
y_84   = [1.8863,  2.07697, 1.87698,  1.98686]
y_97p5 = [2.82284, 2.60829, 2.70761,  2.72798]

# --- Reference ---
ref_2p5  = [0.990642]*4
ref_16   = [1.04971]*4
ref_50   = [1.3451]*4
ref_84   = [1.88341]*4
ref_97p5 = [2.76158]*4

def make_graph(y):
    return ROOT.TGraph(len(x), x_arr, array.array('d', y))

g2p5  = make_graph(y_2p5)
g16   = make_graph(y_16)
g50   = make_graph(y_50)
g84   = make_graph(y_84)
g97p5 = make_graph(y_97p5)

r2p5  = make_graph(ref_2p5)
r16   = make_graph(ref_16)
r50   = make_graph(ref_50)
r84   = make_graph(ref_84)
r97p5 = make_graph(ref_97p5)

# --- Styling ---
colors = [ROOT.kBlue, ROOT.kGreen+2, ROOT.kBlack, ROOT.kOrange+1, ROOT.kRed]
graphs = [g2p5, g16, g50, g84, g97p5]
refs   = [r2p5, r16, r50, r84, r97p5]

for i in range(5):
    graphs[i].SetLineColor(colors[i])
    graphs[i].SetMarkerColor(colors[i])
    graphs[i].SetMarkerStyle(20)
    graphs[i].SetLineWidth(2)

    refs[i].SetLineColor(colors[i])
    refs[i].SetLineStyle(2)
    refs[i].SetLineWidth(2)

# --- Canvas ---
c = ROOT.TCanvas("c", "", 1200, 800)

# --- Pads ---
pad_plot = ROOT.TPad("pad_plot", "", 0.0, 0.0, 0.75, 1.0)
pad_leg  = ROOT.TPad("pad_leg",  "", 0.75, 0.0, 1.0, 1.0)

pad_plot.SetLeftMargin(0.12)
pad_plot.SetBottomMargin(0.12)
pad_plot.SetRightMargin(0.02)

pad_leg.SetLeftMargin(0.0)
pad_leg.SetRightMargin(0.0)
pad_leg.SetFillStyle(0)

pad_plot.Draw()
pad_leg.Draw()

# --- Plot pad ---
pad_plot.cd()

frame = ROOT.TH1F("frame", ";Model;Expected r", 4, -0.5, 3.5)

frame.GetXaxis().SetBinLabel(1, "bern1")
frame.GetXaxis().SetBinLabel(2, "exp1")
frame.GetXaxis().SetBinLabel(3, "pow1")
frame.GetXaxis().SetBinLabel(4, "lau1")

frame.GetXaxis().SetLabelSize(0.045)
frame.GetYaxis().SetTitleOffset(1.2)

frame.SetMinimum(0.8)
frame.SetMaximum(3.0)

frame.Draw()

for g in graphs:
    g.Draw("LP SAME")

for r in refs:
    r.Draw("L SAME")

# --- Legend pad ---
pad_leg.cd()

leg = ROOT.TLegend(0.05, 0.5, 0.99, 0.8)
leg.SetBorderSize(0)
leg.SetFillStyle(0)
leg.SetTextSize(0.07)

leg.AddEntry(g2p5,  "2.5%",  "lp")
leg.AddEntry(g16,   "16%",   "lp")
leg.AddEntry(g50,   "50%",   "lp")
leg.AddEntry(g84,   "84%",   "lp")
leg.AddEntry(g97p5, "97.5%", "lp")
leg.AddEntry(r50, "Refernce", "l")

leg.Draw()

# --- Save ---
c.SaveAs("quantiles_overlay.png")