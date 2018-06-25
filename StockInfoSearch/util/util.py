def split_str(content):
    return content.split(' ')


def page_count(total, size):
    # 计算页码
    page = int(total / size)
    if total % size != 0:
        page += 1
    return page


def result_page(res):
    # result页内容格式化
    res = res['hits']
    res_data = []
    for item in res:
        highlight=list(map(lambda x:x[0],item['highlight'].values()))
        res_data.append(
            {'code': item['_id'], 'code_name': item['_source']['SECURITYSHORTNAME'], 'score': item['_score'],
             'highlight': '...'.join(highlight)})
    return res_data

def get_keys(d, value):
    # 根据value取key
    return [k for k,v in d.items() if v == value]

def reverse_key_value(dict_list):
    # 反转key-value
    return {value:key for key,value in dict_list.items()}

if __name__ == '__main__':
    print(split_str('广东板块 环保工程 节能环保'))
    print(page_count(271, 10))

    from StockInfoSearch.es.EsDAO import all_search
    print(result_page(all_search('小米 msci')))

    print(reverse_key_value({'全文搜索': 'ALL', '股票代码': 'SECURITYCODE', '股票名称': 'SECURITYSHORTNAME', '隶属板块': 'BK',
                             '商业业务': 'BUSINSCOPE',
                             '主营业务': 'COMPSCOPE', '公司详情': 'HXTC'}))

