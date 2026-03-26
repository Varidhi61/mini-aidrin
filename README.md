# Mini AIDRIN: AI Data Readiness Inspector

Mini AIDRIN is a lightweight framework designed to analyze the quality and readiness of datasets for AI/ML workflows. It helps identify issues like missing values, duplicates, and feature relationships through analysis and visualization.
# Overview
In Artificial Intelligence, data quality plays a crucial role in model performance. Poor-quality data leads to poor results, commonly referred to as **Garbage In, Garbage Out (GIGO)**.This project is a simplified implementation of an AI Data Readiness Inspector that evaluates datasets before they are used in machine learning pipelines. It provides insights into data quality and helps in identifying potential issues early.
# Features

- # Supports multiple file formats:
  - CSV files
  - HDF5 files

- # Modular Loader System
  - Easily extendable to support more formats

- # Data Analysis:
  - Missing values detection
  - Duplicate detection
  - Class distribution analysis

- # Visualization:
  - Class distribution graph
  - Missing values graph
  - Correlation heatmap

- # JSON Report Export
  - Saves analysis results in a structured format

- # Command Line Interface (CLI)
  - Run the tool using terminal commands
 
 #  Project Structure

mini-aidrin/
│
├── main.py              # Entry point of the program
├── analyzer.py          # Data analysis logic
├── report.py            # Visualization functions
├── create_hdf5.py       # Script to generate HDF5 test file
├── sample_data.csv      # Sample dataset
│
├── loaders/
│   ├── base_loader.py   # Base loader class
│   ├── csv_loader.py    # CSV file loader
│   ├── hdf5_loader.py   # HDF5 file loader
# Installation

Install required libraries using pip:

```bash
pip install pandas matplotlib seaborn h5py

---

# 6. Usage

```markdown
## Usage

###  Run with CSV file

```bash
python main.py sample_data.csv
# RUN with HDF5 file
python main.py test.h5

---

##  Output

```markdown
## Output

The tool provides:

- Data quality report in the terminal
- Graphical visualizations:
  - Class distribution
  - Missing values
  - Correlation heatmap
- JSON file (`report.json`) containing analysis results

#  Key Learnings

- Understanding of data quality in AI systems
- Modular software design principles
- Handling multiple data formats
- Data visualization using Python libraries
- Building CLI-based tools

# Future Improvements

- Support for additional file formats (Zarr, Parquet)
- Advanced data quality metrics (bias, fairness)
- Automated data quality scoring system
- Integration with web interfaces (Streamlit/Gradio)
