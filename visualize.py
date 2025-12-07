import pandas as pd
import matplotlib.pyplot as plt
import os

# Set paths (adjust if needed)
project_dir = 'output/project'
plots_dir = 'plots'
os.makedirs(plots_dir, exist_ok=True)

# Example 1: Plot top 10 taxa from taxonomic profile (assumes 'project.taxa.txt' is tab-delimited with columns like 'Taxon' and 'Abundance')
taxa_file = os.path.join(project_dir, 'project.taxa.txt')  # Replace with your actual file
df_taxa = pd.read_csv(taxa_file, sep='\t')  # Adjust sep if not tab

# Sort by abundance (assuming a column 'Abundance' or similar; check your file)
df_taxa = df_taxa.sort_values(by='Abundance', ascending=False).head(10)  # Replace 'Abundance' with actual column name

# Bar plot
plt.figure(figsize=(10, 6))
plt.barh(df_taxa['Taxon'], df_taxa['Abundance'])  # Replace column names as needed
plt.xlabel('Abundance')
plt.ylabel('Taxon')
plt.title('Top 10 Taxa in Microbiome')
plt.tight_layout()
plt.savefig(os.path.join(plots_dir, 'top_taxa_bar.png'))
plt.close()

# Example 2: Pie chart for functional categories (e.g., from 'project.functions.txt' with 'Function' and 'Count')
func_file = os.path.join(project_dir, 'project.functions.txt')
df_func = pd.read_csv(func_file, sep='\t')
df_func = df_func.sort_values(by='Count', ascending=False).head(5)  # Top 5 functions

# Pie chart
plt.figure(figsize=(8, 8))
plt.pie(df_func['Count'], labels=df_func['Function'], autopct='%1.1f%%')
plt.title('Top Functional Categories')
plt.savefig(os.path.join(plots_dir, 'functional_pie.png'))
plt.close()

print("Plots saved to:", plots_dir)
