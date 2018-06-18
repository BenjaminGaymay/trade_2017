
##
## EPITECH PROJECT, 2018
## Sans titre(Espace de travail)
## File description:
## account
##

"""
  Account class

Stores informations

"""

import logging

LOG_FORMAT = '%(levelname)s: (%(asctime)s) [%(relativeCreated)dms]\t-\t%(message)s'
logging.basicConfig(filename="trade.log", level=logging.DEBUG, filemode='w', format=LOG_FORMAT)
LOGGER = logging.getLogger()

class Account:
    """Stores account informations (money, shares)"""

    def __init__(self, money):
        self.money = money
        self.shares = {
            'crypto': 0,
            'forex': 0,
            'stock_exchange': 0,
            'raw_material': 0
        }

    def buy_share(self, share, price, ammount=1):
        """
        buy_share

        Method to buy share

        :param share: share to buy
        :type share: str
        :param price: price of one share
        :type price: int
        :param ammount: ammount to be bought, defaults to 1
        :param ammount: int, optional
        :return: bought or otn
        :rtype: bool
        """
        total = price * ammount
        if self.money - total >= 0:
            self.shares[share] += ammount
            self.money -= total
            LOGGER.info('BUY:%d:%s:%s€', ammount, share, total)
            print('BUY:{}:{}'.format(ammount, share), flush=True)
            return True
        return False

    def sell_share(self, share, price, ammount=1):
        """
        sell_share

        Method to sell ammount share

        :param share: share to sell
        :type share: str
        :param price: price of one share
        :type price: int
        :param ammount: ammount to be sold, defaults to 1
        :param ammount: int, optional
        :return: sold or not
        :rtype: bool
        """

        total = price * ammount
        if self.shares[share] > 0 and ammount <= self.shares[share]:
            self.shares[share] -= ammount
            self.money += total
            LOGGER.info('SELL:%d:%s:%s€', ammount, share, total)
            print('SELL:{}:{}'.format(ammount, share), flush=True)
            return True
        return False

    def __str__(self):
        return 'money :\t\t {}'.format(self.money)
