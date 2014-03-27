# -*- coding: utf-8 -*-

import PyCCp
from PyCCp.managers import PoetryManager
from PyCCp.filters import SubjectPF, PaiSimilarityPF, BasicCipaiPF

def test1():
    'test record module'

    sub = u"浣溪沙"
    a_info = {"dynasty": u"宋", "author": u"晏殊"}
    version = ""
    content = u"一曲新词酒一杯，去年天气旧亭台，夕阳西下几时回？无可奈何花落去，似曾相识燕归来，小园香径独徘徊。"
    b = PyCCp.Ci(sub, a_info, content, version)
    print b
    print unicode(b)
    
def test2():
    'test text manager'

    dbm = PyCCp.managers.PoetryManager("text", "dbs/text-souyun-ci")
    print len(dbm.get_all())
    
def test3():
    'test basic filters'

    dbm = PoetryManager("text", "dbs/text-souyun-ci")
    pool = dbm.get_all()
    key = raw_input("keyword in subject?")
    spf = SubjectPF(key.decode("utf-8"))
    stream = spf.filter(pool)
    for each in stream:
        print each
    
    print "========="
    pspf = PaiSimilarityPF(stream)
    print pspf
    stream2 = pspf.filter(pool)
    for each in stream2:
        print each

def test4():
    'test basic pai name filter'

    dbm = PoetryManager("text", "dbs/text-souyun-ci")
    pool = dbm.get_all()
    key = raw_input("keyword in subject?")
    spf = SubjectPF(key.decode("utf-8"))
    stream = spf.filter(pool)

    print "========="
    bcpf = BasicCipaiPF(key.decode("utf-8"))
    print bcpf
    stream2 = bcpf.filter(pool)
    for each in stream2:
        print each

def test5():
    yd = PyCCp.YunDict()
    lst = list(u"曾经沧海难为水除却巫山不是云")
    for each in lst:
        print each
        print yd.gets(each)

if __name__ == "__main__":
    test5()
