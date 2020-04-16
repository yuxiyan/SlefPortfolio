
from src.util.sendMethod import SendMethod


class OperateStock:

    def __init__(self):
        self.run = SendMethod()
        self.cookies = SendMethod().get_token()
        self.symbol=".INX"
        self.params = dict()

    def add_stock(self):
        self.params["symbols"] = self.symbol
        url = r"https://stock.xueqiu.com/v5/stock/portfolio/stock/add.json"
        method = 'POST'
        res = self.run.send_method(url, self.cookies, self.params, method)
        return res

    def cancel_stock(self):
        self.params["symbols"]=self.symbol
        method = 'POST'
        url = r"https://stock.xueqiu.com/v5/stock/portfolio/stock/cancel.json"
        res = self.run.send_method(url, self.cookies, self.params, method)
        return res


    def has_exist(self):
        self.params["symbol"] = self.symbol
        url = r"https://stock.xueqiu.com/v5/stock/portfolio/stock/hasexist.json"
        method = 'GET'
        res = self.run.send_method(url, self.cookies, self.params, method)
        return res




