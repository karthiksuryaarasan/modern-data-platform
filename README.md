Modern Data Platform – End-to-End Analytics Engineering Project
🚀 Overview

This project simulates a production-grade modern data platform for an ecommerce system. It demonstrates how raw transactional data flows through ingestion, warehouse modeling, and analytics layers using industry-standard tools and best practices.

The architecture follows a layered approach:

Raw → Staging → Mart (Star Schema)

🏗 Architecture

Data Generation (Python)

Simulated users, products, and orders data

Time-distributed transactional records

Structured raw data zone

Warehouse Layer (DuckDB)

Raw schema separation (raw_layer)

Idempotent loading logic

Schema isolation for maintainability

Transformation Layer (dbt)

Staging models (views)

Dimension tables (materialized tables)

Incremental fact table (watermark-based logic)

SCD Type 2 implementation for user dimension

Relationship & integrity tests

Data Quality & Governance

Primary key validation

Foreign key relationship tests

Null checks

Model-level documentation

Lineage graph generation

⭐ Key Engineering Concepts Implemented

Incremental fact table using is_incremental() logic

Merge-based modeling with unique keys

Slowly Changing Dimension (Type 2)

Schema-based separation (raw vs analytics)

Inter-model dependency management using ref()

Data quality enforcement using dbt tests

Production-style materialization strategy

🛠 Tech Stack

Python 3.11

DuckDB

dbt-core

dbt-duckdb

YAML

Docker-ready structure

📊 Models Built

stg_users

stg_products

stg_orders

dim_users (SCD Type 2)

dim_products

fact_orders (Incremental)

▶️ How to Run
python ingestion/generate_data.py
python ingestion/load_to_duckdb.py

cd ecommerce_dbt
dbt run
dbt test
dbt docs generate
dbt docs serve
📈 Why This Project Matters

This repository demonstrates:

Practical understanding of data warehousing principles

dbt-based transformation workflows

Scalable modeling patterns

Data reliability and integrity enforcement

Production-aware architecture design

Designed with production scalability in mind and adaptable to cloud warehouses such as Snowflake, BigQuery, or Redshift.
