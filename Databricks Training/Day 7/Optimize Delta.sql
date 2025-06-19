-- Databricks notebook source
Create Table Demo(id int, name string)


-- COMMAND ----------

insert into Demo Values (1,'Swap');
insert into Demo Values (2,'Nil');
insert into Demo Values (3,'Tar');
insert into Demo Values (4,'Unni');
insert into Demo Values (5,'Dher');
insert into Demo Values (6,'Rahul');
insert into Demo Values (7,'Yend');

-- COMMAND ----------

DELETE from Demo where id>4

-- COMMAND ----------

Select * from Demo where id=4

-- COMMAND ----------

desc Demo

-- COMMAND ----------

Desc history Demo

-- COMMAND ----------

desc detail Demo


-- COMMAND ----------



-- COMMAND ----------

OPTIMIZE Demo
ZORDER BY (id)

-- COMMAND ----------

delete from demo

-- COMMAND ----------

restore table Demo to version as of 9

-- COMMAND ----------

select * from demo

-- COMMAND ----------

desc history demo


-- COMMAND ----------

desc detail demo


-- COMMAND ----------

vacuum demo retain 0 hours -- #remove stale files and can't perform time travelling 
--Retention period : 7 day's or 168 hrs
--Can't restore this command , only extend the hours ...

-- COMMAND ----------

SET spark.databricks.delta.retentionDurationCheck.enabled = false


-- COMMAND ----------

SELECT * FROM demo

-- COMMAND ----------


