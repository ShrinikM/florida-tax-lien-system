DB_SETTINGS = {
    "dbname": "tax_liens",  
    "user": "postgres",
    "password": "smadise2",
    "host": "localhost",
    "port": "5432"
}

def get_db_url():
    # This creates the link format that Python needs to connect
    return f"postgresql://{DB_SETTINGS['user']}:{DB_SETTINGS['password']}@{DB_SETTINGS['host']}:{DB_SETTINGS['port']}/{DB_SETTINGS['dbname']}"