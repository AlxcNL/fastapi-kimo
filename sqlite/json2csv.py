#!/usr/bin/env python

# Author: J.A.Boogaard@hr.nl

import json
import logging
import pandas as pd

jsonFile = "../data/courses.json"
csvFile = "../data/courses.csv"

logging.basicConfig(level=logging.INFO)

with open(jsonFile) as data_file:
    coursesList = json.load(data_file)

coursesItem = coursesList[0]

logging.debug(f"Type coursesList : {type(coursesList)}")
logging.debug(f"Type coursesItem : {type(coursesItem)}")

del coursesItem['chapters']
logging.debug(coursesItem)

coursesDf = pd.DataFrame(coursesItem)
logging.info(coursesDf)

# Save as CSV
coursesDf.to_csv(csvFile, index=False, sep=';')
