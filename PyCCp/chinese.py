# -*- coding: utf-8 -*-

breakings = list(u",.，。、!?！？")
blanks = ["\n", "\r", " ", "\t"]

def is_char(c):
    if not c in breakings and not c in blanks:
        return True
    else:
        return False

def count_char(p):
    ans = 0
    for c in p.content:
        if is_char(c):
            ans += 1
    return ans

def last_char(p):
    for c in reversed(p.content):
        if is_char(c):
            return c
    return None
