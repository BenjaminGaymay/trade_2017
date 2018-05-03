#!/usr/bin/env python3
from flask import Flask, render_template
import csv

app = Flask(__name__)

def load(filename):
	p = []
	d = []
	with open(filename, 'r') as csv_file:
		csv_reader = csv.reader(csv_file)
		next(csv_reader)
		for r in csv_reader:
			d.append(int(r[0].split('-')[0]))
			p.append(float(r[1]))
	return d, p

@app.route('/')
def main():
	dates, prices = load("./datas/NFLX2.csv")
	return render_template("index.html", dates=dates, prices=prices)

if __name__ == '__main__':
	app.run(debug=True)