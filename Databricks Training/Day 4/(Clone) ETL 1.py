# Databricks notebook source
from pyspark.sql.functions import *

# COMMAND ----------

#df=spark.read.option("header",True).option("inferSchema",True).csv("dbfs:/FileStore/eClerx Input Files/circuits.csv")
input_path = "dbfs:/FileStore/eClerx Input Files/circuits.csv"
df=spark.read.csv(input_path,header=True,inferSchema=True)

# COMMAND ----------

#
#input_path="dbfs:/FileStore/eclerx_input_files/circuits.csv"
#df=spark.read.csv("dbfs:/FileStore/eclerx_input_files/circuits.csv")
#df=spark.read.option("header",True).option("inferSchema",True).csv("dbfs:/FileStore/eclerx_input_files/circuits.csv")
#df=spark.read.csv(input_path,header=True,inferSchema=True)

# COMMAND ----------

'''Task: 
    1. rename circuitId-- circuit_id, circuitRef -- circuit_ref
    2. add new column with current_date
    3. drop url col'''
    

# COMMAND ----------

#df.display()
df.withColumnsRenamed({"circuitId":"circuit_id","circuitRef":"circuit_ref"}).display()

# COMMAND ----------

df = df.withColumn("Date",current_date())
df.display()

# COMMAND ----------

df.drop("url").display()

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema if not exists formula1
# MAGIC

# COMMAND ----------

df.write.mode("overwrite").saveAsTable("formula1.circuit")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from hive_metastore.formula1.circuit

# COMMAND ----------


