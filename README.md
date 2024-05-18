# Advertising Budget Allocation for Target Sales

## Project Overview

This project utilizes linear and multiple regression analyses to optimize the allocation of an advertising budget across different channels (TV, radio, newspaper) to achieve a specific sales target. By analyzing historical advertising and sales data, we can make informed decisions about how to distribute a given budget to maximize sales.

## Data

The dataset used in this project contains information on advertising expenditures in TV, radio, and newspapers along with the corresponding sales figures. The data is stored in a CSV file named `Advertising.csv`.

## Methodology

1. **Linear Regression**: We perform linear regression separately for each advertising medium (TV, radio, newspaper) to understand their individual impact on sales.
2. **Multiple Regression**: We perform multiple regression using all three advertising mediums simultaneously to understand their combined effect on sales.
3. **Budget Allocation**: Based on the regression coefficients from the multiple regression model, we proportionally distribute the given budget to each advertising medium to achieve the target sales.

## Results

- **TV Advertising**: Significant positive impact on sales.
- **Radio Advertising**: Significant positive impact on sales.
- **Newspaper Advertising**: Insignificant and minimal impact on sales when considered alongside TV and radio.

## Requirements

- Python 3.7+
- pandas
- statsmodels
- numpy

You can install the required packages using:
```bash
pip install pandas statsmodels numpy
```

## Usage
- Clone the repository:
```
git clone https://github.com/yourusername/advertising-budget-allocation.git
cd advertising-budget-allocation
```

- Place the dataset (Advertising.csv) in the project directory.
- Run the regression analysis:
```
python Regression.py
```

## Files
- Advertising.csv: The dataset containing advertising expenditure and sales data.
- Regression.py: The Python script that performs the regression analyses and prints the results.

