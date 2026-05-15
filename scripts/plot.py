import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

input_path = snakemake.input[0]
output_path = snakemake.output[0]
n = snakemake.params.n

df = pd.read_csv(input_path)

# Ensure k is treated as a categorical axis (preserves order)
k_order = sorted(df["k"].unique())
df["k"] = pd.Categorical(df["k"], categories=k_order, ordered=True)
k_labels = [f"k={k}" for k in k_order]

fig, ax = plt.subplots(figsize=(10, 6))

sns.boxplot(
    data=df,
    x="k",
    y="mean",
    order=k_order,
    color="white",
    linecolor="black",
    flierprops={"marker": ".", "color": "black"},
    ax=ax,
)

true_mean = (1 + n) / 2
ax.axhline(true_mean, color="red", linestyle="--", linewidth=1, label=f"True mean = {true_mean}")

ax.set_title(f"Testing Draws for {n}", fontsize=14)
ax.set_xlabel("k (number of draws)", fontsize=12)
ax.set_ylabel("Mean", fontsize=12)
ax.set_xticklabels(k_labels, rotation=15)
ax.legend()

plt.tight_layout()
plt.savefig(output_path, dpi=150)
plt.close()

print(f"Plot saved to {output_path}")
