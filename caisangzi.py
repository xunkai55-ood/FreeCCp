# -*- coding: utf-8 -*-

from PyCCp import PoetryManager, YunDict
from PyCCp.filters import BasicCipaiPF
from PyCCp.cipai import is_equal as is_same_struct
from PyCCp.chinese import count_char, is_char, last_char

yd = YunDict()

def analyze(lst):
    n = len(lst)
    m = count_char(lst[0])

    # info(ping, ze, yun)
    info = [[0, 0, 0] for i in range(m)]

    for p in lst:
        pot_yun_bu = list(set([x["bu"] for x in yd[last_char(p)]]))
        if len(pot_yun_bu) == 1:
            bu = pot_yun_bu[0]
        else:
            bu = None
        i = 0
        for c in p.content:
            if not is_char(c):
                continue
            if yd.has_char(c):
                if yd.only_ping(c):
                    info[i][0] += 1
                elif yd.only_ze(c):
                    info[i][1] += 1
                pot_yun_bu = list(set([x["bu"] for x in yd[c]]))
                if len(pot_yun_bu) == 1 and bu == pot_yun_bu[0]:
                    info[i][2] += 1
            i += 1

    p = lst[0]
    j = 0

    for i in range(m):
        while not is_char(p.content[j]):
            j += 1
        print p.content[j], " ", info[i]
        j += 1

    print "report from ", n, " poetry"
    print "==========="

pai = raw_input("pai: ").decode("utf-8")
pf = BasicCipaiPF(pai)
dbm = PoetryManager("text", "dbs/text-souyun-ci")
pool = dbm.get_all()

stream = pf.filter(pool)

n = len(stream)
checked = [0 for i in range(n)]

for i in range(n):
    if checked[i] == 0:
        some = [stream[i]]
        checked[i] = 1
        for j in range(i, n):
            if is_same_struct(stream[i], stream[j]):
                some.append(stream[j])
                checked[j] = 1
        analyze(some)


