import sys
import io
import string
import re


class MapReduce:
    def __init__(self):
        self.intermediate = dict()
        self.result = []

    def emitIntermediate(self, key, value):
        self.intermediate.setdefault(key, [])
        self.intermediate[key].append(value)

    def emit(self, value):
        self.result.append(value)

    def execute(self, data, mapper, reducer):
        for record in data:
            mapper(record)

        for key in sorted(self.intermediate.keys()):
            # print(key, self.intermediate[key])
            reducer(key, self.intermediate[key])

        self.result.sort()
        for item in self.result:
            print(item)


mapReducer = MapReduce()


def mapper(line):
    """
    split line to word here and return (word, 1)
    :param line:
    :return:
    """
    for c in string.punctuation:
        line = line.replace(c, "")
    line = line.strip().lower()
    words = line.split()
    for word in words:
        mapReducer.emitIntermediate(word, word)  # don't need word as value I think


def reducer(key, list_of_values):
    """
    :param key:
    :param list_of_values:
    :return:
    """
    mapReducer.emit((key, len(list_of_values)))


if __name__ == '__main__':
    inputData = []
    file = open("/Users/reiven/Documents/Python/CSCI4710/Lab2/TheRoadNotTaken.txt", "r")
    for line in file:
        inputData.append(line)
    mapReducer.execute(inputData, mapper, reducer)
