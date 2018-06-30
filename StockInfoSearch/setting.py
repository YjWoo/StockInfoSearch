# ES配置
ES_HOST = 'localhost'
ES_PORT = 9200
ES_INDEX = 'stock'
ES_TYPE = 'info'

FIELDS = ["BK", "BUSINSCOPE", "COMPPROFILE", "COMPSCOPE", "HXTC", "LISTINGDATE",
          "LISTINGTYPE", "MAINBUSIN", "SECURITYCODE",
          "SECURITYSHORTNAME", "ZYCP"]

FIELDS_ALL = ["BK",
              "BUSINSCOPE",
              "COMPPROFILE",
              "COMPSCOPE",
              "ChangePercent",
              "Close",
              "HXTC",
              "LISTINGDATE",
              "LISTINGTYPE",
              "LTGB",
              "LTSZ",
              "MAINBUSIN",
              "MarketValue",
              "PB",
              "PERation",
              "SECURITYCODE",
              "SECURITYSHORTNAME",
              "ZGB",
              "ZYCP",
              ]

CONDITION_VALUE = {'全文搜索': 'ALL', '股票代码': 'SECURITYCODE', '股票名称': 'SECURITYSHORTNAME', '隶属板块': 'BK',
                   '商业业务': 'BUSINSCOPE',
                   '主营业务': 'COMPSCOPE', '公司详情': 'HXTC'}

CONDITION_KEY = {'ALL': '全文搜索', 'SECURITYCODE': '股票代码', 'SECURITYSHORTNAME': '股票名称', 'BK': '隶属板块', 'BUSINSCOPE': '商业业务',
                 'COMPSCOPE': '主营业务', 'HXTC': '公司详情'}
