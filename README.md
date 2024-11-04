# IDS 706 Data Engineering Mini Project 9
[![Format](https://github.com/jessc0202/Sizhe_Chen_mini_Project_9/actions/workflows/format.yml/badge.svg)](https://github.com/jessc0202/Sizhe_Chen_mini_Project_9/actions/workflows/format.yml)
[![Install](https://github.com/jessc0202/Sizhe_Chen_mini_Project_9/actions/workflows/install.yml/badge.svg)](https://github.com/jessc0202/Sizhe_Chen_mini_Project_9/actions/workflows/install.yml)
[![Lint](https://github.com/jessc0202/Sizhe_Chen_mini_Project_9/actions/workflows/lint.yml/badge.svg)](https://github.com/jessc0202/Sizhe_Chen_mini_Project_9/actions/workflows/lint.yml)
[![Test](https://github.com/jessc0202/Sizhe_Chen_mini_Project_9/actions/workflows/test.yml/badge.svg)](https://github.com/jessc0202/Sizhe_Chen_mini_Project_9/actions/workflows/test.yml)

# Alcohol Consumption Data Analysis

This project analyzes global alcohol consumption patterns, focusing on beer, spirits, wine, and total alcohol consumption across different countries by using Cloud-Hosted Notebook. The analysis includes basic statistics, correlation matrices, and visualizations of alcohol consumption. The results are saved in a summary markdown file with accompanying charts.

## Project Structure

- `main.py`: Main entry point for the project. This script loads the data, performs basic analysis, generates visualizations, and saves the analysis to a markdown summary.
- `mylib/lib.py`: Contains utility functions for loading, processing, and visualizing the data. This modular approach keeps the main script clean and makes functions reusable.
- `test_main.py` and `test_lib.py`: Unit tests for the functions in `main.py` and `lib.py` respectively.
- `requirements.txt`: Lists the required Python packages to run the project.
- `README.md`: Provides an overview of the project.

## Data Source

The data used in this project is from the [FiveThirtyEight's alcohol consumption dataset](https://github.com/fivethirtyeight/data/). The dataset contains information about beer, spirit, and wine servings per capita, as well as the total liters of pure alcohol consumed per capita across various countries.

### Dataset URL
[Dataset Link](https://raw.githubusercontent.com/fivethirtyeight/data/refs/heads/master/alcohol-consumption/drinks.csv)

### Video Demonstrating
[Youtube Link](https://www.youtube.com/watch?v=nSjfec2Xx8I)

## Project Setup

### Prerequisites

This project requires Python 3 and the following libraries:
- `pandas`
- `matplotlib`
- `seaborn`

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd <project-directory>
   ```

## Usage
### Run the main analysis script:

```
python main.py
```

This will:

Load the dataset.
Perform basic statistical analysis and print results.
Generate various visualizations.
Save the analysis summary and visualizations as a markdown file `alcohol_consumption_summary.md` and PNG images.

### The summary markdown file (alcohol_consumption_summary.md) includes:

Basic statistics of alcohol consumption.
Top 5 countries by total alcohol consumption.
Correlation matrix of beer, spirits, wine, and total alcohol consumption.
Visualizations showing average servings, top countries by consumption, distribution plots, and alcohol consumption categories.

### Running Tests:

You can run tests to verify the functionality of the code. Use the following command:

```
pytest
```

## Functionality Overview

- **Data Preprocessing**: `load_and_preprocess` function loads and renames columns for consistency.
- **Statistical Analysis**:
  - `calculate_basic_stats` provides descriptive statistics.
  - `compute_correlation_matrix` generates a correlation matrix.
- **Top N Analysis**: `get_top_countries_by_alcohol` retrieves the top countries by alcohol consumption.
- **Visualization**:
  - `plot_average_servings`: Bar plot showing average servings of beer, spirits, and wine.
  - `plot_top_countries`: Bar plot of the top 5 countries by total alcohol consumption.
  - `plot_servings_distributions`: Histogram plots for each type of drink.
  - `classify_and_count_categories`: Categorizes countries into low, moderate, and high alcohol consumption categories and visualizes them.
- **Markdown Report**: `save_to_markdown` saves a markdown summary of the analysis with embedded images.

## Visualizations

The project generates and saves the following images:

- **average_servings.png**: Average servings of beer, spirits, and wine.
- **top_countries.png**: Top 5 countries by total alcohol consumption.
- **beer_distribution.png**, **spirit_distribution.png**, **wine_distribution.png**, **total_alcohol_distribution.png**: Distribution histograms for each type of alcohol.
- **consumption_category.png**: Bar plot of the number of countries by alcohol consumption category.


## References 
https://github.com/nogibjj/python-ruff-template