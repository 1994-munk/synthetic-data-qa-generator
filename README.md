# Synthetic Data Quality & Edge-Case Generator

A data quality testing utility designed to generate baseline datasets and intentionally inject malformed payloads, missing parameters, and boundary-breaking edge cases to stress-test ETL and API validation layers.

## Features
- **Baseline Generator:** Creates clean, structured JSON data records.
- **Edge-Case Mutation:** Dynamically introduces data corruption (null values, type mismatches, truncated JSON strings) for rigorous QA testing.
- **Resilience Testing:** Validates that downstream ingestion layers catch and handle corrupt payloads gracefully.

## Quick Start
```bash
python data_generator.py
