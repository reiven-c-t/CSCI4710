import pyspark
import pyspark.sql
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[*]").appName("lab3").getOrCreate()
sc = spark.sparkContext

# Question 12
import pandas as pd
import matplotlib.pyplot as plt

df_pieces = []
path = "/Users/reiven/Documents/Python/CSCI4710/Lab3/names/"

years = range(2013, 2017)
for year in years:
    df_year = pd.read_csv(path + "yob" + str(year) + ".txt", names=["name", "sex", "births"])
    df_year["year"] = year
    df_pieces.append(df_year)

names = pd.concat(df_pieces, ignore_index=True)

spark_df = spark.createDataFrame(names)

cached = spark_df.persist()
spark_df.count()
spark_df.first()

names.shape

spark_df.columns

spark_df.printSchema()
# find Emma names
n = spark_df.filter(cached.name == 'Emma')
n.show()
# top 10
# returns a list type
from pyspark.sql.functions import col

# Question 13
top10 = spark_df[['name', 'births']].groupBy('name').sum().sort(col('sum(births)').desc()).limit(10).show()

# Question 14
print("count of distinct name:", spark_df.select("name").distinct().count())

# Question 15
print("count the names born in 2016:", spark_df.filter(col("year") == "2016").select("name").distinct().count())
