# Student Data Processing Pipeline

A Python-based data processing project that loads, cleans, and transforms student data from a CSV file using Pandas. The project also includes automated unit testing with Pytest.

## Project Overview

This project demonstrates a simple data processing pipeline consisting of three main stages:

### 1. Load Data
- Reads student records from `students_messy.csv`.
- Loads CSV data into a Pandas DataFrame.

### 2. Clean Data
- Standardizes column names.
- Removes unnecessary whitespace.
- Handles empty values.
- Removes duplicate records.
- Resets DataFrame indexes.

### 3. Add Features
Creates additional columns to improve the dataset:
- `full_name` – Combines first and last names.
- `age_group` – Categorizes students as Adult or Minor.
- `email_domain` – Extracts the domain from email addresses.
- `has_missing_values` – Identifies records containing missing values.

## Technologies Used

- Python
- Pandas
- Pytest
- CSV

## Project Structure

```text
student-data-processing-pipeline/
│
├── pipeline.py
├── test_pipeline.py
├── students_messy.csv
├── students_clean.csv
├── README.md
└── .gitignore
```

## Installation

Install the required dependencies:

```bash
py -m pip install pandas pytest
```

## How to Run

### Step 1: Run the Data Processing Pipeline

```bash
py pipeline.py
```

The processed dataset will be saved as:

`students_clean.csv`

### Step 2: Run Automated Tests

```bash
py -m pytest -v
```

Expected test result:

```text
test_pipeline.py::test_clean PASSED

1 passed
```

## Testing

The project contains one Pytest test function for the `clean()` function.

It verifies:
- Column name standardization.
- Removal of extra whitespace.
- Removal of duplicate records.

## Output

The final processed dataset is generated as `students_clean.csv`.

## Author

**Humna Malik**

Software Engineering | Python | Data Processing | Software Testing

---

Created as part of a practical Python Data Processing assignment.