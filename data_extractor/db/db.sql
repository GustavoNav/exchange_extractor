CREATE TABLE tb_historic (
    id SERIAL PRIMARY KEY,
    date_information TIMESTAMP WITH TIME ZONE,
    open NUMERIC(14, 6),
    high NUMERIC(14, 6),
    low NUMERIC(14, 6),
    close NUMERIC(14, 6),
    volume BIGINT,
    dividends NUMERIC(14, 6),
    stock_splits NUMERIC(14, 6),
    company_code VARCHAR(10),
    CONSTRAINT unique_historic UNIQUE (date_information, open, high, low, close, volume, dividends, stock_splits, company_code)
);

CREATE TABLE tb_general_financials (
    id SERIAL PRIMARY KEY,
    company_code VARCHAR(10) NOT NULL,
    sector VARCHAR(50),
    net_sales NUMERIC(15, 2),
    net_income NUMERIC(15, 2),
    net_margin NUMERIC(5, 2),
    ebitda NUMERIC(15, 2),
    ebitda_margin NUMERIC(5, 2),
    total_assets NUMERIC(15, 2),
    gross_debt NUMERIC(15, 2),
    equity NUMERIC(15, 2),
    pe_ratio NUMERIC(5, 2),
    CONSTRAINT unique_company_code UNIQUE (company_code)
);

CREATE TABLE tb_real_time(
	id SERIAL PRIMARY KEY,
	company_code VARCHAR(10) NOT NULL,
	date_information TIMESTAMP,
    open NUMERIC(14, 6),
    high NUMERIC(14, 6),
    low NUMERIC(14, 6),
	close NUMERIC(14, 6),
	CONSTRAINT unique_real_time UNIQUE (company_code, date_information, open, high, low, close)
);