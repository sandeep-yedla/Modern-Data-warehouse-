'''
Create a database


run with:
   /opt/spark/bin/spark-submit /mnt/c/repos/dw-spark/spark/python/initialize_db.py

'''

from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import *

#initialize the database
def initialize_db(spark):

    result = spark.catalog.listDatabases()
    df = spark.createDataFrame(result)
    df.select("name").show()
    result = spark.catalog.listTables()
       
    if (result):   
        df = spark.createDataFrame(result)     
        df.select("name").show()
    
    spark.sql("create database if not exists telemetry comment 'telemetry demo by sandeep yedla'")    
    result = spark.catalog.listDatabases()
    df = spark.createDataFrame(result)
    df.select("name").show()


def main():       
    spark = SparkSession.builder.appName("telemetry demo by sandeep yedla").getOrCreate()    
    sc = spark.sparkContext
    sc.setLogLevel("ERROR")  
    initialize_db(spark)
    spark.stop()

#load the script
main()




