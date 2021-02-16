"""BaiduSpider API

TODO: 添加关于API的文档
"""
import os

from flask import Flask, request
from flask_cors import CORS

import os
import sys

from baiduspider import BaiduSpider

app = Flask(__name__)
cors = CORS(app, supports_credentials=True)
spider = BaiduSpider()


@app.route('/web')
def search_web():
    query = request.args.get('query')
    page = int(request.args.get('page', 1))
    return {
        'status': 'success',
        'results': spider.search_web(query, page)
    }


@app.route('/pic')
def search_pic():
    query = request.args.get('query')
    page = int(request.args.get('page', 1))
    return {
        'status': 'success',
        'results': spider.search_pic(query, page)
    }


@app.route('/zhidao')
def search_zhidao():
    query = request.args.get('query')
    page = int(request.args.get('page', 1))
    return {
        'status': 'success',
        'results': spider.search_zhidao(query, page)
    }


@app.route('/video')
def search_video():
    query = request.args.get('query')
    page = int(request.args.get('page', 1))
    return {
        'status': 'success',
        'results': spider.search_video(query, page)
    }


@app.route('/news')
def search_news():
    query = request.args.get('query')
    page = int(request.args.get('page', 1))
    return {
        'status': 'success',
        'results': spider.search_news(query, page)
    }


@app.route('/wenku')
def search_wenku():
    query = request.args.get('query')
    page = int(request.args.get('page', 1))
    return {
        'status': 'success',
        'results': spider.search_wenku(query, page)
    }


@app.route('/jingyan')
def search_jingyan():
    query = request.args.get('query')
    page = int(request.args.get('page', 1))
    return {
        'status': 'success',
        'results': spider.search_jingyan(query, page)
    }


@app.route('/baike')
def search_baike():
    query = request.args.get('query')
    return {
        'status': 'success',
        'results': spider.search_baike(query)
    }


@app.route('/status')
def get_status():
    return {
        'status': 'online'
    }


if __name__ == '__main__':
    app.run()
