# TCGA-BRCA Somatic Variant Analysis Pipeline

A computational workflow for exploring and characterizing somatic single-nucleotide variants (SNVs) and indels across the **TCGA Breast Invasive Carcinoma (BRCA)** cohort, focusing on high-confidence deleterious alterations in key tumor suppressor genes (*BRCA1* and *BRCA2*).

---

## 📌 Project Overview
- **Cohort:** The Cancer Genome Atlas (TCGA-BRCA)
- **Sample Size:** 1,009 primary breast cancer tumor samples
- **Target Genes:** *BRCA1*, *BRCA2*
- **Primary Finding:** Identification and structural classification of **62 high-confidence deleterious somatic mutations** across frameshift indels, nonsense single nucleotide variants, and splice-site disrupting mutations.

---

## 🔬 Analytical Workflow
1. **Cohort Data Retrieval:** Explored open-access whole-exome sequencing somatic mutation calls (MAF format) from the GDC Data Portal.
2. **Quality & Effect Filtering:** 
   - Applied variant quality criteria to eliminate low-depth and artifactual calls.
   - Filtered for high-impact protein-truncating consequences (nonsense, frameshift insertions/deletions, canonical splice donor/acceptor alterations).
3. **Clinical & Functional Annotation:**
   - Cross-referenced variants against curated clinical knowledge bases (ClinVar, COSMIC).
   - Characterized mutational clustering across key functional domains (e.g., zinc-finger, RING, and BRCT domains).

---

## 🛠 Tools & Stack
- **Language:** Python
- **Libraries/Modules:** Data structures, tabular exploration, and sequence handling
- **Platforms & Portals:** TCGA GDC Data Portal, UCSC Genome Browser / Ensembl
- **Environment:** Jupyter Notebook, VS Code

---

## 👤 Author
- **Sarmitha K** – Undergraduate Student, B.Sc. Biotechnology, PSG College of Arts and Science
- **GitHub:** [@SarmithaK](https://github.com/SarmithaK)
- **LinkedIn:** [Sarmitha K](https://www.linkedin.com/in/sarmitha-k-4a9156305)
