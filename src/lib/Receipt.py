import re
from ProcessEntry import *
import typing as t

class ReceiptEntry:
    def __init__(self, name, price, qty) -> None:
        self.name = name 
        self.price = price 
        self.qty = qty

    def printPosition(self):
        print('\tName: {0}, Price: {1}, Qty: {2}'.format(self.name, self.price, self.qty))


class Receipt:
    def __init__(self, productList: list, date = None, totalPrice = None) -> None:
        self.productList = [
            ReceiptEntry(item[0], item[1], item[2]) for item in productList
        ]
        self.date = date
        self.totalPrice = totalPrice

    def printReceipt(self):
        print('Date: {0}\nTotal Price: {1}'.format(self.date, self.totalPrice))
        print('Receipt Content:')
        for item in self.productList:
            item.printPosition()


class ReceiptMatcher:    
    def __init__(self) -> None:
        matchEntriexRegex = r'''
        [0-9]+[ ]                                   # Receip entry start with an ordinal literal
        (?P<Name>[ а-я!-]+)+                        # Product name - 1 or more distinct words 
        (?P<Price>[0-9]+[., ]?[0-9][0-9])[ *_#«]+   # Price - always contains 2 fixed point digits
        (?P<Qty>[0-9.]+)'''                         # Qty - either integer or fixed-point number w/ 3 fixed-point digits
        matchDateRegex = r'''(?P<Date>[0-3][0-9].[0-1][0-9].[2-3][0-9])'''
        matchTotalPriceRegex = r'''Сумма[ _][(]Руб[)]: (?P<TotalPrice>[0-9]+[.]?[0-9][0-9])'''

        self.__matchEntries__ = re.compile(matchEntriexRegex, re.VERBOSE | re.IGNORECASE)
        self.__matchDate__ = re.compile(matchDateRegex)
        self.__matchTotalPrice__ = re.compile(matchTotalPriceRegex)

    def __searchDate__(self, text) -> t.Union[str, None]:
        try:
            dateMatch = self.__matchDate__.search(text).group('Date')
        except AttributeError:
            return None
        dateMatch = trimSpaceAndReplaceComma(dateMatch)
        return dateMatch

    def __searchTotalPrice__(self, text) -> t.Union[str, None]:
        try:
            totalPriceMatch = self.__matchTotalPrice__.search(text).group('TotalPrice')
        except AttributeError:
            return None
        totalPriceMatch = trimSpaceAndReplaceComma(totalPriceMatch)
        totalPriceMatch = insertDot(totalPriceMatch, 2)
        return totalPriceMatch

    def __searchReceiptEntries__(self, text) -> list:
        entriesMatches = self.__matchEntries__.findall(text)
        entriesMatches = map(processEntry, entriesMatches)
        return entriesMatches
    
    def makeReceipt(self, text) -> Receipt:
        date = self.__searchDate__(text)
        totalPrice = self.__searchTotalPrice__(text)
        entries = self.__searchReceiptEntries__(text)

        return Receipt(entries, date = date, totalPrice = totalPrice)