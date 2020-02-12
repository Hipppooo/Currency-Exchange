class Currency(object):
    def __init__(self, name, exchange_rate, divider):
        self.set_name(name)
        self.divider = divider
        self.set_exchange_rate(exchange_rate, self.divider)

    def get_name(self):
        return self.__name

    def get_exchange_rate(self):
        return self.__exchange_rate

    def set_name(self, name):
        #         Sprawdzenie try catch
        self.__name = name

    def set_exchange_rate(self, exchange_rate, divider):
        #         Sprawdzenie try catch
        self.__exchange_rate = float(exchange_rate)/float(divider)
