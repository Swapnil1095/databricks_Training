-- Databricks notebook source
create table newemp(id int, name string, city string);
--TRUNCATE emp;

-- COMMAND ----------

create table newemp(id int, name string, city string)


-- COMMAND ----------



-- COMMAND ----------

desc extended newemp



-- COMMAND ----------

-- MAGIC %fs head
-- MAGIC dbfs:/user/hive/warehouse/newemp/_delta_log/00000000000000000000.json
-- MAGIC
-- MAGIC

-- COMMAND ----------



desc history newemp



-- COMMAND ----------

insert into newemp values(1,'a','Mumbai')



-- COMMAND ----------

select * from newemp


-- COMMAND ----------


desc detail newemp

-- COMMAND ----------

insert into newemp values(2,'Swap','Mum'),(3,'nil','Pune'),(4,'Sush','Rajasthan');

-- COMMAND ----------

insert into newemp values(5,'Tarun','Mum')

-- COMMAND ----------

insert into newemp values(2,'Aniket','Rajuri')

-- COMMAND ----------

DELETE from newemp where id=1

-- COMMAND ----------

Select * from newemp version as of 4

-- COMMAND ----------

select * from newemp timestamp as of '2025-06-09T07:31:26.000+00:00'

-- COMMAND ----------


