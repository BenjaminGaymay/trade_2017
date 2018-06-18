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
        self.bought_price = {
            'crypto': -1,
            'forex': -1,
            'stock_exchange': -1,
            'raw_material': -1
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


    def get_bought_price(self, market):
        """
        get_bought_price [summary]

        Returns the price of the last market's share price bought

        :param market: market's name
        :type market: str
        """
        return self.bought_price[market]


    def get_prev_day(self, market):
        """
        get_prev_day

        Return previous day

        :param market: market's name
        :type market: str
        :return: price of stock of previous day
        :rtype: float
        """

        try:
            return self.history[market][-2]
        except IndexError:
            return -1


    def get_current_day(self, market):
        """
        get_current_day

        Return current day

        :param market: market's name
        :type market: str
        :return: price of current day's stock
        :rtype: float
        """

        return self.current[market]

    def calc_avg(self):
        """
        calc_avg
        """


        for key in self.avg:
            self.avg[key] = sum(self.history[key]) / len(self.history[key])

    def __str__(self):
        return 'crypto : {}\nforex : {}\n\
            stock : {}\nraw : {}\n'.format(self.current['crypto'],
                                           self.current['forex'],
                                           self.current['stock_exchange'],
                                           self.current['raw_material'])
