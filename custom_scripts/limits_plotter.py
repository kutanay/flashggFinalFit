import ROOT
import array

ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch(True)

mass = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60]


exp_025 = [1.1159, 0.9241, 0.9883, 0.9398, 1.0657, 1.0667, 0.9912, 0.8150, 0.7102, 0.6544]
exp_160 = [1.3467, 1.1396, 1.2000, 1.1552, 1.2888, 1.2881, 1.1893, 0.9837, 0.8522, 0.7874]
exp_500 = [1.6953, 1.4648, 1.5195, 1.4805, 1.6484, 1.6016, 1.4883, 1.2383, 1.0664, 0.9883]
exp_840 = [2.1751, 1.9144, 1.9496, 1.9231, 2.1018, 2.0421, 1.8857, 1.5789, 1.3597, 1.2522]
exp_975 = [2.7222, 2.4403, 2.4608, 2.4570, 2.6362, 2.5392, 2.3498, 1.9632, 1.7054, 1.5604]

exp = exp_500
err1_up = [hi - mid for hi, mid in zip(exp_840, exp_500)]
err1_down = [mid - lo for lo, mid in zip(exp_160, exp_500)]
err2_up = [hi - mid for hi, mid in zip(exp_975, exp_500)]
err2_down = [mid - lo for lo, mid in zip(exp_025, exp_500)]

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
frame = ROOT.TH1F(
    "frame",
    ";m_{a} [GeV];#sigma(pp #rightarrow H) #times BR(H #rightarrow aa #rightarrow #gamma#gamma#gamma#gamma) (fb)",
    1, 13, 62
)

#frame.SetMinimum(0.01)
frame.SetMaximum(6)
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

latex.SetTextFont(52)
latex.SetTextSize(0.04)
latex.DrawLatexNDC(0.18, 0.91, "#bf{CMS} Preliminary")
latex.SetTextFont(40)
#latex.DrawLatexNDC(0.62, 0.93, "34.70 fb^{-1} (13.6 TeV)")
lumi = 34.70
latex.DrawLatex(0.62,0.92,"13.6 TeV , %.2f fb^{-1}"%lumi)
c.Update()

# Legend
leg = ROOT.TLegend(0.6, 0.7, 0.88, 0.88)
leg.SetFillStyle(0)
leg.SetBorderSize(0)
leg.SetTextFont(42)
leg.AddEntry(g_exp, "Median expected", "l")
leg.AddEntry(band1, "68% CL expected", "f")
leg.AddEntry(band2, "95% CL expected", "f")
leg.Draw()

# Save
#c.SaveAs("limits-full-corrections-pre.png")
c.SaveAs("limits.png")
c.SaveAs("limits.pdf")