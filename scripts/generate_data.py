import numpy as np
import pandas as pd

n = snakemake.params.n
k_values = snakemake.params.k_values
repeats = snakemake.params.repeats
output_path = snakemake.output[0]

rows = []
for k in k_values:
    for rep in range(repeats):
        samples = np.random.randint(1, n + 1, size=k)
        mean_val = samples.mean()
        rows.append({"k": k, "repeat": rep + 1, "mean": mean_val})

df = pd.DataFrame(rows)
df.to_csv(output_path, index=False)

print(f"Data saved to {output_path} — n={n}, k_values={k_values}, repeats={repeats}")
