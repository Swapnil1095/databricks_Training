# Databricks notebook source
# MAGIC %sql
# MAGIC create schema if not exists formula1
# MAGIC

# COMMAND ----------

from pyspark.sql.functions import *
#df=spark.read.option("header",True).option("inferSchema",True).csv("dbfs:/FileStore/eClerx Input Files/circuits.csv")

#input_path="dbfs:/FileStore/eclerx_input_files/circuits.csv"
#df=spark.read.csv("dbfs:/FileStore/eclerx_input_files/circuits.csv")
#df=spark.read.option("header",True).option("inferSchema",True).csv("dbfs:/FileStore/eclerx_input_files/circuits.csv")
#df=spark.read.csv(input_path,header=True,inferSchema=True)


input_path = "dbfs:/FileStore/eClerx Input Files/circuits.csv"
df=spark.read.csv(input_path,header=True,inferSchema=True)

df= df.withColumnsRenamed({"circuitId":"circuit_id","circuitRef":"circuit_ref"})
df = df.withColumn("Date",current_date())
df = df.drop("url")

final_df = df.write.mode("overwrite").saveAsTable("formula1.circuit1")



# COMMAND ----------

# MAGIC %sql
# MAGIC select * from hive_metastore.formula1.circuit1
# MAGIC
# MAGIC
