import pandas as pd
import sqlite3
import os

def setup_database(csv_path, db_name):
    """
    Ingests raw CSV data into a SQLite database.
    """
    if not os.path.exists(csv_path):
        print(f"Error: The file {csv_path} was not found.")
        return

    print("Loading data from CSV...")
    df = pd.read_csv(csv_path)

    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)
    
    # 4. Write data to the table
    # Using 'layoffs_staging' to match your SQL analysis scripts
    table_name = "layoffs_staging"
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    
    print(f"Successfully loaded {len(df)} rows into the '{table_name}' table.")

    # 5. Verify and Close
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cursor.fetchone()[0]
    print(f"Verification: Found {count} rows in the database.")
    
    conn.close()

if __name__ == "__main__":
    # Define paths
    CSV_FILE = 'Data/layoffs.csv'
    DB_FILE = 'layoffs.db'
    
    setup_database(CSV_FILE, DB_FILE)