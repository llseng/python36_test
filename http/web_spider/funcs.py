# -*- coding: utf-8 -*-
# @Author: llseng
# @Date:   2021-02-19 18:27:07
# @Last Modified by:   llseng
# @Last Modified time: 2021-02-20 17:14:20

import re, requests

DOMAIN = 'www.linovelib.com'

LIST_META_REX = r'\<div\sclass=\"book\-meta\"\>([\s\S]*?)\<\/div\>'
LIST_TITLE_REX = r'\<h1\>(?P<title>[\s\S]*?)\<\/h1\>'
LIST_STAN_REX = r'\<span\>([\s\S]*?)\<\/span\>'
LIST_AUTHOR_REX = r'\<a([\s\S]*?)\>(?P<author>[\s\S]*?)\<\/a\>'

LIST_UL_REX = r'\<ul\sclass=\"chapter-list\sclearfix\"\>([\s\S]*?)\<\/ul\>'
LIST_LABEL_REX = r'\<(div|li)([\s\S]*?)\>(?P<html>[\s\S]*?)\<\/(div|li)\>'
LIST_LI_REX = r'\<li\sclass=\"col-4\">([\s\S]*?)\<\/li\>'
LIST_A_REX = r'\<a\shref=\"(?P<url>[^\"]*?)\"\>(?P<title>[\s\S]*?)\<\/a\>'

CONTENT_P_REX = r'\<p\>(?P<p>[\s\S]*?)\<\/p\>'
CONTENT_ALSO_REX = r'\<p\sstyle=\"font-weight:\s400;color:\#721f27;\"\>'
CONTENT_ALSO_URL_REX = r'\<a\shref=\"(?P<url>[^\"]*?)\"\>下一章\<\/a\>'

# 标题与信息
def get_meta( html ):

    m = {'title': None, 'author': None}
    metao = re.search( LIST_META_REX, html )
    if metao:
        meta_html = metao.group(1)

        titleo = re.search( LIST_TITLE_REX, meta_html )
        if titleo:
            m['title'] = titleo.group('title') 

        authoro = re.search( LIST_AUTHOR_REX, meta_html )
        if authoro:
            m['author'] = authoro.group('author') 

    return m

# 目录
def get_list( html ):

    l = []
    ulo = re.search( LIST_UL_REX, html )
    if not ulo: return l

    ul_html = ulo.group(1)

    l = [ {'url': x.group('url'), 'title': x.group('title') } for x in re.finditer( LIST_A_REX, ul_html ) ]

    return l

# 目录2
def get_list2( html ):

    l = []
    ulo = re.search( LIST_UL_REX, html )
    if not ulo: return l

    ul_html = ulo.group(1)

    def li_case_func( s ):
        label = {'url': None, 'title': None}

        ao = re.search( LIST_A_REX, s )
        if ao:
            label['url'] = ao.group('url')
            label['title'] = ao.group('title')

        return label

    li_cases = {'div': lambda s: {'url': None, 'title': re.sub( r'\<[\w]+([\s\S]*?)\>([\s\S]*?)\<\/[\w]+\>', '', s )}, 'li': li_case_func }
    for x in re.finditer( LIST_LABEL_REX, ul_html ):
        case = li_cases.get( x[1], None )
        if not case:
            print( x[0] )
            continue
        l.append( case( x.group('html') ) )

    return l

# 获取章节
def get_content( url ):
    also = True
    ps = ['']
    while also:
        html = get_html( url )
        html_ps = get_ps( html )
        if not html_ps: break

        ps[-1] += html_ps[0]
        ps += html_ps[1:]
        also = is_also( html )
        if also:
            url = 'https://' + DOMAIN + get_also_url( html )

    return ps

# 获取内容
def get_ps( html ):
    return re.findall( CONTENT_P_REX, html )

# 是否还有内容
def is_also( html ):
    if re.search( CONTENT_ALSO_REX, html ): return True
    else: return False

# 获取下一页地址
def get_also_url( html ):
    url = None
    auo = re.search( CONTENT_ALSO_URL_REX, html )
    if auo:
        url = auo.group( 'url' )

    return url

def get_html( url ):
    html = ''

    try:
        r = requests.get( url, timeout = 15 )
        r.encoding = 'utf-8'
        html = r.text
    except Exception as e:
        html = repr( e )
        print( '异常', html )

    return html

def main():
    # print( get_content( 'javascript:cid(0)' ) )
    pass

if __name__ == '__main__':
    main()
