#!/usr/bin/env python

# Author: J.A.Boogaard@hr.nl

import json
import logging
import pandas as pd

jsonFile = "../data/courses.json"
csvFile = "../data/courses.csv"
separator = ';'

logging.basicConfig(level=logging.DEBUG)

with open(jsonFile) as data_file:
    coursesList = json.load(data_file)

logging.debug(f"Type coursesList : {type(coursesList)}")

logging.info("Write CSV Header")

firstLine = coursesList[0]
del firstLine['chapters']
cols = list(firstLine.keys())
logging.debug(type(cols))

header = f"{separator}".join(cols)
logging.info(header)

with open(csvFile, "w", encoding="utf-8") as f:
    f.write(header)

for coursesItem in coursesList:
    del coursesItem['chapters']
    logging.debug(coursesItem)

    coursesDf = pd.DataFrame(coursesItem)
    logging.debug(coursesDf)

    coursesDf.to_csv(csvFile, index=False, sep=separator, mode='a', header=False)

