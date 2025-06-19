# Databricks notebook source
# MAGIC %fs ls
# MAGIC

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

# MAGIC %fs ls dbfs:/FileStore/raw/
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %fs ls dbfs:/FileStore/raw/Book1.csv
# MAGIC

# COMMAND ----------

dbutils.fs.mkdirs("dbfs:/FileStore/eClerx Input Files")

# COMMAND ----------

dbutils.fs.cp("dbfs:/FileStore/raw/Book1.csv","dbfs:/FileStore/eClerx Input Files")

# COMMAND ----------

dbutils.fs.rm("dbfs:/FileStore/raw/Book1.csv")

# COMMAND ----------

dbutils.fs.rm("dbfs:/FileStore/raw/")

# COMMAND ----------


