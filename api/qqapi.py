# coding=utf-8

import urllib2
import urllib
import re
import cookielib
import spidermonkey
import json
import time
import random
import os
import json.encoder as json_encode,json.decoder as json_decode

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
    msgid = 74210001
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
            imgfile = open("api/code.jpg", "wb")
            imgfile.write(imgData)
            imgfile.close()
            #self.code1 = raw_input('code:')
            #print 'verifycode:', self.code1
            return True
        else:
            ck = dict((c.name, c.value) for c in self.cookies)
            self.pt_verifysession_v1 = ck['ptvfsession']
            print 'verifycode:', self.code1
            print 'pt_verifysession_v1:', self.pt_verifysession_v1
            return False
    def login_on(self):
        try:
            # getp
            sm = spidermonkey.Runtime()
            file_js = open("api/loginMd5.js", "r")
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
            if data['retcode']==0:
                return True
        except Exception,e:
            print e
            return False
        return False
    def get_infoHash(self):
        # get_hash
        sm = spidermonkey.Runtime()
        file_js = open("api/infoHash.js", "r")
        cx = sm.new_context()
        get_hash = cx.execute(file_js.read())
        self.info_hash = get_hash(self.username, self.ptwebqq)
        print 'info_hash:', self.info_hash
    def get_groups(self):
        '''
        result: {gmasklist: [], gnamelist: [{flag: 16794625, name: "Python学习交流群", gid: 4056809648, code: 2351612940}],…}
            gmarklist: []
            gmasklist: []
            gnamelist: [{flag: 16794625, name: "Python学习交流群", gid: 4056809648, code: 2351612940}]
            retcode: 0
        '''
        url_post='http://s.web2.qq.com/api/get_group_name_list_mask2'
        data_post = {
            'r': '{"vfwebqq":"' + self.newvfwebqq + '","hash":"' + self.info_hash + '"}'
        }
        req = urllib2.Request(url_post, data=urllib.urlencode(data_post))
        req.add_header(
            'Referer', 'http://s.web2.qq.com/proxy.html?v=20130916001&callback=1&id=1')
        data = json.load(urllib2.urlopen(req))
        return data['result']
    def get_friends(self):
        url_post = 'http://s.web2.qq.com/api/get_user_friends2'
        data_post = {
            'r': '{"vfwebqq":"' + self.newvfwebqq + '","hash":"' + self.info_hash + '"}'
        }
        req = urllib2.Request(url_post, data=urllib.urlencode(data_post))
        req.add_header(
            'Referer', 'http://s.web2.qq.com/proxy.html?v=20130916001&callback=1&id=1')
        data = json.load(urllib2.urlopen(req))
        return data['result']
    def get_discuss(self):
        url='http://s.web2.qq.com/api/get_discus_list?clientid='+self.clientid+'&psessionid='+self.psessionid+'&vfwebqq='+self.newvfwebqq+'&t=1425137995649'
        req=urllib2.Request(url)
        req.add_header(
            'Referer', 'http://s.web2.qq.com/proxy.html?v=20130916001&callback=1&id=1')
        data=json.load(urllib2.urlopen(req))
        print 'retcode',data['retcode']
        return data['result']
    def get_online_uin(self):
        url='http://d.web2.qq.com/channel/get_online_buddies2?vfwebqq='+self.newvfwebqq+'&clientid='+self.clientid+'&psessionid='+self.psessionid+'&t=1424840879328'
        print url
        req=urllib2.Request(url)
        req.add_header(
            'Referer', 'http://d.web2.qq.com/proxy.html?v=20130916001&callback=1&id=2')
        data=json.load(urllib2.urlopen(req))
        print 'retcode',data['retcode']
        return data['result']
    def get_self_info(self):
        url='http://s.web2.qq.com/api/get_self_info2?t=1424840878871'
        req=urllib2.Request(url)
        req.add_header(
            'Referer', 'http://s.web2.qq.com/proxy.html?v=20130916001&callback=1&id=1')
        data=json.load(urllib2.urlopen(req))
        return data['result']
    def get_face(self,uin='1599524561'):
        if os.path.exists('tmp/head/'+uin+'.jpg'):
            print 'exist uin',uin
            return
        url = 'http://face%s'%random.randint(1,9)+'.web.qq.com/cgi/svr/face/getface?cache=1&type=1&f=40&uin=%s'%uin+'&vfwebqq=%s'%self.newvfwebqq
        req = urllib2.Request(url)
        data=urllib2.urlopen(req).read()
        f=open('tmp/head/'+uin+'.jpg','wb')
        f.write(data)
        f.close()
    def get_happyface(self,id):
        z = [14, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 50, 51, 96, 53, 54, 73, 74, 75, 76, 77, 78, 55, 56, 57, 58, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 32, 113, 114, 115, 63, 64, 59, 33, 34, 116, 36, 37, 38, 91, 92, 93, 29, 117, 72, 45, 42, 39, 62, 46, 47, 71, 95, 118, 119, 120, 121, 122, 123, 124, 27, 21, 23, 25, 26, 125, 126, 127, 
            128, 129, 130, 131, 132, 133, 134, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170]
        B = [14, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 15, 16, 96, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 89, 113, 114, 115, 60, 61, 46, 63, 64, 116, 66, 67, 53, 54, 55, 56, 57, 117, 59, 75, 74, 69, 49, 76, 77, 78, 79, 118, 119, 120, 121, 122, 123, 124, 42, 85, 43, 
            41, 86, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170]
        print 'index:',B[z.index(id)]
        url='http://pub.idqqimg.com/lib/qqface/'+str(B[z.index(id)])+'.gif'
        if os.path.exists('tmp/face/'+str(id)+'.gif'):
            print 'exist face ',id
            return
        req = urllib2.Request(url)
        data=urllib2.urlopen(req).read()
        f=open('tmp/face/'+str(id)+'.gif','wb')
        f.write(data)
        f.close()
    def get_poll(self):
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
            return data['result']
        else:
            return None
    def send_msg(self,to_uin,msg=u'hello world'):
        '''
        url = 'http://d.web2.qq.com/channel/send_buddy_msg2'
        data_poll = {
            'r': '{"to":'+str(to_uin)+',"content":"[\"'+msg+u'\",[\"font\",{\"name\":\"宋体\",\"size\":10,\"style\":[0,0,0],\"color\":\"000000\"}]]","face":147,"clientid":'+self.clientid+',"msg_id":'+str(self.msgid)+',"psessionid":"'+self.psessionid+'"}'
        }
        req = urllib2.Request(url, data=urllib.urlencode(data_poll))
        req.add_header(
            'Referer', 'http://d.web2.qq.com/proxy.html?v=20130916001&callback=1&id=2')
        urllib2.urlopen(req)
        '''
        print 'sendto:',to_uin,'-',msg
        self.msgid+=1
        msg = u"[\""+ msg +u"\",[\"font\",{\"name\":\""+u'宋体'+u"\",\"size\":\"10\",\"style\":[0,0,0],\"color\":\"000000\"}]]"
        url = 'http://d.web2.qq.com/channel/send_buddy_msg2'
        a = {'to':to_uin,'face':180,'content':msg,'msg_id':self.msgid,'clientid':self.clientid,'psessionid':self.psessionid}
        array = {'r':json_encode.JSONEncoder().encode(a)}
        req = urllib2.Request(url, data=urllib.urlencode(array))
        req.add_header(
            'Referer', 'http://d.web2.qq.com/proxy.html?v=20130916001&callback=1&id=2')
        urllib2.urlopen(req)
'''
if __name__ == "__main__":
    qq = PyLinuxQQ('28762822', 'xxx')
    qq.login_sig()
    qq.login_check()
    qq.login_on()
    qq.get_infoHash()
    qq.get_friends()
    while True:
        time.sleep(10)
        qq.update_poll()
'''