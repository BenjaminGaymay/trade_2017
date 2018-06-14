##
## EPITECH PROJECT, 2018
## Sans titre(Espace de travail)
## File description:
## trade
##

"""
 Trade class

Holds everything

"""

import sys
from data import Data
from account import Account

class Trade:
    """
     Trade class

    """

    def __init__(self):
        self.data = Data()
        self.account = Account(10000)
        self.markets = ['crypto', 'forex', 'stock_exchange', 'raw_material']
        self.inc = 0
        self.dec = 0

    def sell_all(self):
        """Sell all shares

        Arguments:
            account {Account} -- hold money + shares
            data {Data} -- hold prices
        """
        for key, value in self.account.shares.items():
            print('SELL:{}:{}'.format(value, key), flush=True)
            self.account.money += value * self.data.current[key]


    def check_buy(self):
        """Check values to know if we should buy

        Arguments:
            account {Account} -- contains money+current shares
            data {Data} -- contains all different datas of shares
        """


        for market in self.markets:
            if self.data.current[market] < self.data.avg[market] and \
                self.data.current[market] < self.data.history[market][-2] and \
                self.account.money - self.data.current[market] >= 0:
                print('BUY:1:{}'.format(market), flush=True)
                self.account.money -= self.data.current[market]
                self.account.shares[market] += 1
            elif self.data.current[market] > self.data.avg[market] and \
                self.data.current[market] < self.data.history[market][-2] and \
                self.account.shares[market] > 0:
                print('SELL:{}:{}'.format(self.account.shares[market], market), flush=True)
                self.account.shares[market] -= 1
                self.account.money += self.data.current[market]

    def try_sell(self):
        """
        try_sell

        sell or not, depends of the price
        """
        for market in self.markets:
            if self.data.current[market] < self.data.history[market][-2]:
                self.inc = 0
                self.dec += 1
            if self.dec >= 3 and self.account.shares[market] > 0:
                self.account.sell_share(market, self.data.current[market])
                print('SELL:{}:{}'.format(1, market), flush=True)


    def try_buy(self):
        """
        try_buy

        buy or not, depends of the price
        """
        for market in self.markets:
            if self.data.current[market] > self.data.history[market][-2]:
                self.dec = 0
                self.inc += 1
            if self.inc >= 3 and self.account.money >= self.data.current[market]:
                self.account.buy_share(market, self.data.current[market])
                print('BUY:1:{}'.format(market), flush=True)

    def run(self):
        """
        run

        run the trade process

        """
        while True:
            input_stdin = get_data_from_stdin()
            if input_stdin is None:
                self.sell_all()
                print("STATS", flush=True)
                print("EXIT", flush=True)
                break
            self.data.parse_data(input_stdin)
            self.data.calc_avg()
            if len(self.data.history['forex']) <= 1:
                continue
            self.try_buy()
            self.try_sell()
            print("STATS", flush=True)



def get_data_from_stdin():
    """Get data from stdin"""
    data = []
    for i in range(4):
        data.append(sys.stdin.readline())
        if not data[-1]:
            return None
        i = i
    return data


def get_data_from_file(file):
    """
    get_data_from_file

    get file's content

    Args:
        file ([type]): [description]

    Returns:
        [type]: [description]
    """


    data = []
    try:
        with open(file, 'r') as filefd:
            data = filefd.readlines()
    except FileNotFoundError as err:
        data = None
        print(err)
    return data
