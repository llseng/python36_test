# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-01-22 16:13:03
# @LastEditors: llseng
# @LastEditTime: 2021-01-22 16:13:03
#

from time import time
from threading import Thread

import requests, re, os

class download_file( Thread ):
    """
    下载线程
    """
    def __init__( self, url, path ):
        super().__init__()
        self.url = url
        self.path = path

    def run( self ):
        print( "download_file:", self.path, "START" )
        res = requests.get( self.url )
        if res.status_code == 200:
            if self.path[:1] == '/':
                file_path = "logs"+ self.path
            else:
                file_path = "logs/"+ self.path

            if not os.path.exists( os.path.dirname( file_path ) ):
                os.makedirs( os.path.dirname( file_path ) )
            with open( file_path, "wb") as fd:
                fd.write( res.content )

        print( "download_file:", self.path, "END" )

web_url = 'https://www.gzqidong.cn/main/index.html'

web_domain_url = web_url[:web_url.find('/', 10)]
web_now_url = web_url[:web_url.rfind('/')]

print( web_url, web_domain_url, web_now_url )
data = requests.get( web_url )
data.encoding = "UTF-8-SIG"

url_re = re.compile( r"(href|src)=[\'\"](\S+\.\w+)[\'\"]" )
web_files = url_re.findall( data.text )

for f in web_files:
    tmp, file_url = f
    if re.match( r"https?:\/\/", file_url ): continue
    if file_url[:1] == "/":
        req_file_url = web_domain_url + file_url
    else:
        req_file_url = web_now_url + "/" + file_url
    print( file_url, req_file_url )
    download_file( req_file_url, file_url ).start()

# print( data.text )