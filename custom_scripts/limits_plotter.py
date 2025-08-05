#limit potting script

import ROOT
import array


ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch(True)

mass = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60]


#limits for sigstr

exp_025 = [0.0252, 0.0238, 0.0238, 0.0238, 0.0238, 0.0233, 0.0219, 0.0197, 0.0169, 0.0147]
exp_160 = [0.0290, 0.0280, 0.0280, 0.0274, 0.0280, 0.0267, 0.0253, 0.0228, 0.0195, 0.0170]
exp_500 = [0.0347, 0.0327, 0.0327, 0.0327, 0.0327, 0.0317, 0.0298, 0.0269, 0.0229, 0.0200]
exp_840 = [0.0410, 0.0398, 0.0398, 0.0398, 0.0398, 0.0386, 0.0360, 0.0324, 0.0277, 0.0248]
exp_975 = [0.0488, 0.0468, 0.0468, 0.0468, 0.0468, 0.0454, 0.0424, 0.0382, 0.0326, 0.0290]


exp = exp_500
err1_up = [hi - mid for hi, mid in zip(exp_840, exp_500)]
err1_down = [mid - lo for lo, mid in zip(exp_160, exp_500)]
err2_up = [hi - mid for hi, mid in zip(exp_975, exp_500)]
err2_down = [mid - lo for lo, mid in zip(exp_025, exp_500)]

#err1_up = []
#err1_down = []
#err2_up = []
#err2_down = []
#for i in range(len(exp_500)):
#    err1_up.append()
print(err1_up)

# Convert to ROOT arrays
x = array.array('d', mass)
y_exp = array.array('d', exp)
zeros = array.array('d', [0.0]*len(mass))
ey1_up = array.array('d', err1_up)
ey1_down = array.array('d', err1_down)
ey2_up = array.array('d', err2_up)
ey2_down = array.array('d', err2_down)

# Create canvas
c = ROOT.TCanvas("c", "", 800, 800)
c.SetLogy(0)
c.SetLeftMargin(0.15)
c.SetBottomMargin(0.15)

# Frame
frame = ROOT.TH1F("frame", " ;m_{a} [GeV];r", 1, 13, 62)
#frame.SetMinimum(0.01)
frame.SetMaximum(0.1)
frame.Draw()

# ±2σ band
band2 = ROOT.TGraphAsymmErrors(len(mass), x, y_exp, zeros, zeros, ey2_down, ey2_up)
band2.SetFillColor(ROOT.kYellow)
band2.SetLineColor(0)
band2.Draw("3")

# ±1σ band
band1 = ROOT.TGraphAsymmErrors(len(mass), x, y_exp, zeros, zeros, ey1_down, ey1_up)
band1.SetFillColor(ROOT.kGreen + 1)
band1.SetLineColor(0)
band1.Draw("3")

# Expected central
g_exp = ROOT.TGraph(len(mass), x, y_exp)
g_exp.SetLineColor(ROOT.kRed)
g_exp.SetLineStyle(2)
g_exp.SetLineWidth(2)
g_exp.SetMarkerStyle(20)
g_exp.Draw("LP SAME")

# CMS Label
latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextFont(62)
latex.SetTextSize(0.045)
#latex.DrawLatex(0.18, 0.84, "CMS")
latex.SetTextFont(52)
latex.SetTextSize(0.04)
#latex.DrawLatex(0.18, 0.78, "Preliminary")
latex.SetTextFont(42)
#latex.DrawLatex(0.62, 0.84, "#sqrt{s} = 13 TeV, L = 138 fb^{-1}")

# Legend
leg = ROOT.TLegend(0.7, 0.7, 0.88, 0.88)
leg.SetFillStyle(0)
leg.SetBorderSize(0)
leg.SetTextFont(42)
leg.AddEntry(g_exp, "Expected", "l")
leg.AddEntry(band1, "#pm1#sigma", "f")
leg.AddEntry(band2, "#pm2#sigma", "f")
leg.Draw()

# Save
#c.SaveAs("limits-full-corrections-pre.png")
c.SaveAs("limits-full-corrections-sig-str-pre.png")
c.SaveAs("limits-full-corrections-sig-str-pre.pdf")