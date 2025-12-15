-- DROP TABLE IF EXISTS duval_tax_liens;

-- CREATE TABLE duval_tax_liens (
--     id SERIAL PRIMARY KEY,
--     case_number VARCHAR(50) UNIQUE NOT NULL,
--     parcel_number VARCHAR(50),
--     applicant_name VARCHAR(255),
--     amount_due DECIMAL(10, 2), 
--     status VARCHAR(50),
--     sale_date DATE,
--     scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

-- CREATE INDEX idx_parcel ON duval_tax_liens(parcel_number);

DELETE FROM duval_tax_liens WHERE LENGTH(case_number) < 5;
SELECT * FROM duval_tax_liens;