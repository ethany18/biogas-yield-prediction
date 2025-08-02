import numpy as np
import pandas as pd
import os

# Make sure the 'data' folder exists
os.makedirs("data", exist_ok=True)

np.random.seed(42)
n_days = 100

data = {
    'Date': pd.date_range(start='2025-01-01', periods=n_days),
    'Starch_input': np.random.normal(200, 50, n_days),
    'Fat_input': np.random.normal(100, 30, n_days),
    'Protein_input': np.random.normal(150, 40, n_days),
    'Volume_input': np.random.normal(50, 5, n_days),
    'Temperature': np.random.normal(35, 2, n_days),
    'pH': np.random.normal(7.0, 0.3, n_days),
    'OLR': np.random.normal(2.5, 0.5, n_days),
    'HRT': np.random.normal(20, 5, n_days),
}

df = pd.DataFrame(data)

# Methane Yield model
df['Methane_yield'] = (0.35 * df['Starch_input'] +
                       0.6 * df['Fat_input'] +
                       0.3 * df['Protein_input']) * 0.001 * np.random.normal(1.0, 0.05, n_days)

df['Electricity_generated'] = df['Methane_yield'] * \
    0.01  # Assuming 10 kWh per 1 m³

# Save to CSV
df.to_csv("data/biogas_data.csv", index=False)

print("✅ Data simulated and saved to data/biogas_data.csv")
print(df.head())


# This code simulates biogas production data and saves it to a CSV file.
# It generates random values for inputs like starch, fat, protein, and calculates methane yield and electricity generated based on a simple model.
# The data is saved in a 'data' folder, which is created if it doesn't exist.
# The simulation runs for 100 days starting from January
