import sys
import re
from operator import add
import string

from pyspark.sql import SparkSession


def remove_punctuation(word):
    for c in string.punctuation:
        word = word.replace(c, "")
    return word

if __name__ == "__main__":
    # if len(sys.argv) != 2:
    #     print("Usage: wordcount <file>", file=sys.stderr)
    #     exit(-1)

    spark = SparkSession\
        .builder\
        .master("local[*]")\
        .appName("lab2")\
        .getOrCreate()

    lines = spark.read.text("/Users/reiven/Documents/Python/CSCI4710/Lab2/TheRoadNotTaken.txt").rdd.map(lambda r: r[0])
    # remove punctuation and lowercase
    counts = lines.flatMap(lambda x: remove_punctuation(x).split(' ')) \
                  .map(lambda x: x.strip().lower())\
                  .map(lambda x: (x, 1)) \
                  .reduceByKey(add)
    output = counts.collect()
    for (word, count) in output:
        print("%s: %i" % (word, count))

    spark.stop()