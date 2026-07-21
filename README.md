# Data Pipeline Automation - Bank Transaction  
>> **Portfolio Project** : Developed an automated data pipeline project for bank transaction fraud detection using dummy transaction dataset

## 🔗 About Dataset

📎Raw data source: [Kaggle Dataset](https://www.kaggle.com/datasets/marusagar/bank-transaction-fraud-detection)


## 🛠️ Tech Stack

Data Cleaning: Python (Pandas)
Data Validation: Great Expectatoion
ETL: PySpark, MongoDB
Orchestration: Airflow


## 📌 Business Context

With increasingly more online transactions and digital banking activities, fraudulent transactions have end up a good sized danger to both the financial institution and its customers.

To cope with this developing subject, Bank LOL wants to provide additional data that labels whether the transaction has indication of fraud or not.

## 👩‍💻 Workflow

**(1) Pre-Automation:** Data Cleaning & Validation

Data Cleaning:
- Removed missing values found
- Removed data duplicates
- Converted date column to `datetime` format

Data validation rules:
1. Transaction_ID must be unique
2. Age column value to be between 18 and 100
3. Account_Type contains  'Savings', 'Business', 'Checking'
4. Transaction_Amount to be in form of float
5. Transaction_Currency must contain 3 digit
6. Customer_Email to match regex contains [emailname@domain.ext]
7. Customer_Name column value  length be between 2 to 40 characters

**(2) Automation:** ETL & workflow orchestration

The ETL process is done using PySpark.

1. **Extract:** Data extraction with Kagglehub to download dataset from Kaggle and store into the project's root directory.

2. **Transform:** Reused Phase 1 cleaning code and adjusted it to PySpark

3. **Load:** Established a database connection with MongoDB and inserted the documents into the MongoDB collection.

Orchestration is done using Airflow.

4. **Orchestration:** Implemented workflow orchestration using to automate and schedule the ETL pipeline.


## Conclusion

Data Validation: Explored, cleaned and validated the dataset using Pandas and Great Expectations

ETL: Extracted, transformed and loaded the cleaned dataset using Kaggle hub, Apache Spark and MongoDB

Workflow Orchestration: Automated and scheduled ETL pipeline using Apache Airflow.