import unittest
from src.util.operateStock import OperateStock
from src.util.portfolioGroup import PortfolioGroup
from src.util.parsJson import *



class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def teardown(self):
        pass

    def setUp(self):
        self.run = OperateStock()
        self.exe = PortfolioGroup()
        self.exist = self.run.has_exist()['data']['hasExist']

    def test_add_stock(self):

        if self.exist == False:
            self.run.add_stock()
            self.assertEqual(self.run.add_stock()['data'], True, msg="用例失败")
            dict=self.exe.portfolio_stock_group()
            obkey="include"
            print(dict_get(dict, obkey, None))
            self.assertEqual(dict_get(dict,obkey,None),True,msg="用例失败")
            print("添加股票成功。。。")
        else:
            print("股票已存在。。。")


    def test_cancel_stock(self):
        if self.exist == True:
            self.run.cancel_stock()
            print("删除股票成功。。。。")




#if __name__ == "__name__":
unittest.main()


















