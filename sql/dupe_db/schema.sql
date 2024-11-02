CREATE TABLE ProductTypes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    value TEXT NOT NULL
);

INSERT INTO ProductTypes (value) VALUES
    ('BATOM'),
    ('BLUSH'),
    ('CORRETIVO'),
    ('LAPIS'),
    ('CONTORNO'),
    ('MULTIFUNCIONAL');

CREATE TABLE Attributes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    value TEXT NOT NULL
);

INSERT INTO Attributes (value) VALUES
    ('TONALIDADE'),
    ('TEXTURA'),
    ('ACABAMENTO'),
    ('COBERTURA'),
    ('VOLUME'),
    ('PESO');

CREATE TABLE brand (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    logo TEXT,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated TIMESTAMP
);

CREATE INDEX idx_brand_name ON brand(name);

CREATE TABLE product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brand_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    product_type INTEGER NOT NULL REFERENCES ProductTypes(id),
    image TEXT,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated TIMESTAMP,
    FOREIGN KEY (brand_id) REFERENCES brand(id)
);

CREATE INDEX idx_product_name ON product(name);
CREATE INDEX idx_product_brand_id ON product(brand_id);
CREATE INDEX idx_product_product_type ON product(product_type);

CREATE TABLE product_variant (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    image TEXT,
    FOREIGN KEY (product_id) REFERENCES product(id)
);

CREATE INDEX idx_product_variant_product_id ON product_variant(product_id);
CREATE INDEX idx_product_variant_name ON product_variant(name);

CREATE TABLE equiv_class (
    id INTEGER PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE product_variant_equiv (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_variant_id INTEGER NOT NULL,
    equiv_class_id INTEGER NOT NULL,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_variant_id) REFERENCES product_variant(id),
    FOREIGN KEY (equiv_class_id) REFERENCES equiv_class(id)
);

CREATE INDEX idx_product_variant_equiv_product_variant_id ON product_variant_equiv(product_variant_id);
CREATE INDEX idx_product_variant_equiv_equiv_class_id ON product_variant_equiv(equiv_class_id);

CREATE TABLE attribute (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name INTEGER NOT NULL REFERENCES Attributes(id),
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated TIMESTAMP
);

CREATE INDEX idx_attribute_name ON attribute(name);

CREATE TABLE attribute_value (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    attribute_id INTEGER NOT NULL,
    value TEXT NOT NULL,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated TIMESTAMP,
    FOREIGN KEY (attribute_id) REFERENCES attribute(id)
);

CREATE INDEX idx_attribute_value_attribute_id ON attribute_value(attribute_id);
CREATE INDEX idx_attribute_value_value ON attribute_value(value);

CREATE TABLE product_attribute_value (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    attribute_value_id INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES product(id),
    FOREIGN KEY (attribute_value_id) REFERENCES attribute_value(id)
);

CREATE INDEX idx_product_attribute_value_product_id ON product_attribute_value(product_id);
CREATE INDEX idx_product_attribute_value_attribute_value_id ON product_attribute_value(attribute_value_id);
