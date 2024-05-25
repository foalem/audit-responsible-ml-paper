# Project Name: Data Collection and Analysis for our paper Logging Requirement for Continuous Auditing of Responsible Machine Learning-based Applications

This repository contains a Python script for conducting a replication study of the paper titled "Logging Requirement for Continuous Auditing of Responsible Machine Learning-based Applications." The script enables you to collect data from GitHub repositories, perform various analyses, and save the results. This README provides an overview of the project and instructions for using the script.

## Prerequisites

Before using this script, make sure you have the following prerequisites:

- Python 3.x installed.
- Required Python packages installed. You can install them using `pip install -r requirements.txt`, where `requirements.txt` contains the necessary packages.

## Usage

To run the script, use the following command:

```
python main.py [options]
```
## Options
```

-c, --collect: Search repositories with some configuration.
-s, --save: Save the found repositories.
-m, --metric: Collect repository metrics.
-cl, --clone: Clone repositories.
-conv, --convert: Convert all notebook files in a repository to .py files.
-p, --parser: Parse Python files and extract all function calls.
-i, --issue: Collect issues from repositories.
```
## Examples
Search and Save Repositories:
```
python main.py --collect --save
```
Collect Metrics:
```
python main.py --metric
```

Clone Repositories:
```
python main.py --clone
```

Convert Notebooks to Python:
```
python main.py --convert
```

Parse Python Files:
```
python main.py --parser
```

Collect Issues:
```
python main.py --issue
```
