# File Information
# Version: 0.00.04 (Pre-Alpha) 
# Creator: Michael Yurachek
# Last updated: 05 / 23 / 2024

import os
import matplotlib.pyplot as plt
import pandas as pd

# Read data from CSV file
df = pd.read_csv('./assets/csv/incomeAverage.csv')

# Convert 'Year' column to integers
df['Year'] = df['Year'].astype(int)

# Extract data
yr = df['Year']
maleInc = df['Avg Income (Male)']
femaleInc = df['Avg Income (Female)']

# Plotting
plt.figure(figsize=(10,6))

# Plot male high school GPA with blue color and solid line
plt.plot(yr, maleInc, color='blue', linestyle='-', linewidth=2, label='Male Average Income')

# Plot female high school GPA with hotpink color and dashed line
plt.plot(yr, femaleInc, color='hotpink', linestyle='--', linewidth=2, label='Female Average Income')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Average Income')
plt.title('Average Income By Gender By Year')

# Add legend
plt.legend()

# Add gridlines
plt.grid(True, linestyle='--', alpha=0.6)

# Adjust x-axis ticks
plt.xticks(yr, rotation=45)  # Rotate x-axis labels for better readability

# Save plot image
strFile = "./assets/images/graphs/genderIncomeGraph.png"
if os.path.isfile(strFile):
    os.remove(strFile)   # Remove the existing file if it exists
plt.savefig(strFile)

# Show plot
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()

os.system('cls||clear')