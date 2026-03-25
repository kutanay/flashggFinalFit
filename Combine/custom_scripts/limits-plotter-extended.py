import ROOT
import array
import re
import sys
import math

ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch(True)

mass = list(range(15, 63))

filename = sys.argv[1]

signal_list = [3.6757205620467404,3.6997119901552193,3.7236997425431366,3.7476899807821673,3.7716824175437953,3.7956710586343645,3.778537399475689,3.7614075359880723,3.7442731723943523,3.727140357562027,3.710007542729701,3.693242018644105,3.676472784550967,3.6597063455746555,3.6429389285057714,3.6261715114368878,3.670704523768844,3.7152375361008003,3.759768521061075,3.8043033838787363,3.8488343978619994,3.8856023128647745,3.9223663790331527,3.959135223275479,3.995901047138397,4.032666871001316,4.162143706228557,4.291620541455795,4.421100182392348,4.550573825060717,4.680052147781232,4.965118804154734,5.250185460528238,5.535250863695599,5.820317339407321,6.105383815119045,6.57435055672597,7.043323403716707,7.512288172631275,7.981259031035388,8.450229889439502,8.938264466474193,9.426299043508878,9.914333071246022,10.402375799067277,10.890407636480894,10.890407636480894,10.890407636480894]

background_list = [4.5569149593396245,4.044698294005587,4.500674570708388,3.756568413182378,4.374377070163297,4.65621856802666,5.164061553355582,4.907579072523346,6.464510615992025,6.9288011844368596,7.116698693451578,7.823528835783097,6.804067181710529,4.3191311217455635,4.94623066313801,6.03193162964266,6.423273842998449,5.523915963281617,9.190090132863395,7.52218890924576,10.461274940512077,11.631973193401809,13.49824595646949,7.780246493928095,6.929035391300952,5.211610353754436,6.338076427157779,7.198291028774055,9.012302557387493,10.77551020408163,10.775510204081634,11.40897885097743,  11.223675464929533,12.103270985807837,11.027070202207861,9.033418097576224,10.942608540400768,13.685540636460349,12.914118076751633,14.784215522142402,16.550234388341135,16.237970311833184,15.961131456411842,14.06761227310095,11.926426318814055,13.258831095422204,13.436468936008794,9.93677279140072,]

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