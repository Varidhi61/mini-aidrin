#  Mini AIDRIN: AI Data Readiness Inspector

Mini AIDRIN is a lightweight framework designed to analyze the quality and readiness of datasets for AI/ML workflows. It helps identify issues like missing values, duplicates, and feature relationships through analysis and visualization.

---
##  Overview
In Artificial Intelligence, data quality plays a crucial role in model performance. Poor-quality data leads to poor results, commonly referred to as **Garbage In, Garbage Out (GIGO)**.
This project is a simplified implementation of an AI Data Readiness Inspector that evaluates datasets before they are used in machine learning pipelines. It provides insights into data quality and helps in identifying potential issues early.

---
##  Features

-  Supports multiple file formats:
  - CSV files
  - HDF5 files  

-  Modular Loader System  
  Easily extendable to support more formats  

-  Data Analysis:
  - Missing values detection  
  - Duplicate detection  
  - Class distribution analysis  

-  Visualization:
  - Class distribution graph  
  - Missing values graph  
  - Correlation heatmap  

-  JSON Report Export  
  Saves analysis results in a structured format  

-  Command Line Interface (CLI)  
  Run the tool using terminal commands  

---

##  Project Structure
mini-aidrin/
│
├── main.py # Entry point
├── analyzer.py # Data analysis
├── report.py # Visualization
├── create_hdf5.py # Generate HDF5 file
├── sample_data.csv
│
├── loaders/
│ ├── base_loader.py
│ ├── csv_loader.py
│ ├── hdf5_loader.py


---

##  Installation

Install required libraries:

```bash
pip install pandas matplotlib seaborn h5py

# Usage
Run with CSV file
python main.py sample_data.csv
Run with HDF5 file
python main.py test.h5

#Output

The tool provides:

Data quality report in the terminal
Graphical visualizations:
Class distribution
Missing values
Correlation heatmap
JSON file (report.json) containing results
# Key Learnings
Understanding of data quality in AI systems
Modular software design principles
Handling multiple data formats
Data visualization using Python
Building CLI-based tools
# Future Improvements
Support for additional file formats (Zarr, Parquet)
Advanced data quality metrics (bias, fairness)
Automated data scoring system
Integration with web interfaces (Streamlit/Gradio)
