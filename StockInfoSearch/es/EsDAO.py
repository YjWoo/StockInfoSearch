from elasticsearch import Elasticsearch
import traceback
from StockInfoSearch.settting import *
from StockInfoSearch.util.util import split_str

es = Elasticsearch(['%s:%s' % (ES_HOST, ES_PORT)])


def insert_one(code, body):
    try:
        es.index(index=ES_INDEX, doc_type=ES_TYPE, body=body, id=code)
    except Exception:
        traceback.print_exc()


def update_one(code, body):
    try:
        es.update(index=ES_INDEX, doc_type=ES_TYPE, id=code, body={'doc': body})
    except Exception:
        traceback.print_exc()


def delete_one(code, body={}):
    try:
        if body == {}:
            es.delete(index=ES_INDEX, doc_type=ES_TYPE, id=code)
        else:
            es.delete_by_query(index=ES_INDEX, doc_type=ES_TYPE, body=body)
    except Exception:
        traceback.print_exc()


def search(dsl):
    # 根据dsl语句搜索
    try:
        return es.search(index=ES_INDEX, doc_type=ES_TYPE, body=dsl)
    except Exception:
        traceback.print_exc()


def search_by_code(code):
    # 根据结果返回
    return es.get(index=ES_INDEX, doc_type=ES_TYPE, id=code)['_source']


def bool_search(content, field, sort={'_score': 'desc'}, func='must', start=0, size=10):
    # 布尔搜索
    content = split_str(content)
    str_dict = []
    for item in content:
        str_dict.append({'match': {field: item}})
    dsl = {'query': {'bool': {func: str_dict}}, 'highlight': {'fields': {field: {}}, "pre_tags": ["<font color='red'>"],
                         "post_tags": ["</font>"]}, 'size': size,
           'from': start,
           'sort': sort}
    return search(dsl)['hits']


def all_search(content, sort={'_score': 'desc'}, start=0, size=10):
    # 全文搜索
    dict_list = {}
    for i in FIELDS:
        dict_list[i] = {}
    dsl = {'query': {'multi_match': {'query': content, 'fields': FIELDS, 'operator': 'and', "type": "most_fields"}},
           'highlight': {"boundary_chars": ".,!? \t\n，。！？", 'fields': dict_list, "pre_tags": ["<font color='red'>"],
                         "post_tags": ["</font>"]}, 'size': size, 'from': start,
           'sort': sort}
    return search(dsl)['hits']


if __name__ == '__main__':
    # res = bool_search(['小米'], 'HXTC', start=0, size=10)
    # res = res['hits']
    # print(len(res))
    # for i in res:
    #     print(i['highlight'])

    # res = all_search('小米 msci')['hits']['hits']
    # for i in res:
    #     print(i['_score'])

    res = bool_search('小米', 'BK')
    print(res)
