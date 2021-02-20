# -*- coding: utf-8 -*-
# @Author: llseng
# @Date:   2021-02-19 18:27:07
# @Last Modified by:   llseng
# @Last Modified time: 2021-02-20 18:51:18

import funcs, os

def main():
    url = input( "请输入小说地址" )
    if url.find( funcs.DOMAIN ) < 0:
        print( f"只能是 {funcs.DOMAIN} 里的小说" )
        return

    html = funcs.get_html( url )

    metas = funcs.get_meta( html )
    lists = funcs.get_list2( html )

    if not metas['title']:
        print( '未检测到小说信息' )
        return

    print( metas )

    try:
        txtfile = open( metas['title'] + '.txt', 'w', encoding='utf-8' )
        txtfile.write( metas['title'] + "\n\n\n" )
        txtfile.write( '    作者:' + metas['author'] + "\n\n" )

        i = 0
        for x in lists:
            if x['title'] == '插图': continue

            if x['title'][-1] not in ['卷']:
                i += 1
                x['title'] = f'第{i}章 {x["title"]}'
            else:
                i = 0

            txtfile.write( ' ' + x['title'] + "\n\n\n" )

            if x['url']:
                print( x )
                content = funcs.get_content( 'https://' + funcs.DOMAIN + x['url'] )
                contents = [ '    ' + line + "\n\n" for line in content ]
                txtfile.writelines( contents )
                

    except Exception as e:
        print( repr( e ) )

    pass

if __name__ == '__main__':
    main()