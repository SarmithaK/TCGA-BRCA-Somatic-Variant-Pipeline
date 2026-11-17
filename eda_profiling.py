import os
import pandas as pd

# 1. Define file path (data folder kulla data_mutations.txt irukku)
file_path = os.path.join("data", "data_mutations.txt")

print("=" * 60)
print("Loading TCGA Breast Invasive Carcinoma Dataset...")
print("=" * 60)

# 2. Read only the most essential genomic columns
columns_to_load = [
    "Hugo_Symbol",
    "Variant_Classification",
    "Variant_Type",
    "Tumor_Seq_Allele2",
    "HGVSp_Short",
    "Tumor_Sample_Barcode",
]

# Read the tab-delimited file, skipping any metadata/header comment lines starting with #
df = pd.read_csv(
    file_path,
    sep="\t",
    comment="#",
    low_memory=False,
    usecols=columns_to_load,
)

print(f"Total somatic mutations across all genes: {len(df):,}")
print(f"Total unique patient samples: {df['Tumor_Sample_Barcode'].nunique():,}")

# 3. Filter specifically for BRCA1 and BRCA2
brca_df = df[df["Hugo_Symbol"].isin(["BRCA1", "BRCA2"])].copy()

print("\n" + "=" * 60)
print("BRCA1 & BRCA2 MUTATION OVERVIEW")
print("=" * 60)
print(f"Total BRCA mutations: {len(brca_df)}")
print(brca_df["Hugo_Symbol"].value_counts())

# 4. Breakdown by Variant Classification (Missense, Nonsense, Frameshift, etc.)
print("\n" + "=" * 60)
print("VARIANT CLASSIFICATION SUMMARY")
print("=" * 60)
summary = (
    brca_df.groupby(["Hugo_Symbol", "Variant_Classification"])
    .size()
    .unstack(fill_value=0)
)
print(summary)

# 5. Top recurrent protein changes (Hotspots)
print("\n" + "=" * 60)
print("TOP PROTEIN MUTATIONS (HGVSp_Short)")
print("=" * 60)
print(brca_df["HGVSp_Short"].value_counts().head(10))

# 6. Save the filtered BRCA mutations for our next analysis steps
output_path = os.path.join("data", "filtered_brca_mutations.csv")
brca_df.to_csv(output_path, index=False)
print(f"\nFiltered BRCA data successfully saved to: {output_path}")
print("=" * 60)
import matplotlib.pyplot as plt
import seaborn as sns

# 7. Visualizing the Data (EDA)
print("\n" + "=" * 60)
print("GENERATING VISUALIZATIONS...")
print("=" * 60)

# Plot 1: BRCA1 vs BRCA2 Mutation Counts
plt.figure(figsize=(8, 5))
sns.countplot(data=brca_df, x='Hugo_Symbol', palette='Set2')
plt.title('Total Somatic Mutations: BRCA1 vs BRCA2')
plt.xlabel('Gene')
plt.ylabel('Mutation Count')
plt.savefig('data/brca_mutation_counts.png', dpi=300, bbox_inches='tight')
plt.close()

# Plot 2: Variant Classification Breakdown
plt.figure(figsize=(10, 6))
sns.countplot(data=brca_df, y='Variant_Classification', hue='Hugo_Symbol', palette='viridis')
plt.title('Variant Classification in BRCA1 & BRCA2')
plt.xlabel('Mutation Count')
plt.ylabel('Mutation Type')
plt.legend(title='Gene')
plt.savefig('data/variant_classification.png', dpi=300, bbox_inches='tight')
plt.close()

print("Visualizations successfully saved as PNG files in the 'data' folder!")
print("=" * 60)