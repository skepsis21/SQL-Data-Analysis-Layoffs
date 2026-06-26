import pandas as pd
import sqlite3
import os

def setup_database(csv_path, db_name):
    """
    Ingests raw CSV data into a SQLite database.
    """
    # 1. Ensure the data directory exists (good practice)
    if not os.path.exists(csv_path):
        print(f"Error: The file {csv_path} was not found.")
        return

    # 2. Load the data
    print("Loading data from CSV...")
    df = pd.read_csv(csv_path)

    # 3. Create/Connect to the SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # 4. Write data to the table
    # 'replace' ensures that every time you run this, you get a fresh database
    table_name = "layoffs"
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    
    print(f"Successfully loaded {len(df)} rows into the '{table_name}' table in {db_name}.")

    # 5. Close connection
    conn.close()

if __name__ == "__main__":
    # Define paths
    CSV_FILE = 'Data/layoffs.csv'
    DB_FILE = 'layoffs.db'
    
    setup_database(CSV_FILE, DB_FILE)