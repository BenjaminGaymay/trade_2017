#!/usr/bin/env python3

import requests
import csv
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint
import time


class Datas:
	"""
	Datas class
	"""
	def __init__(self, filename):
		"""
		Init Function
		:param filename: file with datas
		"""

		self.filename = filename
		self.dates = []
		self.prices = []
		self.example = []
		self.get_datas()


	def get_datas(self):
		"""
		get datas from csv file
		"""
		with open(self.filename, 'r') as csv_file:
			csv_reader = csv.reader(csv_file)
			next(csv_reader)
			for row in csv_reader:
				self.dates.append(row[0])
				self.prices.append(float(row[1]))


	def calc_avg(self, prices):
		return sum(prices) / len(prices)


def main():
	datas = Datas("./datas/NFLX.csv")

	# -1 UNDEF
	# 0 BUY
	# 1 SELL
	state = -1

	money = 1000.0
	_list = []
	i = 0
	print("Money at start: %.2f$" % money)
	while True:
		if (i < len(datas.prices)):
			_list.append(datas.prices[i])
		else:
			break
		avg = datas.calc_avg(_list)
		if _list[i] > avg and _list[i] > _list[i-1]:
			print("SELL")
			money += _list[i]
			state = 0
		elif _list[i] < avg and _list[i] < _list[i-1]:
			print("BUY")
			money -= _list[i]
			state = 1
		i += 1
	print("Money at end: %.2f$" % money)


if __name__ == '__main__':
	main()