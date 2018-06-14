#!/usr/bin/env python3
##
## EPITECH PROJECT, 2018
## Sans titre(Espace de travail)
## File description:
## data
##

"""
  Data class

hold datas

"""

class Data:
    """Class that holds different data"""
    def __init__(self):
        self.avg = {
            'crypto': -1,
            'forex': -1,
            'stock_exchange': -1,
            'raw_material': -1
        }
        self.current = {
            'crypto': -1,
            'forex': -1,
            'stock_exchange': -1,
            'raw_material': -1
        }
        self.history = {
            'crypto': [],
            'forex': [],
            'stock_exchange': [],
            'raw_material': []
        }

    def parse_data(self, data):
        """Store data in variables of the class"""
        for elem in data:
            for key in self.current:
                if elem.split(':')[0] == key:
                    string = elem.split(':')[1].replace(',', '.')

                    value = float(string)
                    self.current[key] = value
                    self.history[key].append(value)


    def calc_avg(self):
        """
        calc_avg
        """


        for key in self.avg:
            # tmp = list(reversed(self.history[key]))
            # self.avg[key] = sum(tmp[:14]) / len(tmp[:14])
            self.avg[key] = sum(self.history[key]) / len(self.history[key])

    def __str__(self):
        return 'crypto : {}\nforex : {}\n\
            stock : {}\nraw : {}\n'.format(self.current['crypto'],
                                           self.current['forex'],
                                           self.current['stock_exchange'],
                                           self.current['raw_material'])

