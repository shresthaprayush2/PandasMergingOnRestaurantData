# PandasMergingOnRestaurantData
This repository contains a Python script designed to merge and clean restaurant performance data from multiple CSV files. The data is sourced from various time frames (weekly, monthly, yearly) and is combined into a single dataset for easier analysis and insights. The project demonstrates the use of Pandas for data manipulation and cleaning, making it a great resource for students learning data processing in Python.

# Nepvent Data Merging

Welcome to the Nepvent Data Merging repository! This project showcases how to efficiently merge and clean data from multiple CSV files using Python and Pandas. If you're learning data manipulation with Pandas, this repository will provide a practical example to help you understand the process.

## Project Overview

In this project, we have performance data from different Nepvent restaurant clients, extracted from Google Analytics in various formats (weekly, monthly, and yearly). The goal is to combine all this data into a single dataset to give the marketing team actionable insights.

### Key Features

- **Extracting Consistent Restaurant Names:** The script includes a function that cleans and standardizes restaurant names across all datasets, ensuring consistency.
- **Merging Data:** We demonstrate how to merge datasets on a common key (restaurant name) using Pandas' `merge` function.
- **Data Cleaning:** Basic data cleaning techniques are applied to ensure the final dataset is accurate and ready for analysis.

# Here’s a quick rundown of what the script does:

    Extracting Restaurant Names: The function changePageTitle() extracts the restaurant names from the page titles, ensuring consistency across datasets.

    Selecting Relevant Columns: We only select the columns needed for our analysis, reducing the data size and improving efficiency.

    Merging Data: Data from weekly, monthly, and yearly CSV files is merged on the restaurant name, using outer joins to ensure no data is lost.

    Final Export: The cleaned and merged data is exported to a new CSV file, ready for analysis.

# Contributing

If you have suggestions or improvements, feel free to fork the repository and submit a pull request. Contributions are welcome!
**


