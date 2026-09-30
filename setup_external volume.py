# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC USE CATALOG ecommerce;
# MAGIC
# MAGIC CREATE SCHEMA IF NOT EXISTS raw;
# MAGIC
# MAGIC CREATE EXTERNAL VOLUME IF NOT EXISTS raw.raw_landing
# MAGIC LOCATION 'abfss://ecomm-raw-data@stgecomadlsddevap001.dfs.core.windows.net/'
# MAGIC COMMENT 'landing zone for raw data';