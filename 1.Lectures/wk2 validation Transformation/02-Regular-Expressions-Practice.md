# Lecture: Regular Expressions – Practice

## ✅ Summary

This lecture shifts focus from theory to the **practical application of regular expressions (regex)**. It shows how regex can be used to match, extract, and transform text patterns — especially useful in data cleaning workflows.

Key points include:
- Anatomy of a regex for floating-point numbers.
- Core regex constructs: character sets, quantifiers, anchors, groups, and escape characters.
- Issues of **false positives** and **false negatives**, and how to adjust regex accordingly.
- Strategy: **Use regex for syntax checks, and code for semantics**.
- Practical tools: regex groups, transformations, and backreferences (e.g., changing date formats).

---

## 📚 Details

### 🔸 Use Case: Floating-Point Numbers

Extracting values like:
```text
pi = -0.314159265e+1
e  =  0.2718281828E+1
```

**Regex Used**:
```regex
[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?
```

### Explanation:

| Part                   | Meaning |
|------------------------|---------|
| `[-+]?`                | Optional sign (either `-` or `+`) |
| `[0-9]*`               | Any number of digits (including none) |
| `\.`                  | Literal dot (escaped) |
| `[0-9]+`               | At least one digit after the decimal |
| `([eE][-+]?[0-9]+)?`   | Optional scientific notation component |

---

### 🔸 Key Regex Constructs

| Construct       | Description |
|------------------|-------------|
| `[abc]`          | Match one of `a`, `b`, or `c` |
| `[^abc]`         | Match any character **except** `a`, `b`, or `c` |
| `[0-9]` or `\d`  | Match a digit |
| `*`              | Zero or more |
| `+`              | One or more |
| `?`              | Zero or one (optional) |
| `.`              | Any character (except newline) |
| `\.`             | Escape dot to match it literally |
| `()`             | Grouping |
| `\1`, `\2`       | Backreferences to captured groups |
| `^`, `$`         | Anchors: start and end of line |
| `\b`, `\B`       | Word boundary / non-boundary |

---

### 🔸 Common Regex Pitfalls

| Type            | Description |
|------------------|-------------|
| **False Negative** | Regex **fails to match** valid patterns → too strict |
| **False Positive** | Regex **matches invalid** data → too loose |

💡 **Fix**:
- **Relax** the regex to fix false negatives.
- **Tighten** the regex to fix false positives.

---

### 🔸 Regex Golf

- Concept from [XKCD 1313](https://xkcd.com/1313/)
- The "sport" of crafting the **shortest regex** to match only what you want.
- Often not practical — leads to unmaintainable, brittle expressions.

---

### 🔸 Practical Advice: Syntax vs Semantics

> 🔧 **Use regex for pattern structure (syntax). Use code for deeper logic (semantics).**

**Example**: 
- Matching `02/29/2000` is easy with regex.
- But checking whether it’s a valid **leap year** date? → better done in code.

```python
# Leap year logic
if year % 4 != 0:
    common_year
elif year % 100 != 0:
    leap_year
elif year % 400 != 0:
    common_year
else:
    leap_year
```

---

### 🔸 Groups and Backreferences

**Grouping**:
```regex
([0-9]+)\s*([a-z]+)
```
- Group 1: number  
- Group 2: word  
- `\1`, `\2` allow you to **reuse matched content**

---

### 🔸 Transforming Date Formats with Groups

**From**: `MM/DD/YYYY`  
**To**: `YYYY-MM-DD`

**Regex**:
```regex
(\d{2})/(\d{2})/(\d{4})
```

**Replacement**:
```text
$3-$1-$2
```

✅ This pattern is often used in **Python, OpenRefine, or scripting workflows**.

---

### 🔸 Escaped and Special Characters

| Escape Sequence | Matches                  |
|-----------------|--------------------------|
| `\.`            | Literal dot              |
| `\\`           | Backslash                |
| `\t`            | Tab                      |
| `\n`            | Newline                  |
| `\r`            | Carriage return          |
| `\u00A9`        | Unicode ©                |

---

### 🔸 Summary

- Regex is a powerful pattern matching tool rooted in formal language theory.
- Essential for:
  - **Data extraction**
  - **Validation**
  - **Transformation**
- Best used in combination with **code-based logic** for complete accuracy.
- Regex may take time to learn but offers **"superpowers"** for any data scientist.

> 🧠 Like chess, once you learn it, you see patterns everywhere — but it takes practice.