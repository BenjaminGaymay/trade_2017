#!/usr/bin/env python3

import requests
import csv
import matplotlib.pyplot as plt

datas = []

with open('datas/NFLX.csv', 'r') as csvfile:
	csv_reader = csv.reader(csvfile)
	next(csv_reader)
	for line in csv_reader:
		datas.append(float(line[1]))

plt.plot(datas)
plt.show()