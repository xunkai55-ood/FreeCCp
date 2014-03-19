# -*- coding: utf-8 -*-

class Record(object):

    def __init__(self, subject, a_info, content, version = ""):
        
        # basic info
        self.subject = subject
        self.a_info = a_info
        self.content = content
        self.version = version

    def __unicode__(self):
        return self.content + u"——《" + self.subject + u"》[" + self.a_info["dynasty"] + u"]" + self.a_info["author"]

    def __str__(self):
        return unicode(self).encode('utf-8')

