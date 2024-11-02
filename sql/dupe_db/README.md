# Design Document

By Andrii Mishchenko

Video overview: https://youtu.be/ZmGrJQbB23Q

## Scope

As the cost of living continues to rise, more cosmetics consumers have been trying to spend less money and are instead choosing 'dupes' – beauty products that emulate more expensive counterparts at a much more affordable price [1].
The objective of the Dupe DB project is to create a Relational Database that will help to organize dupes.


## Functional Requirements

Consumers can search through existing:
- Brands
- Products
- Products' variants
- Product's Dupes

It is out of the scope for the current database design to allow users to create new dupes or update existing one.
Since this is a POC (Proof of Concept) Database created using SQLite, there is no straightforward mechanism to enforce user roles management.

The next step of this project is to migrate to the more robust RDMS, such as PostgreSQL and implement user role rules.

## Representation

### Entities
Each entity is structured with attributes necessary to describe them fully.

#### Brand
`id`: Unique identifier for each brand.
`name`: The brand's name, indexed for faster lookups.
`logo`: Optional URL to the brand's logo.
`created`, `updated`: Timestamps for creation and updates.

#### Product
- `id`: Unique identifier for each product.
- `brand_id`: Foreign key referencing the brand.
- `name`: Product name.
- `product_type`: Type of product (e.g., lipstick, blush).
- `image`: Optional URL to an image of the product.
- `created`, `updated`: Timestamps for tracking changes.

#### ProductVariant
- `id`: Unique identifier for each product variant.
- `product_id`: Foreign key referencing the product.
- `name`: Name of the variant (e.g., shade name).
- `image`: Optional URL for the variant's image.

#### EquivClass
- `id`: Unique identifier for each equivalence class.

#### ProductVariantEquiv
- `id`: Unique identifier.
- `product_variant_id`: Foreign key linking to a product variant.
- `equiv_class_id`: Foreign key linking to an equivalence class.
- `created`: Timestamp to track when the relationship was created.

#### Attribute
- `id`: Unique identifier for each attribute.
- `name`: Name of the attribute (e.g., tone, texture).
- `created`, `updated`: Timestamps for tracking attribute changes.

#### AttributeValue
- `id`: Unique identifier.
- `attribute_id`: Foreign key referencing the attribute.
- `value`: Specific value for the attribute (e.g., “red” for tone).
- `created`, updated: Timestamps for tracking attribute value changes.

#### ProductAttributeValue
- `id`: Unique identifier.
- `product_id`: Foreign key linking to a product.
- `attribute_value_id`: Foreign key linking to a specific attribute value.

#### Chosen types

- `INTEGER` for `ID`s: Using integer-based `ID`s as primary keys allows for efficient indexing and joins.
- `TEXT` for names and descriptions: Product names, brand names, and attribute values are best represented as text since they are inherently string-based.
- `FOREIGN KEYS` for relationships: Foreign keys establish relationships between entities, maintaining referential integrity in the database.
- `TIMESTAMP` for dates: created and updated attributes use timestamp data types to store precise creation and modification times.
- `ENUM` representation for ProductTypes and Attributes: Since these are categorical values with a limited set of choices, using enums (or a lookup table for enum values in SQL) keeps the data consistent.

The constraints help maintain database in as normilized form as possible and improve performance.

- Primary Keys: Unique identifiers for each record, ensuring each entry is distinct and allowing for efficient access and updates.
- Unique Constraints: Ensuring unique values for attributes like name in Brand prevents data duplication.
- Foreign Keys: Establishing dependencies between tables to ensure referential integrity, making sure that linked entries (e.g., products to brands) exist.
- Not Null: Ensuring essential fields like product.name and app_user.email are always populated for data consistency.
- Indexes: Adding indexes on frequently queried columns such as name in `Product` speeds up query performance.

### Relationships

- `Brand`. Brand represents, well, brands, e. g. Avon, Nivea, Loreal and etc.
- Each `Brand` can have one or more `Product`(s). For example, Nivea has a Lipstick with commercial name “Lip Care”. So this would be a single entry in the `Product` table.
- On the other hand, each `Product` has its Variants. Back to the Nivea’s “Lip Care” lipstick. It has a set of flavours: Strawberry Lip Care, Vanilla Buttercream Lip Care, Blackberry Lip Care, etc. The variants will be stored in `Product Variant` table.
- Each `Product` can have some set of properties that are complementary to the `Product Variant`. For example: Mineral oil free, Tinted or not to name a few. To represent this relation between `Product` and its `Attribute` we will create a couple of tables:
    * `Attribute` table - will store the attribute name, e. g. `TONE`, `TEXTURED` etc.
    * `Attribute Value` - That will map the `Attribute` name to its value: `TONE -> Red` for example
    * `Product Attribute Value` - will link each `Attribute` and Attribute Value value with a given Product

To link the `Products` and `Product Variant`s, we are going to use an approach similar to one described by Deron Meranda [3] back in 2008.
It resumes in creating 2 tables:
- `Equivalence Class` - this table will hold a unique identifier for the `Equivalence Class`. `The Equivalence Class` is just an arbitrary unique value that serves as an umbrella to a set of products that are named as Dupes.
`Product Variant Equivalence` - Relate one `Product Variant` to other `Product Variants` by the means of `Equivalence Class` to form a 'dupe'

Here is the ER diagram

![ER Diagram](https://i.ibb.co/MNLQXWj/cluster-nude-dupes-public.png)

## Optimizations

### Indexes
- Primary Keys: Every table has a primary key index by default (on id columns), which optimizes access to rows by their unique identifier and ensures each row is uniquely identifiable.

#### Indexes on Frequently Queried Columns

- `brand.name`, `product.name`: Since brand and product names are likely used in searches and product listings, these are indexed for faster retrieval.
- `product.product_type`: Filtering by product type (e.g., lipstick, blush) is common in product catalogs, so indexing helps here.
`product_variant.name`: Product variants like tones or shades will often be searched or filtered, so this index helps speed up those queries.
`attribute_value.value`: Attributes such as color or texture may be frequently filtered, especially in a search or product filter, so this index supports those queries.

#### Foreign Key Indexes

Foreign key columns such as `brand_id` in `product`, `product_id` in `product_variant`, and `attribute_id` in `attribute_value` are indexed. This optimization is important for join operations, which are common when querying related data across tables.
`product_variant_id` and `equiv_class_id` in `zproduct_variant_equiv`: Since equivalence relationships (like "dupes") may involve joining tables on these keys, indexing these columns supports efficient join operations.

## Limitations

In this section you should answer the following questions:

### Limited Support for Complex Relationships
- Equivalence Classes for Product Variants: The EquivClass and ProductVariantEquiv tables are designed to group similar products, such as "dupes" or alternatives, but the structure may not fully capture complex relationships between products. For example, if products need to have multi-level similarity (e.g., close dupes vs. distant alternatives), this single level of equivalence might be too simplistic.
- Multiple Attributes per Product: The design can represent multiple attributes for products (like tone, texture, etc.), but adding new attribute types dynamically (outside of the defined choices) could be challenging. Changing the list of attributes in the enum choices or adding new types might require schema changes, which could be cumbersome in a growing product catalog.

## References
1. https://www.cosmeticsdesign-europe.com/Article/2024/09/18/10-beauty-dupes-to-know-about#:~:text=As%20the%20cost%20of%20living,a%20much%20more%20affordable%20price
2. https://skinsort.com/dupes
3. https://forums.mysql.com/read.php?125,206642
