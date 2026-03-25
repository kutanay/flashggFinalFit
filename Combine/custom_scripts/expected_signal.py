import os
import subprocess
import ROOT

ROOT.gROOT.SetBatch(True)

mass_points = range(15, 63)

datacard_base = (
    "/eos/home-t/takumar/gitcode/higgsdna_finalfits_tutorial_24/"
    "07_FinalFits/CMSSW_14_1_0_pre4/src/flashggFinalFit/"
    "Combine/2024/datacards/Datacard_bdt_{}_2024.txt"
)

output_txt = "signal_yields_prefit_2024.txt"

def run_fitdiagnostics(datacard_path, mass):
    tag = f"{mass}_2024"
    cmd = [
        "combine",
        "-M", "FitDiagnostics",
        datacard_path,
        "-n", f"_{tag}",
        "-t", "-1",
        "--expectSignal=1",
        "--saveNormalizations"
    ]
    subprocess.run(cmd, check=True)
    return f"fitDiagnostics_{tag}.root"

def extract_signal_yield(root_file):
    f = ROOT.TFile.Open(root_file)
    norm_prefit = f.Get("norm_prefit")
    sig = norm_prefit.find("CAT1/total_signal")
    value = sig.getVal()
    f.Close()
    return value

results = []

for m in mass_points:
    datacard = datacard_base.format(m)
    root_output = run_fitdiagnostics(datacard, m)
    y = extract_signal_yield(root_output)
    results.append(y)
    print(f"MA{m} : {y}")

with open(output_txt, "w") as f:
    f.write("Prefit signal yields (Asimov mu=1)\n\n")
    for i, m in enumerate(mass_points):
        f.write(f"MA{m} : {results[i]}\n")
    f.write("\n\n# Python array (copy-paste ready)\n")
    f.write("signal_yields = [\n")
    for y in results:
        f.write(f"    {y},\n")
    f.write("]\n")

print(f"\nSaved results to {output_txt}")