# set up the pyspark environment
import pyspark
from pyspark import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql import SQLContext

# Stop Spark context started by default and start another Spark context
# Allows code to reexecute without error
# sc.stop()
sc = SparkContext("local", "test")

spark = SparkSession(sc)

import pyspark.sql
from pyspark.sql.functions import col, avg
