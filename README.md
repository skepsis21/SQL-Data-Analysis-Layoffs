# SQL-Data-Analysis-Layoffs
Exploratory Data Analysis (EDA) on global layoff data using MySQL

# Exploratory Data Analysis (SQL)

## 📌 Project Overview
This project focuses on executing a comprehensive Exploratory Data Analysis (EDA) on historical global tech layoff data. Moving beyond basic data retrieval, this project utilizes advanced MySQL techniques to uncover macro-economic trends, sectoral vulnerabilities, and the concentration of economic impact among major industry players.

The primary objective of this repository is to serve as a **Universal EDA Blueprint** that can be systematically adapted to any transactional or volumetric dataset.

---

## 🛠️ Technical Toolkit & SQL Concepts Applied
* **Advanced Aggregations:** Utilizing `GROUP BY` and `HAVING` clauses for data segmentation.
* **Time-Series Analysis:** Extracting chronological trends using date manipulation functions like `YEAR()` and `SUBSTRING()`.
* **Window Functions:** Reconciling cumulative statistics with `SUM() OVER(ORDER BY...)` and sequence logic via `ROW_NUMBER()`.
* **Layered Common Table Expressions (CTEs):** Building multi-stage relational matrices to handle complex analytical pipelines (e.g., dense ranking partitions and concentration metrics).
* **Statistical Modeling:** Implementing the **Pareto Principle (80/20 Rule)** to calculate running percentage distributions on the fly.

---

## 📋 The 10-Stage Analytical Framework
The SQL script (`layoffs_eda.sql`) is engineered into five distinct phases:

1. **Stage 1: The Pulse Check (Descriptive Stats)** - Establishing quantitative extremes and temporal boundaries.
2. **Stage 2: Categorical Driver Aggregation** - Identifying the highest-impact industries and organizations.
3. **Stage 3: Macro-Level Time Series** - Isolating cyclical trends via Year-over-Year (YoY) and monthly bucketing.
4. **Stage 4: Cumulative Trajectory Modeling** - Building a global running total baseline.
5. **Stage 5: Impact Concentration (Pareto Matrix)** - Mathematically isolating the critical few companies driving the absolute majority of global layoff volumes.

---

## 💡 Key Analytical Questions Answered
* What are the upper and lower boundaries of single-event layoffs?
* Which industries proved resilient during the initial waves, and which collapsed under early recessionary pressures?
* Is the macroeconomic damage spread evenly across thousands of smaller tech startups, or is it heavily skewed by massive mega-cap corporations? (Calculated dynamically via the Pareto calculation query).

---

## SQL Exploratory Data Analysis
I performed deep-dive analysis into layoff trends using SQL window functions and CTEs to identify high-impact economic events.

![SQL Pareto Analysis](docs/MySQL_Layoffs.png)


*Template curated for portfolio development and architectural data exploration.*
