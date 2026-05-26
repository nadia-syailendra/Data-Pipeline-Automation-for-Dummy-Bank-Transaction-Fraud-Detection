'''
=================================================
Milestone 3

Nama  : Nadia Syailendra
Batch : CODA-016-RMT

Program ini dibuat untuk menjalankan automasi data pipeline untuk tahap load dataset yang sudah
di transform ke dalam Mongo DB dalam proses ETL.
=================================================
'''

#Import Mongo and Spark to load transformed dataset to Mongo
from pymongo import MongoClient
from pyspark.sql import SparkSession
spark = SparkSession.builder \
.appName("LoadMongoDB") \
.getOrCreate()

#Connect to Mongo
client = MongoClient("yourmongoclienthere")

#Create DB and collection to insert dataset
db_client = client['Banking']
collection = db_client['Transaction']

#Read transformed dataset
data = spark.read.csv('/opt/airflow/data/transformed_data', header=True, inferSchema=True)

#Create document list to convert 1000 rows to Mongo as dictionary
document_list = [row.asDict() for row in data.limit(1000).collect()]

#Insert document list to Mongo
if document_list:
    collection.insert_many(document_list)
    print("Sakses.")
else:
    print("Error.")

# Stop Spark
spark.stop()
print("Load complete")