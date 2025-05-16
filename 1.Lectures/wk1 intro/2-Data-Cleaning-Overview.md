# Lecture: Data Cleaning Overview

## ✅ Summary

This lecture introduces the core concept of **data cleaning (aka data wrangling)** and its role in the broader data science lifecycle. It emphasizes that data cleaning is essential — though often overlooked — and makes up the bulk of the effort in real-world data projects.

Key points discussed include:
- The **difference between data wrangling and analytics**, and why wrangling matters more than it gets credit for.
- Real-world **costs of low-quality data**: monetary loss, confusion, inefficiencies, and even legal risks.
- The **goal of data cleaning**: understanding, assessing, and improving data quality.
- Introduction to key **error types** (quantitative vs qualitative).
- Course themes and tools: regular expressions, OpenRefine, SQL/Datalog, and workflow/provenance tracking using YesWorkflow.

---

## 📚 Details

### 🔷 What is Data Wrangling?

**Data wrangling** involves preparing raw data for meaningful analysis. It includes:
- ETL: Extract, Transform, Load
- Data integration
- Cleaning and querying
- Repairing inconsistencies

🧠 **Key insight**: While data analytics is the “glamorous” part of data science, **80% of the work is in wrangling**, and it’s what makes reliable analytics possible.

---

### 🔸 Skills Data Scientists Need

A study of LinkedIn job data (CrowdFlower) shows:
- SQL is the **most in-demand** skill.
- Other database skills (Oracle, PostgreSQL, NoSQL) also highly valued.

📌 Even though this course doesn’t teach SQL directly, you are expected to **think like a database person**.

---

### 🔸 The High Cost of Dirty Data

Low-quality data leads to both **direct and indirect losses**. Examples include:
- Rework costs, re-entry, misinterpretation
- Lost customers, lost revenue, lawsuits
- System migration, privacy violations, failed operations

Source: *Ge & Helfert, Handbook of Data Quality*

💡 Takeaway: Dirty data is costly even if you choose to ignore or live with it.

> BUNK Cost:A sunk cost in a bad or worthless investment.
---

### 🔸 What is the Goal of Data Cleaning?

Data cleaning aims to:
- **Understand**: What’s wrong with the data?
- **Assess**: What needs fixing?
- **Improve**: Clean it to meet the standards.

This can be remembered via the **three Qs**:
1. **Quality Dimensions** – Accuracy, Timeliness, Completeness, Relevance
2. **Fitness for Use** – Is it good enough to answer our questions?
3. **Queries** – Use SQL/Datalog to profile, validate, and clean data.

---

### 🔸 Where Does Cleaning Fit in the Lifecycle?

The data lifecycle looks like this:

```text
Gather → Profile → Clean → Analyze
```

However, in reality, this is not a strict pipeline — it’s often cyclical:
	•	Data profiling identifies errors
	•	Cleaning standardizes and fixes them
	•	Controlled vocabularies and reference dictionaries help with normalization
	•	Data integration introduces new errors due to source mismatches

### 🔸 Types of Data Errors

From Abedjan et al.'s taxonomy:

| Type                  | Description                                      | Tools Used                      |
|-----------------------|--------------------------------------------------|----------------------------------|
| **Quantitative Errors** | Outliers or numerical anomalies                  | Statistical or ML-based methods (not in this course) |
| **Qualitative Errors**  | Syntax or schema issues — the course’s main focus | Regex, SQL, Datalog, OpenRefine |

**Subtypes of qualitative errors include:**

- **Syntactic violations**:  
  _e.g., multiple ways to write the same date or place_  
  ➤ Fixable via regex, OpenRefine, or controlled vocabularies.

- **Schema/Integrity Constraint Violations**:  
  _e.g., Foreign key mismatch like PERSON.ZIP not matching ADDRESS.ZIP_  
  ➤ Fixable via SQL or Datalog rules.

- **Duplicates**:  
  _e.g., “Joe Doe” appearing twice with different spellings or IDs_  
  ➤ Fixable via matching and de-duplication tools.

---

### 🔸 Tools and Themes You’ll Learn

| Theme              | Concepts & Tools Covered                            |
|--------------------|-----------------------------------------------------|
| **Syntax**         | Use of **regular expressions** to identify and transform patterns |
| **OpenRefine**     | GUI tool to clean, transform, and cluster data before DB import |
| **Schema & Semantics** | Use **SQL and Datalog** to define and enforce data rules (ICs) |
| **Synthesis & Provenance** | Use **YesWorkflow** to model scripts as workflows and track data lineage |


### 🔸 Real Data Example: Issues Even After Cleaning

Even after using OpenRefine or scripts, issues might persist:
	•	Duplicate IDs (e.g., two persons with ID 43)
	•	Format inconsistencies (name order, date formats)
	•	Empty or placeholder values (e.g., 999-999-9999, NULL)
	•	Referential integrity violations (missing ZIP code in ADDRESS table)

📌 Database constraints and SQL/Datalog rules will help us detect and address these.

### 🔸 Workflow Automation and Provenance
	•	In real-world projects, data cleaning is often done via scripts.
	•	YesWorkflow lets us:
	•	Annotate those scripts
	•	Visualize them as workflows
	•	Track data lineage and dependencies

This is key for reproducibility and auditability in data science pipelines.

### 🧠 Closing Thought

Data cleaning isn’t glamorous, but it’s the foundation of every reliable analysis.
