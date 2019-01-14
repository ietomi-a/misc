# coding: utf-8
import sys

import urllib.request, urllib.parse
from urllib.request import build_opener, HTTPCookieProcessor
from http.cookiejar import CookieJar

import requests

print(sys.version)
#print("test")

# 以下のコードは
# https://www.softantenna.com/wp/review/httpbin/
# https://www.yoheim.net/blog.php?q=20160204
# を参考にしている.

ROOT_URL = "http://httpbin.org"

def http_GET_test():
    params = {
        "name": "atsushi",
        "age": 29,
        "comment": "my test start ok?"
    }
    p = urllib.parse.urlencode(params)
    url = "%s/get?%s" % ( ROOT_URL, p )
    # print(url)
    with urllib.request.urlopen(url) as res:
        html = res.read().decode("utf-8")
        print(html)

def http_POST_test():
    params = {
        "name": "atsushi",
        "age": 29,
        "comment": "my test start ok?"
    }
    data = urllib.parse.urlencode(params).encode("utf-8")

    url = ROOT_URL + "/post"
    with urllib.request.urlopen( url, data=data) as res:
       html = res.read().decode("utf-8")
       print(html)    


def cookies_test():
    opener = build_opener(HTTPCookieProcessor(CookieJar()))
    url = ROOT_URL + "/cookies/set/kkk/vvv"
    r = requests.get(url)
    print(r.cookies.keys())
    # # url = ROOT_URL + "/post"
    # with opener.open( url ) as res:    
    #     print(res.read().decode("utf-8"))
    return


# http_GET_test()
# http_POST_test()
cookies_test()


# r = requests.get('http://example.com/some/cookie/setting/url')

