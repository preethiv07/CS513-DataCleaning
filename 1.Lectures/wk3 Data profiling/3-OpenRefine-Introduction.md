# Lecture: OpenRefine Introduction

## ✅ Summary

This lecture gives a hands-on introduction to **OpenRefine**, a data wrangling tool designed to help users clean and normalize messy datasets through faceting, clustering, and transformations. It demonstrates importing datasets, performing normalization, and using OpenRefine’s **facets**, **clustering**, and **provenance tracking** capabilities.

Key operations demonstrated include:
- Creating a project and importing data
- Using **Text**, **Timeline**, and **Scatterplot** facets
- Cleaning inconsistencies through **clustering**
- Tracking changes via **Operation History**

Two datasets are used:
- USDA Farmers Market Directory (relatively clean)
- NYPL Historic Menus (messy, crowdsourced)

---

## 📚 Details

### 🔸 What is OpenRefine?

**OpenRefine** (formerly Google Refine) is a tool for:
- **Data profiling**: understanding your data
- **Detecting and fixing** data quality issues
- **Transforming and linking** data from different sources

---

### 🔸 Getting Started: Import and Project Setup

Steps:
1. Click **Create Project** in OpenRefine.
2. Import a CSV, TSV, or Excel file.
3. Use default settings or customize import options.
4. Assign a meaningful project name.

🗂️ Example: USDA dataset with **8,664 rows** successfully imported.

---

### 🔸 Text Facets: The Workhorse

- Apply **Text Facet** on a column (e.g., `MarketName`)
- Reveals the number of unique entries
- Helps find duplicates or variations

🛠️ Example:
- `MarketName` had **8,095 unique values**
- Top repeated value: `"El Mercado Familiar"` (33 times)

---

### 🔸 Clustering for Normalization

- Hit the **Cluster** button to detect similar strings
- Review suggestions and **merge similar values**
- Choose canonical form and **mass-edit** values

💡 Example:
- Correcting four spellings of “Irvington Farmers Market”
- Reduced unique values from **8,095 to 7,846**

🧠 You can:
- Merge clusters all at once
- Re-run clustering iteratively for cleaner results

---

### 🔸 Provenance with Operation History

- Use **Undo/Redo** tab to see every operation performed
- Enables:
  - Reapplying transformations to new data
  - Documenting your cleaning process

📦 Export your transformation steps for reuse!

---

### 🔸 Timeline Facet: Visualizing Temporal Data

Steps:
1. Convert string column (e.g., `updateTime`) to **Date**
2. Apply **Timeline Facet** to analyze time distribution

Findings:
- Missing data in early years (e.g., 2010–2011)
- More complete data in 2012 onward

🧠 Helps profile time-based trends or data gaps.

---

### 🔸 Scatterplot Facet: Geospatial Insights

Steps:
1. Convert `x` and `y` columns to **Number** type
2. Apply **Scatterplot Facet**

📍 Result:
- Visual outline of **U.S. farmers market locations**
- Includes points in **Alaska** and **Hawaii**
- Easily exportable to **Google Maps**

---

### 🔸 Complex Data: NYPL Menus

- Crowdsourced data with inconsistencies:
  - Different spellings of the same restaurant
  - Evolving business names over time

🧠 Lesson:
- Even curated data may have deep normalization issues
- Use clustering thoughtfully, especially when names may change over time

---

### 🔸 Types of Clustering Algorithms

| Method               | Description |
|----------------------|-------------|
| **Key Collision**    | Fastest, safest (e.g., Fingerprint, Ngram) |
| **Metaphone**        | Sound-based (English pronunciation) |
| **Nearest Neighbor** | Edit-distance based (PPM, Levenshtein) |

⚠️ **Caution**: Don't cluster unrelated names like:
- `"Hotel Savoy, NY"` vs `"Savoy Hotel, London"`

---

### 🧠 Summary of What You Learned

- ✅ Import and normalize datasets
- ✅ Use facets: **Text**, **Timeline**, **Scatterplot**
- ✅ Apply clustering to merge similar values
- ✅ Track steps via **Operation History**
- ✅ Prepare clean, georeferenced, and temporally profiled data

> OpenRefine is a lightweight but powerful tool that enables **fast iteration and deep insight** for cleaning real-world messy data.

---