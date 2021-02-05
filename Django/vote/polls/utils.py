#
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-02-04 19:30:25
# @LastEditors: llseng
# @LastEditTime: 2021-02-04 19:31:14
#
import hashlib

def gen_md5_digest( content ):
    return hashlib.md5( content.encode() ).hexdigest()