# coding=utf-8

import urllib2
import urllib
import re
import cookielib
import spidermonkey
import json
import time


class PyLinuxQQ(object):

    """docstring for PyLinuxQQ"""
    """
        by Younfor 2015-02-17
        QQ 361106306
    """
    username = ''
    password = ''
    login_sig = ''
    check = ''
    code1 = ''  # default verifycode
    code2 = ''  # uname 0x123
    pt_verifysession_v1 = ''
    p = ''
    ptwebqq = ''
    newvfwebqq = ''
    psessionid = ''
    info_hash = ''
    clientid = '53999199'

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

    def login_sig(self):
        # get_login_sig
        url_sig = 'https://ui.ptlogin2.qq.com/cgi-bin/login?daid=164&target=self&style=16&mibao_css=m_webqq&appid=501004106&enable_qlogin=0&no_verifyimg=1&s_url=http%3A%2F%2Fw.qq.com%2Fproxy.html&f_url=loginerroralert&strong_login=1&login_state=10&t=20131024001'
        req = urllib2.Request(url_sig)
        data = urllib2.urlopen(req).read()
        arg = re.search(r'g_login_sig=encodeURIComponent\("(.*?)"', data)
        self.login_sig = arg.group(1)
        print 'login_sig:', self.login_sig

    def login_check(self):
        # get_check
        url = 'https://ssl.ptlogin2.qq.com/check?pt_tea=1&uin=' + self.username + \
            '&appid=501004106&js_ver=10113&js_type=0&login_sig=' + self.login_sig + \
            '&u1=http%3A%2F%2Fw.qq.com%2Fproxy.html&r=0.5872094901278615'
        req = urllib2.Request(url)
        data = urllib2.urlopen(req).read()
        arg = re.search(r"'(.)','(.*?)','(.*?)'", data)
        self.check = arg.group(1)
        self.code1 = arg.group(2)
        self.code2 = arg.group(3)
        print 'check,code1,code2:', self.check, self.code1, self.code2
        # get_verifycode
        url_code = 'https://ssl.captcha.qq.com/getimage?aid=501004106&r=0.4779968443326652&uin=' + \
            self.username
        if self.check == '1':
            req = urllib2.Request(url_code)
            imgData = urllib2.urlopen(req).read()
            imgfile = open("code.jpg", "wb")
            imgfile.write(imgData)
            imgfile.close()
            self.code1 = raw_input('code:')
        else:
            ck = dict((c.name, c.value) for c in self.cookies)
            self.pt_verifysession_v1 = ck['ptvfsession']
        print 'verifycode:', self.code1
        print 'pt_verifysession_v1:', self.pt_verifysession_v1

    def login_on(self):
        # getp
        sm = spidermonkey.Runtime()
        file_js = open("loginMd5.js", "r")
        cx = sm.new_context()
        getp = cx.execute(file_js.read())
        self.p = getp(self.username, self.password, self.code1)
        print 'p:', self.p
        # login 1
        if self.check == '1':
            ck = dict((c.name, c.value) for c in self.cookies)
            self.pt_verifysession_v1 = ck['verifysession']
        login_on_url = 'https://ssl.ptlogin2.qq.com/login?u=' + self.username + '&p=' + self.p + '&verifycode=' + self.code1 + \
            '&webqq_type=10&remember_uin=1&login2qq=1&aid=501004106&u1=http%3A%2F%2Fw.qq.com%2Fproxy.html%3Flogin2qq%3D1%26webqq_type%3D10&h=1&ptredirect=0&ptlang=2052&daid=164&from_ui=1&pttype=1&dumy=&fp=loginerroralert&action=0-16-56797&mibao_css=m_webqq&t=1&g=1&js_type=0&js_ver=10113&login_sig=' + self.login_sig + '&pt_randsalt=0&pt_vcode_v1=0&pt_vcode_v1=0&pt_verifysession_v1=' + \
            self.pt_verifysession_v1
        req = urllib2.Request(login_on_url)
        data = urllib2.urlopen(req).read()
        print 'login 1'
        # login 2
        arg = re.search(r"'.','.','(.*?)'", data)
        req = urllib2.Request(arg.group(1))
        data = urllib2.urlopen(req).read()
        ck = dict((c.name, c.value) for c in self.cookies)
        if ck['ptwebqq']:
            # print 'ptwebqq:', ck['ptwebqq']
            self.ptwebqq = ck['ptwebqq']
        print 'ptwebqq:', self.ptwebqq
        print 'login 2'
        # login 3
        url_vf = 'http://s.web2.qq.com/api/getvfwebqq?ptwebqq=' + \
            self.ptwebqq + '&clientid=53999199&psessionid=&t=1424324701030'
        req = urllib2.Request(url_vf)
        req.add_header(
            'Referer', 'http://s.web2.qq.com/proxy.html?v=20130916001&callback=1&id=1')
        data = json.load(urllib2.urlopen(req))
        self.newvfwebqq = data['result']['vfwebqq']
        print 'newvfwebqq:', self.newvfwebqq
        print 'login 3'
        # login post
        url_post = 'http://d.web2.qq.com/channel/login2'
        data_post = {
            'r': '{"ptwebqq":"' + self.ptwebqq + '","clientid":53999199,"psessionid":"","status":"online"}'
        }
        req = urllib2.Request(url_post, data=urllib.urlencode(data_post))
        req.add_header(
            'Referer', 'http://d.web2.qq.com/proxy.html?v=20130916001&callback=1&id=2')
        data = json.load(urllib2.urlopen(req))
        print 'login post'
        '''
        {"retcode":0,
            "result":{"uin":28762822,
                        "cip":3062847601,
                        "index":1075,
                        "port":49069,
                        "status":"online",
                        "vfwebqq":"3a479360aa6e9f45b0d6a990bb53a296666c3bff30b78bc58ee4d992899680848deadb94a4689df8",
                        "psessionid":"8368046764001d636f6e6e7365727665725f77656271714031302e3133392e372e31363000000b43000006af016201b6e2c66d0000000a403251345a4f675a506a6d000000283a479360aa6e9f45b0d6a990bb53a296666c3bff30b78bc58ee4d992899680848deadb94a4689df8",
                        "user_state":0,
                        "f":0
                        }
        }
        '''
        self.psessionid = data['result']['psessionid']
        print 'psessionid:', self.psessionid

    def get_infoHash(self):
        # get_hash
        sm = spidermonkey.Runtime()
        file_js = open("infoHash.js", "r")
        cx = sm.new_context()
        get_hash = cx.execute(file_js.read())
        self.info_hash = get_hash(self.username, self.ptwebqq)
        print 'info_hash:', self.info_hash

    def get_friends(self):
        url_post = 'http://s.web2.qq.com/api/get_user_friends2'
        data_post = {
            'r': '{"vfwebqq":"' + self.newvfwebqq + '","hash":"' + self.info_hash + '"}'
        }
        req = urllib2.Request(url_post, data=urllib.urlencode(data_post))
        req.add_header(
            'Referer', 'http://s.web2.qq.com/proxy.html?v=20130916001&callback=1&id=1')
        data = json.load(urllib2.urlopen(req))
        print data['result']['friends']

    def update_poll(self):
        url = 'http://d.web2.qq.com/channel/poll2'
        data_poll = {
            'r': '{"ptwebqq":"' + self.ptwebqq + '","clientid":"' + self.clientid + '",\
            "psessionid":"' + self.psessionid + '","key":""}'
        }
        req = urllib2.Request(url, data=urllib.urlencode(data_poll))
        req.add_header(
            'Referer', 'http://d.web2.qq.com/proxy.html?v=20130916001&callback=1&id=2')
        data = json.load(urllib2.urlopen(req))
        if data['retcode']==0:
            print data['result'][0]['value']['content']
        else:
            print 'update poll'
if __name__ == "__main__":
    qq = PyLinuxQQ('28762822', '199288@920808')
    qq.login_sig()
    qq.login_check()
    qq.login_on()
    qq.get_infoHash()
    qq.get_friends()
    while True:
        time.sleep(10)
        qq.update_poll()
