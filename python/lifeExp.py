# File Information
# Version: 0.50.01 (Pre-Beta)
# Creator: Michael Yurachek
# Last updated: 05 / 30 / 2024

import os
import matplotlib.pyplot as plt
import pandas as pd

# Read data from CSV file
df = pd.read_csv('./assets/csv/lifeExpectancy.csv')

# Convert 'Exact Age' column to integers
df['Exact Age'] = df['Exact Age'].astype(int)

# Extract data
age = df['Exact Age']
dProbM = df['Death Probability (Male)']
dProbF = df['Death Probability (Female)']

# Plotting
plt.figure(figsize=(10,6))

# Plot male death probability with blue color and solid line
plt.plot(age, dProbM, color='blue', linestyle='-', linewidth=2, label='Male Death Probability')

# Plot female death probability with hotpink color and dashed line
plt.plot(age, dProbF, color='hotpink', linestyle='--', linewidth=2, label='Female Death Probability')

# Add labels and title
plt.xlabel('Exact Age')
plt.ylabel('Death Probability')
plt.title('The Average Death Probability By Gender')

# Add legend
plt.legend()

# Add gridlines
plt.grid(True, linestyle='--', alpha=0.6)

# Adjust x-axis ticks to show every 5 years
plt.xticks(range(min(age), max(age) + 1, 5))  # Set x-axis ticks to every 10 years

# Save plot image
strFile = "./assets/images/graphs/genderDeathProbGraph.png"
if os.path.isfile(strFile):
    os.remove(strFile)   # Remove the existing file if it exists
plt.savefig(strFile)

# Show plot
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()

os.system('cls||clear')
