# OptiSyn: TCMSP Data Preprocessing Module

This branch provides a preprocessing workflow for traditional Chinese medicine (TCM) data based on the **Traditional Chinese Medicine Systems Pharmacology Database and Analysis Platform (TCMSP)**. It includes scripts for:

1. **Automatically retrieving herb-related compound and target data from TCMSP**
2. **Filtering active compounds based on ADME-related criteria**
3. **Generating compound–target association results for downstream analysis**

This module can be used as a data preparation step for network pharmacology, herb-target analysis, and graph-based herbal synergy modeling.

---

## Repository Contents

```text
.
├── Automated Data Retrieval from the TCMSP Database.py
├── Separation of Downloaded TCMSP Data.py
├── herb_name.xlsx
├── herbs_data.xlsx
├── Uniprot database raw data.xlsx
├── Results.zip
└── README.md
File Description
Automated Data Retrieval from the TCMSP Database.py
Automatically retrieves compound and target information for herbs from the TCMSP website using Selenium.
Separation of Downloaded TCMSP Data.py
Filters downloaded TCMSP compound data using predefined criteria and matches compounds with their targets.
herb_name.xlsx
Input file containing herb names to be queried from TCMSP.
herbs_data.xlsx
Supplementary herb-related data for subsequent analysis.
Uniprot database raw data.xlsx
Raw UniProt-related data, potentially for target normalization or annotation.
Results.zip
Compressed output results generated during preprocessing.
Workflow Overview
Step 1: Automatic Retrieval of TCMSP Data
The script Automated Data Retrieval from the TCMSP Database.py performs the following tasks:

Reads herb names from herb_name.xlsx
Opens the TCMSP search page
Obtains the search token required by the website
Searches each herb automatically
Enters the herb detail page
Extracts:
Ingredient information
Target information
Saves the data as Excel files
Each herb generates two files:

{herb_name}ingredients.xlsx
{herb_name}targets.xlsx
These files are stored in:

./成分靶点数据/
Step 2: Filtering and Matching Downloaded Data
The script Separation of Downloaded TCMSP Data.py processes the downloaded TCMSP files by:

Reading the ingredient table and target table of a herb
Filtering compounds using the following criteria:
OB (%) >= 30
DL >= 0.18
Selecting qualified compounds
Merging them with the target table via Mol ID
Exporting the final compound–target relationships
Final output example:

Final_result-Rhododendronmolle.xlsx
The final result contains:

Mol ID
Target name
Requirements
Python Version
Recommended:

Python 3.8+
Required Packages
Install the following dependencies before running the scripts:

pip install selenium beautifulsoup4 lxml pandas openpyxl
Required Python libraries:

selenium
beautifulsoup4
lxml
pandas
openpyxl
Browser and Driver Setup
Because the retrieval script uses Selenium with Google Chrome, you need:

A local installation of Google Chrome
A compatible version of ChromeDriver
ChromeDriver added to your system environment variable, or manually specified in the script
Usage
1. Prepare Herb Name Input
Make sure herb_name.xlsx contains the herb names to be queried.

Example:

Herb Name
甘草
黄芩
当归
The script reads the first column without a header.

2. Configure the Working Directory
In Automated Data Retrieval from the TCMSP Database.py, the working path is currently hardcoded:

os.chdir("D:\\R")
You should modify it to your local project path, for example:

os.chdir("C:\\Users\\YourName\\Desktop\\OptiSyn")
Also update the input file path:

herb = pd.read_excel('D:/R/herb_name.xlsx', header=None)
It is recommended to replace it with a relative path:

herb = pd.read_excel('./herb_name.xlsx', header=None)
3. Run the TCMSP Retrieval Script
python "Automated Data Retrieval from the TCMSP Database.py"
After execution, the script creates the folder:

成分靶点数据
and saves herb-specific ingredient and target files there.

4. Configure Paths in the Filtering Script
In Separation of Downloaded TCMSP Data.py, the current example uses:

file_path1 = r'D:\R\成分靶点数据\Rhododendronmolleingredients.xlsx'
file_path2 = r'D:\R\成分靶点数据\Rhododendronmolletargets.xlsx'
Please change these paths to match your generated files.

The output path is also hardcoded:

final_result.to_excel(r'F:\GA\今天好好找中药了吗\gene\Final_result-Rhododendronmolle.xlsx', index=False)
It is recommended to replace it with a relative path, such as:

final_result.to_excel('./Final_result-Rhododendronmolle.xlsx', index=False)
5. Run the Filtering Script
python "Separation of Downloaded TCMSP Data.py"
This will generate the filtered compound–target result file.

Filtering Criteria
The filtering step uses the following commonly adopted TCMSP screening thresholds:

OB (%): Oral Bioavailability, threshold >= 30
DL: Drug-Likeness, threshold >= 0.18
Filtering code:

filtered_df = df1[(df1['OB (%)'] >= 30) & (df1['DL'] >= 0.18)]
These thresholds can be adjusted depending on specific research needs.

Output
Retrieval Script Output
For each herb:

herb_nameingredients.xlsx
herb_nametargets.xlsx
Filtering Script Output
For each processed herb:

Final_result-<HerbName>.xlsx
Final columns include:

Mol ID
Target name
Notes
Hardcoded paths must be updated before running the scripts
The current code uses local Windows absolute paths.
Website structure changes may break the crawler
Since the script relies on XPath and current TCMSP page layout, future website updates may require code modification.
Network speed affects scraping stability
Slow loading or connection interruption may cause incomplete retrieval.
The current script uses limited exception handling
It only handles the case where a herb is not found. More robust logging and retry mechanisms are recommended for large-scale use.
Headless mode is not fully enabled in the current implementation
Although the code defines:
fp = Options()
fp.add_argument('-headless')
this configuration is not actually passed into the driver initialization. If headless execution is desired, the driver setup should be updated accordingly.
Target page iteration may miss boundary cases
The target-page loop currently uses:
for _ in range(targets_page - 1):
which may require revision depending on the actual number of pages and data completeness.
Suggested Improvements
Replace absolute paths with relative paths
Add support for batch summary export across multiple herbs
Improve exception handling and retry logic
Add logging for failed retrievals
Normalize target names using UniProt or gene symbols
Refactor scripts into reusable functions or modules
Enable true headless browser execution
Improve pagination handling robustness
Application Scenarios
This preprocessing branch is suitable for:

Active compound screening in TCM research
Herb–compound–target network construction
Network pharmacology preprocessing
Herb target mining
Preparing structured inputs for graph-based models such as GCNs
Herbal synergy analysis workflows
Acknowledgement
This work relies on data provided by the TCMSP database for herb-related compound and target information.

Citation Suggestion
If you use this branch in your research, please indicate that:

TCMSP was used as the source of herb compound and target data
Active compounds were screened based on OB and DL thresholds
