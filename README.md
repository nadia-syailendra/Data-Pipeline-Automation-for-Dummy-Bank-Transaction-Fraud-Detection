# Data Pipeline Automation - Bank Transaction Fraud Detection - Dummy Data

## Links

[Datasouce](https://www.kaggle.com/datasets/marusagar/bank-transaction-fraud-detection)


## Overview

In this project, I developed an automated data pipeline project for bank transaction fraud detection using dummy transaction data from Bank LOL. The project aimed to support banking security processes by automatically identifying and labeling potential fraudulent transactions through a scheduled ETL workflow.

## Background

With increasingly more online transactions and digital banking activities, fraudulent transactions have end up a good sized danger to both the financial institution and its customers.

To cope with this developing subject, Bank LOL wants to provide additional data that labels whether the transaction has indication of fraud or not.

## Workflow

1. Data Validation
2. ETL
3. Workflow Orchestration

### Data Validation

---

Data validation is performed using Great Expectations.

My expectations:
1. Transaction_ID must be unique
2. Age column value to be between 18 and 100
3. Account_Type contains  'Savings', 'Business', 'Checking'
4. Transaction_Amount to be in form of float
5. Transaction_Currency must contain 3 digit
6. Customer_Email to match regex contains [emailname@domain.ext]
7. Customer_Name column value  length be between 2 to 40 characters

All the expectations in the dataset has been validated successfully.

### ETL

---

The ETL process is done using PySpark.

1. Extract

I used Kagglehub to download dataset from Kaggle and store into the project's root directory.

2. Transform

I performed data cleaning and checked for missing values, data duplicates and inconsistent data types. In this process, I converted data type where necessary and saved the cleaned data into the project's root directory.

3. Load

To store the data into the database,  I established a database connection with MongoDB. I created the database and collection, converted the dataset into a list dictionaries, and inserted the documents into the MongoDB collection.

### Workflow Orchestration

---

Implemented workflow orchestration using Apache Airflow to automate and scheduled the ETL pipeline.


## Conclusion

Data Validation: Explored, cleaned and validated the dataset using Pandas and Great Expectations

ETL: Extracted, transformed and loaded the cleaned dataset using Kaggle hub, Apache Spark and MongoDB

Workflow Orchestration: Automated and scheduled ETL pipeline using Apache Airflow.