import ROOT
import os
import sys
import array
from collections import defaultdict

ROOT.gROOT.SetBatch(True)

if len(sys.argv) != 3:
    print("Usage: python3 compare_bkg_params.py <start> <stop>")
    sys.exit(1)

start = int(sys.argv[1])
stop  = int(sys.argv[2])

mass_points = range(start, stop + 1)

base_dir_1 = "background"
base_dir_2 = "badder_bkg"

data_1 = defaultdict(dict)
data_2 = defaultdict(dict)

def clean_name(name):
    if "bern1" in name and "_p0" in name:
        return "bern1_p0"
    if "exp1" in name and "_p1" in name:
        return "exp1_p1"
    if "pow1" in name and "_p1" in name:
        return "pow1_p1"
    if "lau1" in name and "_l1" in name:
        return "lau1_l1"
    return None

def process(ws, mass, store):
    multipdf = ws.allPdfs().selectByName("*bkgshape*").first()
    if not multipdf:
        return

    try:
        n = multipdf.getNumPdfs()
    except:
        return

    for i in range(n):
        pdf = multipdf.getPdf(i)
        name = pdf.GetName()

        if not ("bern1" in name or "exp1" in name or "pow1" in name or "lau1" in name):
            continue

        params = pdf.getParameters(ROOT.RooArgSet(ws.var("CMS_hgg_mass")))
        it = params.createIterator()
        p = it.Next()

        while p:
            if isinstance(p, ROOT.RooRealVar):
                cname = clean_name(p.GetName())
                if cname:
                    store[cname][mass] = (p.getVal(), p.getError())
            p = it.Next()

for m in mass_points:

    f1_path = f"{base_dir_1}/{m}_GeV/CMS-HGG_multipdf_CAT1.root"
    if os.path.exists(f1_path):
        f1 = ROOT.TFile.Open(f1_path)
        ws1 = f1.Get("multipdf")
        if ws1:
            process(ws1, m, data_1)
        f1.Close()

    f2_path = f"{base_dir_2}/CMS-HGG_multipdf_fullrun2_M{m}.root"
    if os.path.exists(f2_path):
        f2 = ROOT.TFile.Open(f2_path)
        ws2 = f2.Get("multipdf")
        if ws2:
            process(ws2, m, data_2)
        f2.Close()

os.makedirs("plots_compare", exist_ok=True)

all_params = set(list(data_1.keys()) + list(data_2.keys()))

for pname in all_params:

    masses = sorted(set(list(data_1[pname].keys()) + list(data_2[pname].keys())))

    x1, y1, ex1, ey1 = [], [], [], []
    x2, y2, ex2, ey2 = [], [], [], []

    for m in masses:
        if m in data_1[pname]:
            v, e = data_1[pname][m]
            x1.append(float(m)); y1.append(v); ex1.append(0.0); ey1.append(e)
        if m in data_2[pname]:
            v, e = data_2[pname][m]
            x2.append(float(m)); y2.append(v); ex2.append(0.0); ey2.append(e)

    c = ROOT.TCanvas()
    leg = ROOT.TLegend(0.6, 0.8, 0.88, 0.9)

    g1, g2 = None, None

    if len(x1) > 0:
        g1 = ROOT.TGraphErrors(len(x1),
                               array.array('d', x1),
                               array.array('d', y1),
                               array.array('d', ex1),
                               array.array('d', ey1))
        g1.SetMarkerStyle(20)
        g1.SetMarkerColor(ROOT.kBlue)
        g1.SetLineColor(ROOT.kBlue)

    if len(x2) > 0:
        g2 = ROOT.TGraphErrors(len(x2),
                               array.array('d', x2),
                               array.array('d', y2),
                               array.array('d', ex2),
                               array.array('d', ey2))
        g2.SetMarkerStyle(21)
        g2.SetMarkerColor(ROOT.kRed)
        g2.SetLineColor(ROOT.kRed)

    ymin, ymax = None, None

    def update_range(yvals, evals):
        global ymin, ymax
        for v, e in zip(yvals, evals):
            low  = v - e
            high = v + e
            if ymin is None or low < ymin:
                ymin = low
            if ymax is None or high > ymax:
                ymax = high

    if g1:
        update_range(y1, ey1)
    if g2:
        update_range(y2, ey2)

    if ymin is None or ymax is None:
        ymin, ymax = 0.0, 1.0

    yrange = ymax - ymin if ymax > ymin else 1.0
    ymin -= 0.1 * yrange
    ymax += 0.35 * yrange

    if g1:
        g1.SetTitle(f"{pname};Mass (GeV);Value")
        g1.SetMinimum(ymin)
        g1.SetMaximum(ymax)
        g1.Draw("ALP")
        leg.AddEntry(g1, "Run 3", "lep")

    if g2:
        draw_opt = "LP SAME" if g1 else "ALP"
        if not g1:
            g2.SetTitle(f"{pname};Mass (GeV);Value")
            g2.SetMinimum(ymin)
            g2.SetMaximum(ymax)
        g2.Draw(draw_opt)
        leg.AddEntry(g2, "Run 2", "lep")

    leg.Draw()
    c.SaveAs(f"plots_compare/{pname}.png")

print("Saved plots in plots_compare/")