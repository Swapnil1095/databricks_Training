-- Databricks notebook source
--Managed in internal path (allocated by databrics engine
create table demo_vendors (id int, name string) 

-- COMMAND ----------

-- Externally Managed by user
create table demo_vendors_unmanaged (id int, name string) location '/FileStore/eClerx Input Files/vendors'

-- COMMAND ----------

insert into demo_vendors values (1,'a');
insert into demo_vendors_unmanaged values (1,'a');

-- COMMAND ----------

select * from demo_vendors_unmanaged

-- COMMAND ----------

select * from demo_vendors



-- COMMAND ----------



-- COMMAND ----------

desc extended demo_vendors

-- COMMAND ----------

desc extended demo_vendors_unmanaged

-- COMMAND ----------

DROP TABLE demo_vendors_unmanaged

-- COMMAND ----------

DROP TABLE demo_vendors

-- COMMAND ----------



-- COMMAND ----------


