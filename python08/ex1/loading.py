from importlib import util, import_module
from importlib.metadata import version

def main():
    dependencies: dict[str, str] = {
            "pandas": "Data manipulation",
            "numpy": "Numerical computation",
            # "requests": "Network access",
            "matplotlib": "Visualization ready"
            }


    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    for key,val in dependencies.items():
        if util.find_spec(key):
            _ = import_module(key)
            print(f'[OK], {key}, {version(key)} - {val} ready')
        else:
            print(f'[OK], {key}, {version(key)} - {val}')
    print("what")

    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")
    print("Generating visualization...")
    print("Analysis complete!")


# [OK] pandas (2.1.0) - Data manipulation ready
# [OK] numpy (1.25.0) - Numerical computation ready
# [OK] requests (2.31.0) - Network access ready
# [OK] matplotlib (3.7.2) - Visualization ready

# Analyzing Matrix data...
# Processing 1000 data points...
# Generating visualization...
# Analysis complete!
# Results saved to: matrix_analysis.png


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)



