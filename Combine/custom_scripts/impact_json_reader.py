import json
import sys

def compute_impacts(json_file):

    with open(json_file) as f:
        data = json.load(f)

    # get best fit r
    r_best = data["POIs"][0]["fit"][1]

    print(f"{'Nuisance':40s} {'Impact -1σ':>15s} {'Impact +1σ':>15s}")
    print("-"*75)

    for p in data["params"]:

        name = p["name"]
        r_vals = p["r"]

        r_minus = r_vals[0]
        r_nom   = r_vals[1]
        r_plus  = r_vals[2]

        impact_minus = r_minus - r_nom
        impact_plus  = r_plus  - r_nom

        print(f"{name:40s} {impact_minus:15.6e} {impact_plus:15.6e}")


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python impacts_table.py impacts.json")
        sys.exit(1)

    compute_impacts(sys.argv[1])
