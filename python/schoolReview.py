# File Information
# Version: 0.50.01 (Pre-Beta)
# Creator: Michael Yurachek
# Last updated: 05 / 30 / 2024

import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Function to interpolate or truncate data to fit 10 points
def fit_to_ten_points(series):
    if len(series) < 10:
        # Interpolate to get 10 points
        return np.interp(np.linspace(0, len(series)-1, 10), np.arange(len(series)), series)
    elif len(series) > 10:
        # Truncate to 10 points
        return series[:10]
    else:
        return series

# Read data from CSV file
df = pd.read_csv('./assets/csv/schoolWork.csv')

# Extract data (ensure these columns exist in your CSV)
try:
    adv_diploma = fit_to_ten_points(df['More likely to graduate high school with an advanced diploma.'])
    std_classes = fit_to_ten_points(df['More likely to take standard classes.'])
    adv_classes = fit_to_ten_points(df['More likely to take advanced classes like AP or honors.'])
    std_diploma = fit_to_ten_points(df['More likely to graduate with a standard diploma.'])
except KeyError as e:
    print(f"Column not found in the CSV file: {e}")
    exit()

# Create a line graph
plt.figure(figsize=(12, 8))
plt.plot(range(1, 11), adv_diploma, marker='o', linestyle='-', linewidth=2.5, label='Advanced Diploma')
plt.plot(range(1, 11), std_classes, marker='s', linestyle='--', linewidth=2.5, label='Standard Classes')
plt.plot(range(1, 11), adv_classes, marker='^', linestyle='-.', linewidth=2.5, label='Advanced Classes')
plt.plot(range(1, 11), std_diploma, marker='d', linestyle=':', linewidth=2.5, label='Standard Diploma')

# Adding titles and labels
plt.title('Survey Opinion On High School Topics By Gender', fontsize=16)
plt.xlabel('Scale (1 = Female, 10 = Male)', fontsize=14)
plt.ylabel('Likelihood', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(fontsize=12)

# Adding grid lines
plt.grid(True, linestyle='--', alpha=0.7)

# Save plot image
strFile = "./assets/images/graphs/educationalOutcomesGraph.png"
if os.path.isfile(strFile):
    os.remove(strFile)   # Remove the existing file if it exists
plt.savefig(strFile)

# Adjust layout to prevent clipping of labels and show plot
plt.tight_layout()
plt.show()

# Clear console (works on Windows and Unix-based systems)
os.system('cls' if os.name == 'nt' else 'clear')
