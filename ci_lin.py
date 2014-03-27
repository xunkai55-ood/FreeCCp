# -*- coding: utf-8 -*-

import codecs
import sqlite3
import json

lines = codecs.open("ci_lin_1", "r", "utf-8").readlines()

bu = 0

yun_dic = {} # {"x": [{"bu": num, "yun": "", "sheng": ""}]}
cn_digit = list(u"一二三四五六七八九十")
yun_list = []

sheng_dic = {}
xlns = codecs.open("yun_sheng.txt", "r", "utf-8").readlines()
diao = u"平上去入"
cnt = 0
for each in xlns:
    if each[0] == "=":
        cnt += 1
        continue
    sheng_dic[each.strip()] = diao[cnt]
    print each, diao[cnt]

def sheng(x):
    print x
    print sheng_dic.keys()
    return sheng_dic[x]

for each in lines:
    each = each.strip()

    if len(each) == 0:
        continue

    # start of a part
    if each.find(u"第") == 0 and each.find(u"部") >= 1:
        bu += 1
        continue

    if each.find(u"注") == 0:
        continue

    if each.find(u"其他僻字") == 0:
        # TODO
        continue

    if each[0] in cn_digit:
        s = u""
        for c in each:
            s += c
            if not c in cn_digit:
                break
        yun_list.append(s)
        
        flag = 0
        for c in each:
            if c == u'[' or c == u'(':
                flag += 1
            if not c in cn_digit and flag == 0:
                if yun_dic.has_key(c):
                    yun_dic[c].append({"bu": bu, "yun": s, "sheng": sheng(s)})
                else:
                    yun_dic[c] = [{"bu": bu, "yun": s, "sheng": sheng(s)}]
            if c == u']' or c == u')':
                flag -= 1

        continue

    flag = True
    for c in each:
        if c == u'[':
            flag = False
        if not c in cn_digit and flag:
            if yun_dic.has_key(c):
                yun_dic[c].append({"bu": bu, "yun": s, "sheng": sheng(s)})
            else:
                yun_dic[c] = [{"bu": bu, "yun": s, "sheng": sheng(s)}]
        if c == u']':
            flag = True

yun_list = list(set(yun_list))
yun_list.sort()
for each in yun_list:
    print each
print len(yun_dic.keys())

f = codecs.open("ci_lin_zheng_yun", "w", "utf-8")
json.dump(yun_dic, f, ensure_ascii = False)
