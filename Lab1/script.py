"""
use pip version of pyspark instead of pyspark attached spark-2.2.1-hadoop
"""
import pyspark
import pyspark.sql
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[*]").appName("lab1").getOrCreate()
testFile = "lab1test.txt"


fileData = spark.read.text(testFile).cache()
type(fileData)
fileData.show()

numAs = fileData.filter(fileData.value.contains('a')).count()
numBs = fileData.filter(fileData.value.contains('b')).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

spark.stop()
