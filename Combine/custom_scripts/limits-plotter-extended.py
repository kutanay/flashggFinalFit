import ROOT
import array
import re
import sys
import math

ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch(True)

mass = list(range(15, 63))

filename = sys.argv[1]

signal_list = [2.9862, 3.0057, 3.0252, 3.2015, 3.2219, 3.2424, 3.2278, 3.2132, 3.1477, 3.1333, 3.1189, 3.1048, 3.0907, 3.0876, 3.0734, 3.0593, 3.0768, 3.0942, 3.2385, 3.2567, 3.2749, 3.3281, 3.3813, 3.2651, 3.3157, 3.3662, 3.4743, 3.5824, 3.8633, 3.9765, 4.0896, 4.3387, 4.5878, 4.7969, 5.044, 5.291, 5.6974, 6.1038, 6.6472, 7.0621, 7.4771, 7.9089, 8.3407, 8.6789, 9.1061, 9.5333, 9.5333, 9.5333]
background_list = [2.2679, 2.0147, 2.2353, 1.8558, 2.1663, 2.3006, 2.5538, 2.4253, 3.1732, 3.3929, 3.5107, 3.8552, 3.343, 2.0928, 2.3957, 2.9218, 3.1152, 2.6742, 4.5055, 3.6873, 5.1229, 5.6977, 6.6041, 3.7721, 3.4007, 2.5688, 3.1296, 3.5438, 4.4547, 5.3542, 5.3542, 5.6527, 5.562, 5.9838, 5.476, 2.964, 5.4215, 6.7728, 6.3873, 7.3091, 8.216, 8.0577, 7.9173, 7.0987, 5.9884, 6.6687, 6.7608, 4.9937]

def computeAMS(s, b):
    if b <= 0 or s <= 0:
        return 0.0
    return math.sqrt(2.0 * ((s + b) * math.log(1.0 + s/b) - s))

ams_values = [computeAMS(s, b) for s, b in zip(signal_list, background_list)]

exp_025 = []
exp_160 = []
exp_500 = []
exp_840 = []
exp_975 = []

pattern_025 = re.compile(r"Expected\s+2\.5%:\s+r\s+<\s+([0-9.]+)")
pattern_160 = re.compile(r"Expected\s+16\.0%:\s+r\s+<\s+([0-9.]+)")
pattern_500 = re.compile(r"Expected\s+50\.0%:\s+r\s+<\s+([0-9.]+)")
pattern_840 = re.compile(r"Expected\s+84\.0%:\s+r\s+<\s+([0-9.]+)")
pattern_975 = re.compile(r"Expected\s+97\.5%:\s+r\s+<\s+([0-9.]+)")

with open(filename, "r") as f:
    for line in f:
        if pattern_025.search(line):
            exp_025.append(float(pattern_025.search(line).group(1)))
        elif pattern_160.search(line):
            exp_160.append(float(pattern_160.search(line).group(1)))
        elif pattern_500.search(line):
            exp_500.append(float(pattern_500.search(line).group(1)))
        elif pattern_840.search(line):
            exp_840.append(float(pattern_840.search(line).group(1)))
        elif pattern_975.search(line):
            exp_975.append(float(pattern_975.search(line).group(1)))

exp = exp_500

err1_up = [hi - mid for hi, mid in zip(exp_840, exp_500)]
err1_down = [mid - lo for lo, mid in zip(exp_160, exp_500)]
err2_up = [hi - mid for hi, mid in zip(exp_975, exp_500)]
err2_down = [mid - lo for lo, mid in zip(exp_025, exp_500)]

x = array.array('d', mass)
y_exp = array.array('d', exp)
zeros = array.array('d', [0.0]*len(mass))
ey1_up = array.array('d', err1_up)
ey1_down = array.array('d', err1_down)
ey2_up = array.array('d', err2_up)
ey2_down = array.array('d', err2_down)

x_ams = array.array('d', mass)
y_ams = array.array('d', ams_values)

c = ROOT.TCanvas("c", "", 1000, 1000)

pad1 = ROOT.TPad("pad1", "pad1", 0, 0.34, 1, 1)
pad2 = ROOT.TPad("pad2", "pad2", 0, 0, 1, 0.30)

pad1.SetTickx(1)
pad1.SetTicky(1)

pad2.SetTickx(1)
pad2.SetTicky(1)

pad1.SetBottomMargin(0.04)
pad2.SetTopMargin(0.04)
pad2.SetBottomMargin(0.35)

pad1.Draw()
pad2.Draw()

pad1.cd()

gold_color = ROOT.TColor.GetColor("#ffcc00") 

frame = ROOT.TH1F(
    "frame",
    ";m_{a} [GeV];#sigma(pp #rightarrow H) #times BR(H #rightarrow aa #rightarrow #gamma#gamma#gamma#gamma) (fb)",
    1, 15, 62
)

frame.SetMaximum(5)
#frame.GetXaxis().SetLabelSize(0)
#frame.GetXaxis().SetTitleSize(0)
frame.Draw()

band2 = ROOT.TGraphAsymmErrors(len(mass), x, y_exp, zeros, zeros, ey2_down, ey2_up)
band2.SetFillColor(gold_color)
band2.SetLineColor(0)
band2.Draw("3")

band1 = ROOT.TGraphAsymmErrors(len(mass), x, y_exp, zeros, zeros, ey1_down, ey1_up)
band1.SetFillColor(ROOT.kGreen + 1)
band1.SetLineColor(0)
band1.Draw("3")

g_exp = ROOT.TGraph(len(mass), x, y_exp)
g_exp.SetLineColor(ROOT.kRed)
g_exp.SetLineStyle(2)
g_exp.SetLineWidth(2)
g_exp.SetMarkerStyle(20)
g_exp.SetMarkerColor(ROOT.kBlack)
g_exp.Draw("LP SAME")

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextFont(62)
latex.SetTextSize(0.045)
latex.DrawLatex(0.18, 0.91, "#bf{CMS} Preliminary")

latex.SetTextFont(52)
latex.SetTextSize(0.04)
lumi = 109
latex.DrawLatex(0.61,0.91,"13.6 TeV , %.2f fb^{-1}"%lumi)

leg = ROOT.TLegend(0.6, 0.7, 0.88, 0.88)
leg.SetFillStyle(0)
leg.SetBorderSize(0)
leg.AddEntry(g_exp, "Median expected", "lp")
leg.AddEntry(band1, "68% CL expected", "f")
leg.AddEntry(band2, "95% CL expected", "f")
leg.Draw()

pad1.RedrawAxis()

pad2.cd()

frame2 = ROOT.TH1F(
    "frame2",
    ";m_{a} [GeV];AMS",
    1, 15, 62
)

frame2.SetMinimum(0)
frame2.SetMaximum(max(ams_values)*1.4 if max(ams_values)>0 else 1)

frame2.GetYaxis().SetTitleSize(0.07)
frame2.GetYaxis().SetLabelSize(0.07)
frame2.GetYaxis().SetTitleOffset(0.45)

frame2.GetXaxis().SetTitleSize(0.07)
frame2.GetXaxis().SetLabelSize(0.07)

frame2.Draw()

g_ams = ROOT.TGraph(len(mass), x_ams, y_ams)
g_ams.SetLineColor(ROOT.kBlack)
g_ams.SetLineWidth(2)
g_ams.SetMarkerStyle(20)
g_ams.Draw("LP SAME")
pad2.RedrawAxis()


c.SaveAs("limits_with_AMS.png")
c.SaveAs("limits_with_AMS.pdf")