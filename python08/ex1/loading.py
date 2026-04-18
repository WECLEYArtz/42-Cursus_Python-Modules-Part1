from importlib import util
from importlib.metadata import version


def check_dep() -> None:
    dependencies: dict[str, str] = {
            "numpy": "Numerical computation",
            "pandas": "Data manipulation",
            "matplotlib": "Visualization ready"
            }

    print("Checking dependencies:")

    missing: list[str] = []
    for key, val in dependencies.items():
        if util.find_spec(key):
            print(f'[OK], {key}, {version(key)} - {val} ready')
        else:
            print(f'[KO], {key} - {val} missing')
            missing.append(key)

    if len(missing):
        print("\nMissing dependencie(s):", *missing, "\nUsage:")
        print("'pip install -r requirements.txt && python3 loading.py'")
        print("or")
        print("'poetry install &&  poetry run python loading.py'")
        exit(1)


def main() -> None:
    print("LOADING STATUS: Loading programs...")

    print("Analyzing Matrix data...")

    check_dep()
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    print("Processing 1000 data points...")
    data = np.random.randint(100, size=(1000))
    dataframe = pd.DataFrame(data)

    print("Generating visualization...")
    print()
    plt.plot(dataframe)
    plt.savefig('matrix_analysis.png')
    print("Results saved to: matrix_analysis.png")

    print("Analysis complete!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
