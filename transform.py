'''
=================================================
Milestone 3

Nama  : Nadia Syailendra
Batch : CODA-016-RMT

Program ini dibuat untuk menjalankan automasi data pipeline untuk tahap transform 
untuk melakukan data cleaning menggunakan Spark dalam proses ETL.
=================================================
'''

#Import Spark for transform data
from pyspark.sql import SparkSession
spark = SparkSession.builder \
.appName("transformrawdata") \
.getOrCreate()

#Read csv to spark dataframe
data = spark.read.csv('/opt/airflow/data/Bank_Transaction_Fraud_Detection.csv', header=True, inferSchema=True)

#Check for missing values
from pyspark.sql.functions import col, count, when, isnull
data.select([count(when(isnull(c),c)).alias(c) for c in data.columns]).show() #Result: There are no missing values

#Drop data duplicates
data = data.dropDuplicates()

#Change data type from double to float for Transaction_Amount & Account_Balance
data = data.withColumn("Transaction_Amount", col("Transaction_Amount").cast("float"))
data = data.withColumn("Account_Balance", col("Account_Balance").cast("float"))

#Validate changes in transformed dataset
data.printSchema() #Result: Data type for Transaction_Amount & Account_Balance are float

#Save transformed dataset
data.write.csv('/opt/airflow/data/transformed_data', header=True, mode="overwrite")
print("Transform complete")