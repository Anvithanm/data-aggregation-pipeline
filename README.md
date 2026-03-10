# Data Aggregation Pipeline

## Overview
This project demonstrates loading a dataset from Kaggle, performing basic data cleansing, computing multiple aggregate metrics, and exporting the results into output files.

The project was developed as part of an academic hands-on assignment focused on data loading, preprocessing, aggregation, and reproducible project structure.

## Objectives
- Load a dataset from Kaggle
- Perform basic data cleansing
- Compute at least five aggregate metrics
- Save aggregate outputs into files
- Organize source code under `src/`
- Add tests under `test/`
- Provide run instructions using `Make`

## Dataset
Dataset source: `https://www.kaggle.com/datasets`

Dataset used: `housing`

Reason for selection:
This dataset was selected because it aligns with my background/interests in data analysis / machine learning / business intelligence and provides meaningful fields for aggregation and cleansing.

## Project Structure
```text
.
├── README.md
├── Makefile
├── data/
├── src/
│   └── main.py
│   └── 1553768847-housing.csv
├── test/
│   └── test_main.py
└── .github/workflows/test.yml