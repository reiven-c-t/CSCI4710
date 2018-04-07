import os
import sys

spark_path = "utils/spark-2.2.1-bin-hadoop2.7"

os.environ['SPARK_HOME'] = spark_path
os.environ['HADOOP_HOME'] = spark_path

sys.path.append(spark_path + "/bin")
sys.path.append(spark_path + "/python")
sys.path.append(spark_path + "/python/pyspark/")
sys.path.append(spark_path + "/python/lib")
sys.path.append(spark_path + "/python/lib/pyspark.zip")
sys.path.append(spark_path + "/python/lib/py4j-0.10.4-src.zip")

import pyspark

import pyspark.sql
from pyspark.sql import SparkSession

# local[*]  Run Spark locally with as many worker threads
#       	as logical cores on your machine
# getOrCreate() Gets an existing SparkSession or, if there
#       	is no existing one, creates a new one based on the
#       	options set in this builder

spark = SparkSession \
    .builder \
    .master("local[*]") \
    .appName("lab1") \
    .getOrCreate()


testFile = "lab1test.txt"


fileData = spark.read.text(testFile).cache()
type(fileData)
fileData.show()

numAs = fileData.filter(fileData.value.contains('a')).count()
numBs = fileData.filter(fileData.value.contains('b')).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

spark.stop()
