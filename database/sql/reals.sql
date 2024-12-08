CREATE TABLE types (
    id VARCHAR(20) PRIMARY KEY
);

CREATE TABLE exchanges (
    id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE symbols (
    id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    price DECIMAL(25, 5),
    type_id VARCHAR(20) NOT NULL,
    exchange_id VARCHAR(20),
    is_updated BOOLEAN DEFAULT FALSE,
    is_existing BOOLEAN DEFAULT TRUE,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (type_id) REFERENCES types(id),
    FOREIGN KEY (exchange_id) REFERENCES exchanges(id)
);

CREATE TABLE income_statements (
    symbol VARCHAR(20),
    date TIMESTAMP,
    period VARCHAR(10),
    reported_currency VARCHAR(10),
    cik VARCHAR(20),
    filling_date TIMESTAMP,
    accepted_date TIMESTAMP,
    calendar_year VARCHAR(4),
    revenue BIGINT,
    cost_of_revenue BIGINT,
    gross_profit BIGINT,
    gross_profit_ratio DECIMAL(15, 10),
    research_and_development_expenses BIGINT,
    general_and_administrative_expenses BIGINT,
    selling_and_marketing_expenses BIGINT,
    selling_general_and_administrative_expenses BIGINT,
    other_expenses BIGINT,
    operating_expenses BIGINT,
    cost_and_expenses BIGINT,
    interest_income BIGINT,
    interest_expense BIGINT,
    depreciation_and_amortization BIGINT,
    ebitda BIGINT,
    ebitda_ratio DECIMAL(15, 10),
    operating_income BIGINT,
    operating_income_ratio DECIMAL(15, 10),
    total_other_income_expenses_net BIGINT,
    income_before_tax BIGINT,
    income_before_tax_ratio DECIMAL(15, 10),
    income_tax_expense BIGINT,
    net_income BIGINT,
    net_income_ratio DECIMAL(15, 10),
    eps DECIMAL(15, 4),
    eps_diluted DECIMAL(15, 4),
    weighted_average_shs_out BIGINT,
    weighted_average_shs_out_dil BIGINT,
    link VARCHAR(255),
    final_link VARCHAR(255),
    PRIMARY KEY (symbol, date, period),
    FOREIGN KEY (symbol) REFERENCES symbols(id)
);