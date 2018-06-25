from StockInfoSearch.es import EsDAO
from StockInfoSearch.spider import StocksInfo

def insert_info_to_es():
    # 将每一项爬取数据存储至ES数据库
    f_insert=EsDAO.insert_one
    StocksInfo.get_Stock_info(f_insert)

def update_info_to_es():
    # 每日更新数据至es
    f_update=EsDAO.update_one
    StocksInfo.get_Stock_info(f_update)

if __name__=='__main__':
    update_info_to_es()