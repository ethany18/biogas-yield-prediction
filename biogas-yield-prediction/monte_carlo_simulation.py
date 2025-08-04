import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# define constants
n_simulations = 1000
n_days = 100

# storage
results = []

# Monte Carlo Simulation
for i in range(n_simulations):
    np.random.seed(i)

    data = {
        "Starch_input": np.random.normal(200, 50, n_days),
        "Fat_input": np.random.normal(100, 30, n_days),
        "Protein_input": np.random.normal(150, 40, n_days),
    }

    df = pd.DataFrame(data)

    # calculate methane yield
    df["Methane_yield"] = (
        0.35 * df["Starch_input"] +
        0.6 * df["Fat_input"] +
        0.3 * df["Protein_input"] +
        0.001 * np.random.normal(1.0, 0.05, n_days)
    )

    avg_yield = df["Methane_yield"].mean()
    results.append(avg_yield)


# convert results to DataFrame
sim_results = pd.DataFrame({'Average_Methane_Yield': results})

# save results (optional)
sim_results.to_csv("data/monte_carlo_results.csv", index=False)

# plot histogram
plt.figure(figsize=(8, 5))
sns.histplot(sim_results['Average_Methane_Yield'], kde=True, bins=30)
plt.title("Distribution of Average Methane Yields (Monte Carlo)")
plt.xlabel("Average Methane Yield (L/day)")
plt.ylabel("Frequency")
plt.show()
