# data-science-math-student-performance

## Project Overview

This project performs an end-to-end analysis and modeling pipeline on the "Math-Students Performance Data" dataset. The goal is to explore the relationships between socio-demographic, academic, and lifestyle factors and their impact on final math grades. The pipeline includes:

- Data loading and preprocessing
- Exploratory data analysis and visualization
- Feature engineering
- Model training using Random Forest
- Model evaluation and interpretation

The final target variable is `G3`, the final math grade. Insights gained can support interventions in education policy and student support programs.

---

## Folder Structure

```
project-root/
├── data/
│   └── Math-Students.csv
├── scripts/
│   ├── 01_data_preprocessing.py
│   ├── 02_exploratory_data_analysis.py
│   ├── 03_feature_engineering.py
│   ├── 04_model_building.py
│   └── 05_model_evaluation.py
├── outputs/
│   ├── cleaned_data.csv
│   ├── descriptive_stats.csv
│   ├── correlation.csv
│   ├── eda_plots/
│   │   ├── hist_*.png
│   │   └── correlation_heatmap.png
│   ├── model_data.csv
│   ├── model.pkl
│   ├── evaluation.txt
│   └── actual_vs_predicted.png
├── requirements.txt
└── README.md
```

---

## Usage

### 1. Setup the Project:

Clone the repository.  
Ensure you have Python installed.  
Install required dependencies using the requirements.txt file:

```bash
pip install -r requirements.txt
```

### 2. Run Preprocessing Script
```bash
python scripts/01_data_preprocessing.py
```

### 3. Run Exploratory Data Analysis
```bash
python scripts/02_exploratory_data_analysis.py
```

### 4. Run Feature Engineering
```bash
python scripts/03_feature_engineering.py
```

### 5. Train the Model
```bash
python scripts/04_model_building.py
```

### 6. Evaluate the Model
```bash
python scripts/05_model_evaluation.py
```

---

## Requirements

The project requires the following Python packages:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- joblib

Install them using:
```bash
pip install -r requirements.txt
```

---

## Acknowledgments

dataset name: Math-Students Performance Data  
dataset author:  
Adil Shamim  
dataset source: https://www.kaggle.com/datasets/adilshamim8/math-students
