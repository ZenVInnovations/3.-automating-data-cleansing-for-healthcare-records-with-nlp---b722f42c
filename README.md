# Automating-Data-Cleansing-for-Healthcare-Records-with-NLP
This project provides an automated pipeline for cleansing and standardizing healthcare records using Python. It is designed to process healthcare datasets containing patient information, medical conditions, medications, and related data. The script performs data normalization, text cleansing, duplicate detection, and other preprocessing tasks to ensure clean and consistent data for further analysis or machine learning tasks.

**Features
Automated Data Cleaning:
**
Standardizes date formats (e.g., Date of Admission, Discharge Date).
Normalizes categorical fields (e.g., Gender, Admission Type).
Cleans and standardizes free-text fields (e.g., Medical Condition, Medication, Test Results).
**Duplicate Detection:**

Uses fuzzy string matching to identify and flag potential duplicate records based on names or other text fields.
**Error Handling:**

Handles missing, malformed, or inconsistent data formats gracefully.
Ensures that invalid data entries are processed without disrupting the workflow.
**NLP Integration (Optional):**

Uses NLP models (e.g., spaCy) to extract and process medical-related entities (if enabled).
**Customizable Pipeline:**

Easily extend the script for additional data cleansing or preprocessing tasks.
