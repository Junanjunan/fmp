CREATE TABLE types (
    id VARCHAR(20) PRIMARY KEY
);

CREATE TABLE exchanges (
    id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE symbols (
    id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    type_id VARCHAR(20),
    exchange_id VARCHAR(20),
    is_existing BOOLEAN DEFAULT TRUE,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (type_id) REFERENCES types(id),
    FOREIGN KEY (exchange_id) REFERENCES exchanges(id)
);