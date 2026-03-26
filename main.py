
from loaders.csv_loader import CSVLoader
from loaders.hdf5_loader import HDF5Loader
from analyzer import analyze_data
from report import plot_class_distribution, plot_missing, plot_correlation
import matplotlib.pyplot as plt
import json
import sys

def main():

    # CLI check
    if len(sys.argv) < 2:
        print("❌ Please provide file path")
        return

    file_path = sys.argv[1]

    # File type detection
    if file_path.endswith(".csv"):
        loader = CSVLoader()

    elif file_path.endswith(".h5") or file_path.endswith(".hdf5"):
        loader = HDF5Loader()

    else:
        print("❌ Unsupported file type")
        return

    # Load data
    df = loader.load(file_path)

    if df is not None:
        print("\n🔍 Data Preview:")
        print(df)   # ✅ debug + useful

        report = analyze_data(df)

        print("\n📊 Report:")
        for key, value in report.items():
            print(f"{key}: {value}")

        # Save JSON report
        with open("report.json", "w") as f:
            json.dump(report, f, indent=4)

        print("✅ Report saved as report.json")

        # Visualizations
        plot_class_distribution(report['class_distribution'])

        # Only plot missing if exists
        if any(v > 0 for v in report['missing_values'].values()):
            plot_missing(df)
        else:
            print("ℹ️ No missing values to plot")

        plot_correlation(df)

        plt.show()


if __name__ == "__main__":
    main()