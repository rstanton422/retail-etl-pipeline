# Automated ETL Pipeline for Retail Sales

## Overview
An automated data engineering pipeline that extracts raw, messy sales data, cleans and transforms it using Pandas, and loads it into a SQLite database for reporting. This project simulates a real-world scenario of processing "dirty" data from legacy systems.

## Tech Stack
* **Python 3.10**
* **Pandas:** For data transformation and cleaning.
* **SQLite:** For persistent data storage.
* **SQLAlchemy/SQL:** For querying and reporting.

## Pipeline Steps
1.  **Extraction:** Ingests raw CSV data containing duplicates, nulls, and formatting errors.
2.  **Transformation:**
    * **Deduplication:** Identifies and removes duplicate transactions based on Order ID.
    * **Imputation:** Fills missing price data using the median price of the specific product category.
    * **Normalization:** Converts mixed date formats (MM/DD/YYYY & YYYY-MM-DD) into a standard SQL-compatible ISO format.
    * **Sanitization:** Corrects negative values caused by data entry errors.
3.  **Loading:** Upserts clean data into a persistent SQLite database (`sales_data.db`).
4.  **Reporting:** Executes SQL queries to generate an executive summary of top-performing products.

## How to Run
1.  Generate the chaos: `python generate_messy_data.py`
2.  Run the pipeline: `python etl_pipeline.py`
3.  View the "CEO Report" in the terminal output.
