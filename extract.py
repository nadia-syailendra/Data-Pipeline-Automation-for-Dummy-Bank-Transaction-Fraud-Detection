'''
=================================================
Milestone 3

Nama  : Nadia Syailendra
Batch : CODA-016-RMT

Program ini dibuat untuk menjalankan automasi data pipeline untuk tahap extract dari datasource
dalam proses ETL.
=================================================
'''

#Import Kagglehub and os
import kagglehub
import os

#Create root folder 
DATASET_ROOT_DIR = "/opt/airflow/data/"

#Download raw data to kaggle cache
path = kagglehub.dataset_download("marusagar/bank-transaction-fraud-detection")
print("Path to dataset files:", path)

#Save downloaded raw data from cache to root folder
if not os.path.exists(DATASET_ROOT_DIR):
    os.makedirs(DATASET_ROOT_DIR)
os.system("cp -r {}/* {}".format(path, DATASET_ROOT_DIR))
print("Path to dataset files:", path)
print("Extract complete")