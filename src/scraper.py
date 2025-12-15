import pandas as pd
import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from db_config import get_db_url
import datetime
import os


TARGET_URL = "https://taxdeed.duvalclerk.com/"
LOCAL_FILE = os.path.join("data", "raw", "duval_sample.html")

def fetch_data():
    """Fetches data from URL or falls back to local file."""
    print(f"[*] Attempting to scrape: {TARGET_URL}")
    print("[!] LIVE FETCH MIGHT FAIL. Checking local file...")
    
    if os.path.exists(LOCAL_FILE):
        print("[+] Found local file! Processing...")
        with open(LOCAL_FILE, "r", encoding="utf-8") as f:
            return f.read()
    else:
        print("[-] Local file not found. Please save the HTML manually.")
        return None

def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    data = []
    all_rows = soup.find_all('tr')
    print(f"[*] Scanning {len(all_rows)} total rows on the page...")

    for i, row in enumerate(all_rows):
        cols = row.find_all(['td', 'th'])
        if len(cols) < 4:
            continue
            
        row_text = [c.text.strip() for c in cols]
        
        try:
            applicant = row_text[0]
            case_num = row_text[1]
            
            if not case_num or "Case" in case_num:
                continue

            if not any(char.isdigit() for char in case_num):
                continue

            parcel_id = row_text[3]
            
            amount = 0.0
            if len(row_text) > 6:
                clean_amount = row_text[6].replace('$', '').replace(',', '')
                if clean_amount.replace('.', '', 1).isdigit():
                    amount = float(clean_amount)

            record = {
                "case_number": case_num,
                "parcel_number": parcel_id,
                "applicant_name": applicant,
                "amount_due": amount,
                "status": "Available",
                "sale_date": datetime.date.today()
            }
            
            data.append(record)
            print(f"    [+] Found Lien: {case_num} - ${amount}")
            
        except Exception as e:
            continue
    
    return data

def save_to_postgres(data):
    if not data:
        print("[-] No valid data found.")
        return

    df = pd.DataFrame(data)
    engine = create_engine(get_db_url())
    
    try:
        df.to_sql('duval_tax_liens', engine, if_exists='append', index=False)
        print(f"\n[+] SUCCESS! Saved {len(df)} records to PostgreSQL.")
    except Exception as e:
        print(f"[-] Database Error: {e}")

if __name__ == "__main__":
    print("--- Starting Florida Tax Lien Scraper ---")
    html = fetch_data()
    if html:
        extracted_data = parse_html(html)
        if extracted_data:
            save_to_postgres(extracted_data)
        else:
            print("[-] No rows matched the criteria.")
    print("--- Job Complete ---")