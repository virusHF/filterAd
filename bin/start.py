# coding=utf-8
import re

import chardet
import sys

reload(sys)
sys.setdefaultencoding('utf8')

rules = [
    u'www.mianhuatang.cc',
    u'------------',
    u'（ 好看的小说棉花糖',
    u'想看的书几乎都有啊，比一般的小说网站要稳定很多更新还快，全文字的没有广告。]',
    u'求书网小说qiushu.cc',
    u'txt小说下载80txt.com',
    u'（www.qiushu.cc 好看的小说',
    u'破防盗完美章节，请用搜索引擎各种小说任你观看<!--80txt.com-ouoou-->',
    u'（ 好看的小说',
    u'<!--80txt.com-ouoou-->',
    u'【 www.80txt.com】',
    u'请用搜索引擎完美，各种小说任你观看',
    u'，请用搜索引擎各种小说任你观看',
    u'看清爽的小说就到',
    u'[&#26825;&#33457;&#31958;&#23567;&#35828;&#32593;&#77;&#105;&#97;&#110;&#104;&#117;&#97;&#116;&#97;&#110;&#103;&#46;&#99;&#99;更新快，网站页面清爽，广告少，'
]


def filterCustomer(line):
    ret = line
    for rule in rules:
        ret = ret.replace(rule, '')
    return ret


def filterUrl(line):
    reg = ur'(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?/'
    return re.sub(reg, '', line.lower())


def filterTag(line):
    return re.sub(ur'<.+>.*</.+>', '', line)


def filterParentheses(line):
    line = unicode(line)
    return re.sub(ur'[\uff08|\(].*[\uff09|\)]', '', line)


def filterBracket(line):
    return re.sub(ur'\[.*\]', '', line)


def fitter(line):
    line = filterUrl(line)
    line = filterTag(line)
    line = filterParentheses(line)
    line = filterBracket(line)
    line = filterCustomer(line)
    if u'广告' in line:
        print line
    return line


if __name__ == '__main__':
    file = open('../res/sx.txt')
    result = open('../res/new.txt', 'w')
    for line in file:
        content = fitter(line)
        if content:
            result.write(content)
    
    file.close()
    result.close()
