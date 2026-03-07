import json
import sys

def clean_impacts(input_file, output_file):

    with open(input_file, "r") as f:
        data = json.load(f)

    # Filter params
    filtered_params = [
        p for p in data.get("params", [])
        if not (
            p.get("name", "").startswith("shape")
            or p.get("name", "").startswith("env")
            or p.get("name", "") == "MH"
        )
    ]

    data["params"] = filtered_params

    with open(output_file, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Cleaned file written to: {output_file}")


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python3 impact_cleaner.py input.json output.json")
        sys.exit(1)

    input_json = sys.argv[1]
    output_json = sys.argv[2]

    clean_impacts(input_json, output_json)

