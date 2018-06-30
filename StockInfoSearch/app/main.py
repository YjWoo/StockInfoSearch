# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template, request
from StockInfoSearch.es.EsDAO import search_by_code, all_search, bool_search, show_all
from StockInfoSearch.setting import *
from StockInfoSearch.util.util import page_count, result_page

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/result")
def result():
    args = request.args
    args_keys = list(args.keys())
    content = args['content']
    field = args['field']

    start = 0 if ('start' not in args_keys) else int(args['start']) * 10
    sort_field = '_score' if ('sort_field' not in args_keys) else args['sort_field']
    sort_direction = 'desc' if ('sort_direction' not in args_keys) else args['sort_direction']

    if field == 'ALL':
        if content != '':
            res = all_search(content, sort={sort_field: sort_direction}, start=start, size=10)
        else:
            res = show_all(sort_field, sort_direction, start=start, size=10)
    else:
        res = bool_search(content, field, sort={sort_field: sort_direction}, start=start, size=10)
    total = res['total']
    page = page_count(total, 10)
    data = result_page(res)
    fields = list(CONDITION_VALUE.keys())
    return render_template("result.html", content=content, total=total, page=page, start=start / 10, data=data,
                           field=field,
                           field_name=CONDITION_KEY[field],
                           fields=fields, sort_field=sort_field, sort_direction=sort_direction)


@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        form = request.form
        form_keys = list(form.keys())

        content = form['content']
        field = CONDITION_VALUE[form['field_name']]

        start = 0 if ('from' not in form_keys) else int(form['from'])
        sort_field = '_score' if ('sort_field' not in form_keys) else form['sort_field']
        sort_direction = 'desc' if ('sort_direction' not in form_keys) else form['sort_direction']

        return jsonify({'content': content, 'field': field, 'start': start, 'sort_field': sort_field,
                        'sort_direction': sort_direction})


@app.route("/detail/<code>")
def detail(code):
    data = search_by_code(code)
    return render_template("detail.html", data=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
