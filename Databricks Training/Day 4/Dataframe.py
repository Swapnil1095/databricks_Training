# Databricks notebook source
spark


# COMMAND ----------

user_data = ([(1,'Swap'),(2,'nil')])
user_schema = "id int, name string"


# COMMAND ----------

df = spark.createDataFrame(user_data,user_schema)

# COMMAND ----------

df.show()


# COMMAND ----------


df.display()

# COMMAND ----------

df.select("*").display()


# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

df.select(col("id").alias("emp_id")).display()

# COMMAND ----------

df.display()

# COMMAND ----------

df.withColumnsRenamed({"id":"Emp_id","name":"Emp_name"}).display()

# COMMAND ----------

df2=df.withColumn("ingestion date",current_date())  


# COMMAND ----------

df2.display()

# COMMAND ----------


