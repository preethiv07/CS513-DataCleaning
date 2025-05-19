# Lecture: RegExr Demonstration

## ✅ Summary

This session is a practical walkthrough of using the website **RegExr.com** to experiment with and debug regular expressions. The lecture focuses on using **real-world examples** such as ISO-formatted dates and IP addresses to demonstrate regex pattern crafting, refinement, and testing.

Key concepts include:
- Using **RegExr** to explore and visualize regex matches
- Crafting regex patterns for **dates** and **IP addresses**
- Dealing with **false positives** and **false negatives**
- Incrementally **tightening or relaxing** regex for accuracy
- Using **regex syntax** smartly while understanding limitations

---

## 📚 Details

### 🔸 What is RegExr?

[RegExr.com](https://regexr.com) is a **web-based tool** that:
- Lets you write and test regular expressions
- Explains regex syntax on hover
- Highlights matching substrings in real-time
- Helps debug complex patterns by visual feedback

---

### 🔸 Why Regex for Data Cleaning?

- **Date formats** are inconsistent across systems.
- Regex helps **detect and validate** formats like ISO 8601 (`YYYY-MM-DD`).
- For data quality, regex lets you:
  - Detect non-conforming records
  - Enforce structure before transformation
  - Standardize and clean dirty data

---

### 🔸 Example 1: Match Capitalized Words

**Regex**:
```regex
[A-Z]\w+
```

- `[A-Z]` → Match an uppercase letter
- `\w+` → Match one or more word characters
- Matches words like `Apple`, `Regex`, `USA`, but not just `A`

✅ Great for detecting **proper nouns** or **capitalized entries**.

---

### 🔸 Example 2: Match IP Addresses

**Goal**: Match valid IPs like `192.168.0.1`, but not malformed ones like `999.999.999.9999`.

**Initial attempt**:
```regex
\w+\.\w+\.\w+\.\w+
```
❌ Too broad — matches words, not just digits

**Refined version**:
```regex
[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+
```
✅ Matches digit blocks separated by dots

**Better version**:
```regex
\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}
```
- `\d{1,3}` → Match 1 to 3 digits
- `\.` → Literal dot

Still may match invalid IPs like `256.999.1000.5` — semantic validation must be done in code.

---

### 🔸 Example 3: Match ISO 8601 Dates

Target format: `YYYY-MM-DD`

**Regex**:
```regex
\d{4}-\d{2}-\d{2}
```

- `\d{4}` → Year (4 digits)
- `\d{2}` → Month and day (2 digits each)
- `-` → Literal dash

✅ Matches: `2020-03-15`  
❌ False Positive: `2020-04-100`

**Fix**: Add **word boundary** or stricter end marker.

Example tweak:
```regex
\d{4}-\d{2}-\d{2}\b
```

---

### 🔸 Techniques for Improvement

| Issue            | Remedy                          |
|------------------|----------------------------------|
| **False Negative** | Regex is too strict → relax it |
| **False Positive** | Regex is too loose → tighten it |

✅ Use iterative testing in RegExr with positive and negative examples to perfect your pattern.

---

### 🔸 Strategy: Use Regex for Syntax, Code for Semantics

- Regex checks **structure** (e.g., pattern of date)
- Code checks **validity** (e.g., is `02/29/2001` a real date?)

**Why?**
- Regex alone can’t validate semantic logic like leap years, valid IP ranges, etc.

---

### 🔸 Summary Tips

- **Test your regex visually** with tools like RegExr.
- Always test on **positive and negative** examples.
- Remember:
  > 🔧 Regex is best for **matching shapes** — let code handle the meaning.