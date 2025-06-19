# Databricks notebook source
print("Hello World!")

# COMMAND ----------

# MAGIC %sql
# MAGIC Create Table Employee1 (ename varchar(20), company varchar(20), eposition varchar(20))

# COMMAND ----------

# MAGIC %sql
# MAGIC Insert into Employee1 (ename, company, eposition) Values ("Swapn","eClerx","manager");
# MAGIC Insert into Employee1 (ename, company, eposition) Values ("nil","Nepa","Analyst");
# MAGIC Insert into Employee1  (ename, company, eposition) Values ("Ankit","Tata","Sr. Analyst");
# MAGIC
# MAGIC Insert into Employee1  (ename, company, eposition) Values ("Wagh","Accenture","Developer");

# COMMAND ----------

# MAGIC %sql
# MAGIC Select * from employee1;
