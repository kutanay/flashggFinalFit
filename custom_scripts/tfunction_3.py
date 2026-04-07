import sys
import ROOT

ROOT.gROOT.SetBatch(True)

initial_mass = int(sys.argv[1])
final_mass = int(sys.argv[2])
tag = "run3"

def draw_band(tf_central, tf_up, tf_dn, n_points=70):
    band = ROOT.TGraph(2 * n_points)
    for i in range(n_points):
        x = 110 + (180 - 110) * i / (n_points - 1)
        band.SetPoint(i, x, tf_up.Eval(x))
    for i in range(n_points):
        x = 110 + (180 - 110) * (n_points - 1 - i) / (n_points - 1)
        band.SetPoint(n_points + i, x, tf_dn.Eval(x))
    band.SetFillColor(ROOT.kBlue)
    band.SetFillStyle(3001)
    band.SetLineColor(ROOT.kBlue)
    return band

def bern1_plotter(name, p, p_err, scale, mass, data_binned, massval, tag):
    f_central = ROOT.TF1(name+"_central","[1]*(1 + (([0]*[0]-1)*((x-110)/70)))",110,180)
    f_central.SetParameter(0,p)
    f_central.SetParameter(1,scale)
    f_up = ROOT.TF1(name+"_up","[1]*(1 + (([0]*[0]-1)*((x-110)/70)))",110,180)
    f_up.SetParameter(0,p+p_err)
    f_up.SetParameter(1,scale)
    f_dn = ROOT.TF1(name+"_dn","[1]*(1 + (([0]*[0]-1)*((x-110)/70)))",110,180)
    f_dn.SetParameter(0,p-p_err)
    f_dn.SetParameter(1,scale)
    
    band = draw_band(f_central,f_up,f_dn)
    
    c = ROOT.TCanvas("c_"+name,"",800,600)
    frame = mass.frame()
    frame = mass.frame(ROOT.RooFit.Title(""))
    frame.GetXaxis().SetTitle("m_{#gamma#gamma#gamma#gamma} [GeV]") 
    data_binned.plotOn(frame, ROOT.RooFit.CutRange("left"))
    data_binned.plotOn(frame, ROOT.RooFit.CutRange("right"))
    data_binned.plotOn(frame, ROOT.RooFit.Invisible())
    frame.Draw()
    band.Draw("F SAME")
    f_central.SetLineColor(ROOT.kBlack)
    f_central.SetLineWidth(2)
    f_central.Draw("SAME")

    # Legend
    leg = ROOT.TLegend(0.15,0.65,0.48,0.88)
    leg.AddEntry(frame.getHist(), "Data (blinded)", "P")
    leg.AddEntry(f_central, f"{name} function", "L")
    leg.AddEntry(band, "1#sigma band", "F")
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.Draw()

    # TLatex
    ltx = ROOT.TLatex()
    ltx.SetNDC()
    ltx.SetTextSize(0.03)
    ltx.DrawLatex(0.15,0.92,f"Mass = {massval} GeV, {tag}")

    c.SaveAs(f"best_fit_{massval}_{tag}_{name}.png")
    c.SaveAs(f"best_fit_{massval}_{tag}_{name}.pdf")

def exp1_plotter(name, p, p_err, scale, mass, data_binned, massval, tag):
    f_central = ROOT.TF1(name+"_central","[1]*exp([0]*x)",110,180)
    f_central.SetParameter(0,p)
    f_central.SetParameter(1,scale)
    f_up = ROOT.TF1(name+"_up","[1]*exp([0]*x)",110,180)
    f_up.SetParameter(0,p+p_err)
    f_up.SetParameter(1,scale)
    f_dn = ROOT.TF1(name+"_dn","[1]*exp([0]*x)",110,180)
    f_dn.SetParameter(0,p-p_err)
    f_dn.SetParameter(1,scale)
    
    band = draw_band(f_central,f_up,f_dn)
    
    c = ROOT.TCanvas("c_"+name,"",800,600)
    frame = mass.frame()
    frame = mass.frame(ROOT.RooFit.Title(""))
    frame.GetXaxis().SetTitle("m_{#gamma#gamma#gamma#gamma} [GeV]") 
    data_binned.plotOn(frame, ROOT.RooFit.CutRange("left"))
    data_binned.plotOn(frame, ROOT.RooFit.CutRange("right"))
    data_binned.plotOn(frame, ROOT.RooFit.Invisible())
    frame.Draw()
    band.Draw("F SAME")
    f_central.SetLineColor(ROOT.kBlack)
    f_central.SetLineWidth(2)
    f_central.Draw("SAME")

    leg = ROOT.TLegend(0.15,0.65,0.48,0.88)
    leg.AddEntry(frame.getHist(), "Data (blinded)", "P")
    leg.AddEntry(f_central, f"{name} function", "L")
    leg.AddEntry(band, "1#sigma band", "F")
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.Draw()

    ltx = ROOT.TLatex()
    ltx.SetNDC()
    ltx.SetTextSize(0.03)
    ltx.DrawLatex(0.15,0.92,f"Mass = {massval} GeV, {tag}")

    c.SaveAs(f"best_fit_{massval}_{tag}_{name}.png")
    c.SaveAs(f"best_fit_{massval}_{tag}_{name}.pdf")

def pow1_plotter(name, p, p_err, scale, mass, data_binned, massval, tag):
    f_central = ROOT.TF1(name+"_central","[1]*pow(x,[0])",110,180)
    f_central.SetParameter(0,p)
    f_central.SetParameter(1,scale)
    f_up = ROOT.TF1(name+"_up","[1]*pow(x,[0])",110,180)
    f_up.SetParameter(0,p+p_err)
    f_up.SetParameter(1,scale)
    f_dn = ROOT.TF1(name+"_dn","[1]*pow(x,[0])",110,180)
    f_dn.SetParameter(0,p-p_err)
    f_dn.SetParameter(1,scale)
    
    band = draw_band(f_central,f_up,f_dn)
    
    c = ROOT.TCanvas("c_"+name,"",800,600)
    frame = mass.frame()
    frame = mass.frame(ROOT.RooFit.Title(""))
    frame.GetXaxis().SetTitle("m_{#gamma#gamma#gamma#gamma} [GeV]") 
    data_binned.plotOn(frame, ROOT.RooFit.CutRange("left"))
    data_binned.plotOn(frame, ROOT.RooFit.CutRange("right"))
    data_binned.plotOn(frame, ROOT.RooFit.Invisible())
    frame.Draw()
    band.Draw("F SAME")
    f_central.SetLineColor(ROOT.kBlack)
    f_central.SetLineWidth(2)
    f_central.Draw("SAME")

    leg = ROOT.TLegend(0.15,0.65,0.48,0.88)
    leg.AddEntry(frame.getHist(), "Data (blinded)", "P")
    leg.AddEntry(f_central, f"{name} function", "L")
    leg.AddEntry(band, "1#sigma band", "F")
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.Draw()

    ltx = ROOT.TLatex()
    ltx.SetNDC()
    ltx.SetTextSize(0.03)
    ltx.DrawLatex(0.15,0.92,f"Mass = {massval} GeV, {tag}")

    c.SaveAs(f"best_fit_{massval}_{tag}_{name}.png")
    c.SaveAs(f"best_fit_{massval}_{tag}_{name}.pdf")

def lau1_plotter(name, p, p_err, scale, mass, data_binned, massval, tag):
    f_central = ROOT.TF1(name+"_central","[1]*[0]*pow(x,-4)",110,180)
    f_central.SetParameter(0,p)
    f_central.SetParameter(1,scale)

    f_up = ROOT.TF1(name+"_up","[1]*[0]*pow(x,-4)",110,180)
    f_up.SetParameter(0,p+p_err)
    f_up.SetParameter(1,scale)

    f_dn = ROOT.TF1(name+"_dn","[1]*[0]*pow(x,-4)",110,180)
    f_dn.SetParameter(0,p-p_err)
    f_dn.SetParameter(1,scale)

    band = draw_band(f_central,f_up,f_dn)

    c = ROOT.TCanvas("c_"+name,"",800,600)
    frame = mass.frame()
    frame = mass.frame(ROOT.RooFit.Title(""))
    frame.GetXaxis().SetTitle("m_{#gamma#gamma#gamma#gamma} [GeV]") 
    data_binned.plotOn(frame, ROOT.RooFit.CutRange("left"))
    data_binned.plotOn(frame, ROOT.RooFit.CutRange("right"))
    data_binned.plotOn(frame, ROOT.RooFit.Invisible())
    frame.Draw()

    band.Draw("F SAME")

    f_central.SetLineColor(ROOT.kBlack)
    f_central.SetLineWidth(2)
    f_central.Draw("SAME")

    leg = ROOT.TLegend(0.15,0.65,0.48,0.88)
    leg.AddEntry(frame.getHist(), "Data (blinded)", "P")
    leg.AddEntry(f_central, f"{name} function", "L")
    leg.AddEntry(band, "1#sigma band", "F")
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.Draw()

    ltx = ROOT.TLatex()
    ltx.SetNDC()
    ltx.SetTextSize(0.03)
    ltx.DrawLatex(0.15,0.92,f"Mass = {massval} GeV, {tag}")

    c.SaveAs(f"best_fit_{massval}_{tag}_{name}.png")
    c.SaveAs(f"best_fit_{massval}_{tag}_{name}.pdf")

for massval in range(initial_mass, final_mass+1):
    file_path = f"/eos/home-t/takumar/gitcode/higgsdna_finalfits_tutorial_24/07_FinalFits/CMSSW_14_1_0_pre4/src/flashggFinalFit/Combine/2024/Models/background/{massval}_GeV/CMS-HGG_multipdf_CAT1.root"
    f = ROOT.TFile(file_path)
    w = f.Get("multipdf")
    mass = w.var("CMS_hgg_mass")
    norm = w.var("CMS_hgg_CAT1_2024_13TeV_bkgshape_norm")
    data = w.data("roohist_data_mass_CAT1")
    mpdf = w.pdf("CMS_hgg_CAT1_2024_13TeV_bkgshape")
    bestpdf_name = mpdf.getCurrentPdf().GetName()
    
    if "bern" in bestpdf_name:
        pdf = w.pdf("env_pdf_0_2024_13TeV_bern1")
        var = w.var("env_pdf_0_2024_13TeV_bern1_p0")
        plot_func = bern1_plotter
    elif "exp" in bestpdf_name:
        pdf = w.pdf("env_pdf_0_2024_13TeV_exp1")
        var = w.var("env_pdf_0_2024_13TeV_exp1_p1")
        plot_func = exp1_plotter
    elif "pow" in bestpdf_name:
        pdf = w.pdf("env_pdf_0_2024_13TeV_pow1")
        var = w.var("env_pdf_0_2024_13TeV_pow1_p1")
        plot_func = pow1_plotter
    elif "lau" in bestpdf_name:
        pdf = w.pdf("env_pdf_0_2024_13TeV_lau1")
        var = w.var("env_pdf_0_2024_13TeV_lau1_l1")
        plot_func = lau1_plotter

    p0_val = var.getVal()
    p0_err = var.getError()
    
    mass.setBins(70)
    data_binned = ROOT.RooDataHist("data_binned","data_binned",ROOT.RooArgSet(mass),data)
    
    mass.setRange("full",110,180)
    integral = pdf.createIntegral(ROOT.RooArgSet(mass),ROOT.RooFit.Range("full")).getVal()
    scale = norm.getVal()/integral
    
    mass.setRange("left",110,115)
    mass.setRange("right",135,180)
    
    plot_func(bestpdf_name,p0_val,p0_err,scale,mass,data_binned,massval,tag)
    
    f.Close()
