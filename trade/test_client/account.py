
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
        if ammount <= self.shares[share]:
            self.shares[share] -= ammount
            self.money += total
            return True
        return False

    def __str__(self):
        return 'money :\t\t {}'.format(self.money)
