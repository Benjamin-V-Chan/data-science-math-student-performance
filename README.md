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
