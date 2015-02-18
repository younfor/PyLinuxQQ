# coding=utf-8

import urllib2
import re
import cookielib
import spidermonkey


class PyLinuxQQ(object):

    """docstring for PyLinuxQQ"""
    """
        by Younfor 2015-02-17
        QQ 361106306
    """

    def __init__(self, username, password):
        super(PyLinuxQQ, self).__init__()
        self.cookies = cookielib.CookieJar()
        self.opener = urllib2.build_opener(
            urllib2.HTTPHandler(),
            urllib2.HTTPSHandler(),
            urllib2.HTTPCookieProcessor(self.cookies),
        )
        urllib2.install_opener(self.opener)
        self.username = username
        self.password = password

    def login_pre(self):
        # login_sig
        url_sig = 'https://ui.ptlogin2.qq.com/cgi-bin/login?daid=164&target=self&style=16&mibao_css=m_webqq&appid=501004106&enable_qlogin=0&no_verifyimg=1&s_url=http%3A%2F%2Fw.qq.com%2Fproxy.html&f_url=loginerroralert&strong_login=1&login_state=10&t=20131024001'
        req = urllib2.Request(url_sig)
        data = urllib2.urlopen(req).read()
        # print data
        arg = re.search(r'g_login_sig=encodeURIComponent\("(.*?)"', data)
        # print arg
        self.login_sig = arg.group(1)
        # print self.login_sig
        # check_code
        url = 'https://ssl.ptlogin2.qq.com/check?pt_tea=1&uin=' + self.username + \
            '&appid=501004106&js_ver=10113&js_type=0&login_sig=' + self.login_sig + \
            '&u1=http%3A%2F%2Fw.qq.com%2Fproxy.html&r=0.5872094901278615'
        req = urllib2.Request(url)
        data = urllib2.urlopen(req).read()
        arg = re.search(r"'(.)','(.*?)','(.*?)'", data)
        self.check = arg.group(1)
        self.code1 = arg.group(2)
        self.code2 = arg.group(3)
        # print check, code1, code2
        url_code = 'https://ssl.captcha.qq.com/getimage?aid=501004106&r=0.4779968443326652&uin=' + \
            self.username
        # print data
        if self.check == '1':
            req = urllib2.Request(url_code)
            imgData = urllib2.urlopen(req).read()
            imgfile = open("code.jpg", "wb")
            imgfile.write(imgData)
            imgfile.close()
            self.code1 = raw_input('code:')
            self.pt_verifysession_v1 = None
        else:
            ck = dict((c.name, c.value) for c in self.cookies)
            self.pt_verifysession_v1 = ck['ptvfsession']
        print self.code1

    def login_on(self):
        #getEncryption(c.p.value, pt.salt, c.verifycode.value)
        sm = spidermonkey.Runtime()
        file_js = open("loginMd5.js", "r")
        cx = sm.new_context()
        getp = cx.execute(file_js.read())
        p = getp(self.username, self.password, self.code1)
        if self.check == '1':
            ck = dict((c.name, c.value) for c in self.cookies)
            self.pt_verifysession_v1 = ck['verifysession']
        login_on_url = 'https://ssl.ptlogin2.qq.com/login?u=' + self.username + '&p=' + p + '&verifycode=' + self.code1 + \
            '&webqq_type=10&remember_uin=1&login2qq=1&aid=501004106&u1=http%3A%2F%2Fw.qq.com%2Fproxy.html%3Flogin2qq%3D1%26webqq_type%3D10&h=1&ptredirect=0&ptlang=2052&daid=164&from_ui=1&pttype=1&dumy=&fp=loginerroralert&action=0-16-56797&mibao_css=m_webqq&t=1&g=1&js_type=0&js_ver=10113&login_sig=' + self.login_sig + '&pt_randsalt=0&pt_vcode_v1=0&pt_vcode_v1=0&pt_verifysession_v1=' + \
            self.pt_verifysession_v1
        req = urllib2.Request(login_on_url)
        data = urllib2.urlopen(req).read()
        # print self.pt_verifysession_v1
        # print p
        # print login_on_url
        print data
if __name__ == "__main__":
    qq = PyLinuxQQ('28762822', '199288@920808')
    qq.login_pre()
    qq.login_on()
