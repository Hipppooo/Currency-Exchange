from Currency import *
import configparser


class CurrencyModule(object):
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('currencies.properties')

        self.__currencies = list()

        for i in range(8):
            name = config['Currencies']['currency' + str(i + 1) + '.name']
            exchange_rate = config['Currencies']['currency' + str(i + 1) + '.exchange_rate']
            divider = config['Currencies']['currency' + str(i + 1) + '.divider']

            self.__currencies.append(Currency(name, exchange_rate, divider))

        # cur = self.currencies[7]
        # print(cur.get_name(), cur.get_exchange_rate())

    def get_currencies(self):
        return self.__currencies
