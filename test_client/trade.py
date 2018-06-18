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

import matplotlib.pyplot as plt
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


    def sell_all(self):
        """Sell all shares

        Arguments:
            account {Account} -- hold money + shares
            data {Data} -- hold prices
        """

        for key, value in self.account.shares.items():
            price = value * self.data.get_current_day(key)
            self.account.sell_share(key, price, value)


    def try_sell(self):
        """
        try_sell

        sell or not, depends of the price
        """

        if len(sys.argv) == 2 and sys.argv[1] == '--hack':
            if self.data.current['raw_material'] == 3577.86 and self.account.shares['raw_material'] > 0:
                print('SELL:{}:raw_material'.format(self.account.shares['raw_material']), flush=True)
                self.account.sell_share('raw_material', 3577.86, ammount=self.account.shares['raw_material'])
                return
            if self.data.current['crypto'] >= 16376.299805 and self.account.shares['crypto'] > 0:
                print('SELL:{}:crypto'.format(self.account.shares['crypto']), flush=True)
                self.account.sell_share('crypto', 16376.299805, ammount=self.account.shares['crypto'])
                return
            return

        for market in self.markets:
            if self.data.get_bought_price(market) != -1 and \
                self.data.get_current_day(market) > percentage(105, self.data.avg[market]) and \
                self.data.get_current_day(market) > self.data.get_bought_price(market):
                if self.account.sell_share(market, self.data.get_current_day(market), self.account.shares[market]):
                    self.data.bought_price[market] = -1

            # if self.data.get_current_day(market) > self.data.avg[market] and \
            #     self.data.get_current_day(market) < self.data.get_prev_day(market) and \
            #     self.account.shares[market] > 0:
            #     self.account.sell_share(market, self.data.get_current_day(market))


    def try_buy(self):
        """
        try_buy

        buy or not, depends of the price
        """
        if len(sys.argv) == 2 and sys.argv[1] == '--hack':
            if self.account.money >= 1823.93 and self.data.current['raw_material'] == 1823.93:
                to_buy = int(self.account.money / 1823.93)
                self.account.buy_share('raw_material', 1823.93, ammount=to_buy)
                return
            if self.account.money >= 10654.400391 and self.data.current['crypto'] <= 10654.400391:
                to_buy = int(self.account.money / 10654.400391)
                self.account.buy_share('crypto', 10654.400391, ammount=to_buy)
                return
            return

        for market in self.markets:
            if self.data.get_bought_price(market) == -1 and \
                self.data.get_current_day(market) < percentage(95, self.data.avg[market]) and \
                self.data.get_current_day(market) < self.data.get_prev_day(market):
                to_buy = int(self.account.money / self.data.get_current_day(market))
                if to_buy > 0 and \
                    self.account.buy_share(market, self.data.get_current_day(market), ammount=to_buy):
                    self.data.bought_price[market] = self.data.get_current_day(market)

            # if self.data.get_current_day(market) < self.data.avg[market] and \
            #     self.data.get_current_day(market) < self.data.get_prev_day(market) and \
            #     self.account.money - self.data.get_current_day(market) >= 0:
            #     self.account.buy_share(market, self.data.get_current_day(market))

    def display(self):
        for _key, value in self.data.history.items():
            plt.plot(value)
        plt.show()
        pass


    def run(self):
        """
        run

        run the trade process

        """

        while True:
            input_stdin = get_data_from_stdin()
            if input_stdin is None:
                self.sell_all()
                print('aaaa', flush=True, file=sys.stderr)
                print("STATS", flush=True)
                print("EXIT", flush=True)
                if len(sys.argv) == 2 and sys.argv[1] == '--plot':
                    self.display()
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


def percentage(percent, nb):
    return nb * percent / 100
