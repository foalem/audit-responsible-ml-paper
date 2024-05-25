Project Name: Data Collection and Analysis for our paper Logging Requirement for Continuous Auditing of
Responsible Machine Learning-based Applications

Features
Search Repositories: Search for repositories based on specific configurations.
Save Repositories: Save the found repositories' data.
Collect Metrics: Collect various metrics like commits count, contributors count, stars, etc.
Clone Repositories: Clone repositories to a local directory.
Convert Notebooks: Convert Jupyter Notebooks to Python files recursively.
Parse Python Files: Parse Python files to extract all function calls.
Collect Issues: Collect issues from repositories and save them to a CSV file.
Installation
Clone the Repository:

sh
Copier le code
git clone https://github.com/yourusername/yourproject.git
cd yourproject
Install Dependencies:

sh
Copier le code
pip install -r requirements.txt
Set Up Configuration:
Ensure that the config/constant.py file is properly configured with the necessary paths and configurations.

Usage
The main script main.py provides several command-line arguments to perform different tasks:

sh
Copier le code
python main.py [options]
Options
-c, --collect: Search repositories with some configuration.
-s, --save: Save the found repositories.
-m, --metric: Collect repository metrics.
-cl, --clone: Clone repositories.
-conv, --convert: Convert all notebook files in a repository to .py files.
-p, --parser: Parse Python files and extract all function calls.
-i, --issue: Collect issues from repositories.
Examples
Search and Save Repositories:

sh
Copier le code
python main.py --collect --save
Collect Metrics:

sh
Copier le code
python main.py --metric
Clone Repositories:

sh
Copier le code
python main.py --clone
Convert Notebooks to Python:

sh
Copier le code
python main.py --convert
Parse Python Files:

sh
Copier le code
python main.py --parser
Collect Issues:

sh
Copier le code
python main.py --issue
Project Structure
lua
Copier le code
project_root/
│
├── config/
│   └── constant.py
│
├── data__collection/
│   ├── compute_project_size.py
│   ├── get_issue.py
│   ├── get_repo.py
│   ├── get_repo_infos.py
│   ├── get_repo_metric.py
│   └── clone_repo.py
│
├── parser/
│   ├── convert_notebooks_python.py
│   ├── convert_python_2_to_3.py
│   └── function_call.py
│
├── logging_file.log
├── requirements.txt
└── main.py
Contributing
Contributions are welcome! Please follow these steps to contribute:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit them (git commit -m 'Add some feature').
Push to the branch (git push origin feature-branch).
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgements
argparse - For parsing command-line arguments.
ast - For parsing and analyzing Python abstract syntax trees.
os.path - For common pathname manipulations.
sys - For system-specific parameters and functions.
