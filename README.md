# Student Performance Data: Scripts and Datasets

This repository serves as a collection of scripts and datasets that were generated as part of a DataFestAfrica 24 Datathon. The purpose of this repository is to provide easy access to the scripts and datasets used in the analysis and prediction of student performance based on various metrics.

## Contents

- **Scripts**: Python scripts used to generate different datasets.
- **Datasets**: CSV files of the generated data.

## Structure

```plaintext
📦 student-performance-dataset-repo
 ┣ 📂 datasets                  # Contains generated datasets
 ┣ 📂 scripts                   # Contains Python scripts for data generation
 ┗ 📜 README.md                 # Overview of the repository
```

### `datasets/`
This folder contains the generated datasets in CSV format:
- **academic_performance.csv**: Performance data for students.
- **learning_behavior.csv**: Data on learning behaviors such as platform usage and homework completion.
- **attendance_participation.csv**: Attendance and participation metrics.
- **parental_involvement.csv**: Information about parental involvement in student education.
- **socio_emotional.csv**: Socio-emotional well-being and peer relationships.
- **study_habits.csv**: Data on study habits and exam preparation confidence.
- **resource_utilization.csv**: Information about tutoring sessions and study group participation.
- **teacher_table.csv**: Teacher information such as subjects taught and contact details.
- **activity_table.csv**: Extracurricular activities and assigned teachers.

### `scripts/`
This folder contains Python scripts used to generate each dataset:
- **generate_academic_performance.py**: Generates the academic performance dataset.
- **generate_learning_behavior.py**: Generates the learning behavior dataset.
- **generate_attendance_data.py**: Generates the attendance and participation dataset.
- **generate_parental_involvement.py**: Generates the parental involvement dataset.
- **generate_socio_emotional.py**: Generates the socio-emotional data.
- **generate_study_habits.py**: Generates data related to study habits.
- **generate_resource_utilization.py**: Generates data on tutoring and study material usage.
- **generate_teacher_table.py**: Generates teacher data.
- **generate_activity_table.py**: Generates extracurricular activity data.

## Usage

### Running the Scripts

Each script is self-contained and can be run independently to generate the corresponding dataset. To generate a dataset, run the respective Python script, for example:

```bash
python scripts/generate_academic_performance.py
```

The output will be saved as a CSV file in the `datasets/` folder.

### Dependencies

To run the scripts, you need Python 3.x and the following packages:
- **pandas**
- **numPy**
- **random**
- **datetime**
- **seaborn**
- **matplotlib**
- **scikit-learn**

You can install the dependencies using `pip`:

```bash
pip install pandas numpy
```

## Purpose

The primary goal of this repository is to make the generated datasets and scripts easily accessible for further analysis or reference. 
