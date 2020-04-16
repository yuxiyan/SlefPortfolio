from src.util.sendMethod import SendMethod
from src.util.parsJson import *
import random


class PortfolioGroup:

    def __init__(self):
        self.run = SendMethod()
        self.cookies = SendMethod().get_token()
        self.group = "123"
        self.params = dict()

    def portfolio_stock_group(self):
        self.params["category"]="1"
        self.params["symbol"]=".INX"
        url = r"https://stock.xueqiu.com/v5/stock/portfolio/list.json?"
        method = 'GET'
        res = self.run.send_method(url, self.cookies, self.params, method)
        print(res)
        return res

    def portfolio_create_group(self,default=False):

        if default:
            self.group=random.choice("abcdef")
        self.params["pnames"] = self.group
        self.params["category"] = "1"
        url = r"https://stock.xueqiu.com/v5/stock/portfolio/create.json"
        method = 'POST'
        res = self.run.send_method(url, self.cookies, self.params, method)
        return res
    def portfolio_cancel_group(self):
        self.params["pnames"] = self.group
        self.params["category"] = "1"
        url = r"https://stock.xueqiu.com/v5/stock/portfolio/create.json"
        method = 'POST'
        res = self.run.send_method(url, self.cookies, self.params, method)
        return res



if __name__ == "__name__":
    dict=PortfolioGroup().portfolio_cancel_group()
    #print(dict)
    objkey='id'

    key=dict_get(dict, objkey,None)
    print(key)

