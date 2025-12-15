# Florida Tax Lien Scraping System

## 📌 Project Overview
An automated ETL (Extract, Transform, Load) pipeline designed to aggregate "Lands Available" tax deed data from Florida county government sites. This tool helps investors identify potential tax lien opportunities by scraping public records and structuring them into a queryable PostgreSQL database.

**Key Features:**
* **Robust Scraping:** Handles dynamic government websites with a fallback "Local File" mode for reliability.
* **Data Cleaning:** Normalizes currency, removes search widget artifacts, and standardizes dates.
* **SQL Integration:** Automatically persists structured data into PostgreSQL for analysis.

## 🛠 Tech Stack
* **Language:** Python 3.12
* **Database:** PostgreSQL
* **Libraries:** `BeautifulSoup4` (Parsing), `Pandas` (Data Cleaning), `SQLAlchemy` (ORM)

## ⚙️ How It Works
1.  **Extract:** The script connects to the Duval County Clerk of Courts (or loads a local raw HTML snapshot).
2.  **Transform:** It scans the page for valid tax deed rows, filtering out navigation menus and calendar widgets.
3.  **Load:** Valid records are inserted into the `duval_tax_liens` table, skipping duplicates automatically.

## 🚀 Usage
1.  **Setup Database:**
    Run the SQL commands in `src/schema.sql` to create the table.
2.  **Configure:**
    Update `src/db_config.py` with your PostgreSQL credentials.
3.  **Run Pipeline:**
    ```bash
    python src/scraper.py
    ```

## 📊 Sample Data
* **Case:** 2023-0308TD
* **Parcel:** 167449-2090
* **Opening Bid:** $1,131.91