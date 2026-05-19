-- Exploratory Data Analysis

-- 1. View a sample
SELECT *
FROM layoffs_staging LIMIT 10;

-- 2. Find the absolute extremes (Max/Min values)
SELECT 
    MAX(total_laid_off) AS max_single_event, 
    MIN(total_laid_off) AS min_single_event,
    AVG(total_laid_off) AS avg_layoff_size
FROM layoffs_staging;

-- 3. Find Date Range
SELECT 
    MIN(`date`) AS data_start_date, 
    MAX(`date`) AS data_end_date,
    DATEDIFF(MAX(`date`), MIN(`date`)) AS total_time_span
FROM layoffs_staging;

-- 4. Ranking Categories by Volume
SELECT 
    industry, 
    SUM(total_laid_off) AS total_volume,
    COUNT(company) AS total_events,
    ROUND(AVG(total_laid_off), 0) AS avg_per_event
FROM layoffs_staging
WHERE total_laid_off IS NOT NULL
GROUP BY industry
ORDER BY total_volume DESC;

-- 5. TOP 10 entities by impact
SELECT 
    company, 
    SUM(total_laid_off) AS grand_total
FROM layoffs_staging
GROUP BY company
HAVING grand_total IS NOT NULL
ORDER BY grand_total DESC
LIMIT 10;

-- 6. Year Over Year Trends
SELECT 
    YEAR(`date`) AS financial_year, 
    SUM(total_laid_off) AS yearly_total,
    COUNT(company) AS companies_affected
FROM layoffs_staging
WHERE `date` IS NOT NULL
GROUP BY YEAR(`date`)
ORDER BY financial_year ASC;

-- 7. Month By Month
SELECT 
    SUBSTRING(`date`, 1, 7) AS `month_bucket`, 
    SUM(total_laid_off) AS monthly_total
FROM layoffs_staging
WHERE `date` IS NOT NULL
GROUP BY `month_bucket`
ORDER BY `month_bucket` ASC;

-- 8. Rolling Running Totals
WITH Monthly_Aggregates AS (
    SELECT 
        SUBSTRING(`date`, 1, 7) AS `month_bucket`, 
        SUM(total_laid_off) AS monthly_volume
    FROM layoffs_staging
    WHERE `date` IS NOT NULL AND total_laid_off IS NOT NULL
    GROUP BY `month_bucket`
)
SELECT 
    `month_bucket`, 
    monthly_volume, 
    SUM(monthly_volume) OVER(ORDER BY `month_bucket`) AS cumulative_running_total
FROM Monthly_Aggregates
ORDER BY `month_bucket` ASC;


-- 9. Find out which company has highest number of layoffs in each year using CTE

WITH Consolidated_Yearly_Totals AS (
    SELECT 
        company, 
        YEAR(`date`) AS layoff_year, 
        SUM(total_laid_off) AS total_volume
    FROM layoffs_staging
    WHERE `date` IS NOT NULL AND total_laid_off IS NOT NULL
    GROUP BY company, YEAR(`date`) -- FIXED: Grouped by Year expression, not the exact raw date
), 
Ranked_Entities AS (
    SELECT 
        company, 
        layoff_year, 
        total_volume, 
        DENSE_RANK() OVER(PARTITION BY layoff_year ORDER BY total_volume DESC) AS internal_rank
    FROM Consolidated_Yearly_Totals
)
SELECT *
FROM Ranked_Entities
WHERE internal_rank <= 5
ORDER BY layoff_year DESC, internal_rank ASC;

-- 10. Identify the critical few entities driving the majority of global impact
WITH Entity_Contributions AS (
    SELECT 
        company,
        SUM(total_laid_off) AS total_volume
    FROM layoffs_staging
    WHERE total_laid_off IS NOT NULL
    GROUP BY company
),
Running_Impact AS (
    SELECT 
        company,
        total_volume,
        -- Running total of volume as we move down the list
        SUM(total_volume) OVER(ORDER BY total_volume DESC) AS cumulative_volume,
        -- Total sum of EVERY layout event in the whole database
        SUM(total_volume) OVER() AS grand_total_volume
    FROM Entity_Contributions
),
Pareto_Calculation AS (
    SELECT 
        company,
        total_volume,
        cumulative_volume,
        grand_total_volume,
        -- Calculate what % of the entire economic downturn this single company + those above it represent
        ROUND((cumulative_volume / grand_total_volume) * 100, 2) AS cumulative_percentage_share,
        -- Generate a running row index to see how many companies we've counted
        ROW_NUMBER() OVER(ORDER BY total_volume DESC) AS company_rank,
        -- Total number of unique companies in the dataset
        COUNT(*) OVER() AS total_unique_companies
    FROM Running_Impact
)
SELECT 
    company,
    total_volume,
    cumulative_percentage_share,
    CONCAT(company_rank, ' out of ', total_unique_companies) AS concentration_index,
    ROUND((company_rank / total_unique_companies) * 100, 2) AS percent_of_total_companies_pool
FROM Pareto_Calculation
-- Tip: Change this threshold (e.g., <= 80.00) to see exactly which companies make up the top 80% of damage
WHERE cumulative_percentage_share <= 50.00
ORDER BY total_volume DESC;
