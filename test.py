# -*- coding: utf-8 -*-

import PyCCp

def test1():
    sub = u"浣溪沙"
    a_info = {"dynasty": u"宋", "author": u"晏殊"}
    version = ""
    content = u"一曲新词酒一杯，去年天气旧亭台，夕阳西下几时回？无可奈何花落去，似曾相识燕归来，小园香径独徘徊。"
    b = PyCCp.Ci(sub, a_info, content, version)
    print b
    print unicode(b)

if __name__ == "__main__":
    test1()
