# Lecture: Data Quality Defined

## ✅ Summary

This lecture defines **data quality** as “fitness for use” — meaning data is considered high quality if it supports the intended purpose, whether it’s analysis, decision-making, or operations. 

The lecture outlines the practical challenges in applying this definition depending on context, such as when data is archived versus when it is curated. It introduces a framework for understanding and improving data quality through:

- **Types of Data Errors**: Quantitative (outliers) and Qualitative (format/schema)
- **Three Pillars of Data Quality**: Organizational, Architectural, Computational
- **Data Quality Management Phases**: Context reconstruction, Assessment, Improvement
- **Key Dimensions of Data Quality**: Accuracy, Completeness, Consistency, Timeliness

A key message is that data quality is **contextual** — not all data must be cleaned, only that which is needed to answer your specific questions.

---

## 📚 Details

### 🔷 What is Data Quality?

> “Even though quality cannot be defined, you know what it is.” — *Robert Pirsig*

While hard to define universally, **data quality** is best understood as:
> ✅ **Fitness for use** — data is high quality if it enables its intended purpose.

If the data supports your decisions or operations accurately and reliably, it’s considered high quality.

---

### 🔸 Types of Data Errors

1. **Quantitative Errors** (e.g., outliers)
   - Example: Income listed as $99,999,999 for an average citizen.
   - Often caught through statistical analysis (outside this course’s scope).

2. **Qualitative Errors**
   - **Syntactic/Format Errors**: e.g., inconsistent date formats like `01/02/2020` vs `2020-02-01`
   - **Semantic/Schema Errors**: Violations of integrity constraints, e.g., ZIP codes not matching reference data.

This course focuses primarily on **qualitative errors**, particularly in pattern validation and schema conformance.

---

### 🔸 Fitness for Use: A Practical Perspective

You don’t always need perfect data. Instead, ask:
- What questions do I want to answer?
- Do I need this table/column at all?
- Is the data **already good enough**?

**Examples:**
- If analyzing regions, population data might be unnecessary.
- If you're archiving data, don’t alter it — your job is preservation.
- If you're curating data (e.g., in a museum), cleaning is critical for future usability.

🧠 **Minimal information standards** may be used when you don’t yet know the purpose but still need basic data completeness.

---

### 🔸 The 3 Pillars of Data Quality

Defined in *Handbook of Data Quality*, these provide a structured view:

| Pillar            | Description |
|-------------------|-------------|
| **Organizational** | Establishes roles, policies, and goals for ensuring DQ across teams. |
| **Architectural**  | The technology infrastructure used to support data quality processes. |
| **Computational**  | Algorithms, tools, and techniques (e.g., regex, constraints) to enforce DQ. |

📌 **This course focuses heavily on the computational pillar.**

---

### 🔸 Data Quality Management Phases

A lifecycle approach to handling DQ issues:

1. **Context Reconstruction** *(optional)*:
   - Gather background about data usage, origin, and processes.

2. **Assessment / Measurement**:
   - Evaluate data against **reference standards**.
   - Identify the **causes of poor data quality**.

3. **Improvement**:
   - Apply cleaning techniques and tools.
   - Prioritize based on relevance to analysis.

---

### 🔸 Core Dimensions of Data Quality

These dimensions are used universally to evaluate the condition of a dataset:

| Dimension     | Description & Example |
|---------------|------------------------|
| **Accuracy**     | Are values correct and truthful?<br>_e.g., ZIP `ABCDE` is invalid; `02/30/2023` is not a real date_ |
| **Completeness** | Are all required values present?<br>_e.g., Missing country code in a shipping address_ |
| **Consistency**  | Do values follow format/rules?<br>_e.g., All dates follow `YYYY-MM-DD`, primary keys are unique_ |
| **Timeliness**   | Are the values current and valid for your timeframe?<br>_e.g., Census data from 2001 may not be valid for today’s decisions_ |

⏳ **Timeliness** may also be referred to as *currency* or *volatility*, and is especially important for dynamic datasets like weather or finance.

---

### 🧠 Closing Thought

- Don’t assume you need to clean **everything**.
- Focus on what’s essential to your goal.
- Always ask: *Is the data good enough for what I’m trying to do?*

---