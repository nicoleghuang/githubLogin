'''learn get cookie and send request with cookie'''
import requests
import ssl
import re
#import json
class loginGithub:
    requests.packages.urllib3.disable_warnings()
    if hasattr(ssl,'_unverified_context'):
        ssl._create_default_https_context=ssl._create_unverified_context
    def __init__(self):
        self.headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://github.com/',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Host':None
        }
        self.login_url='https://github.com/login'
        self.post_url='https://github.com/session'
        self.logined_url='https://github.com/dashboard-feed'
        #维持会话，自动处理cookie信息
        self.session=requests.Session()  

    #解析出登录所需要的token    
    def get_token(self):
        result=self.session.get(self.login_url)
        token=re.search('<form.*name="authenticity_token" value=(.*)/>?',result.text)
        #print(result.status_code)
        real_token=token.group(1).replace('\"','')
        #print(token.group(1))
        #print(real_token)
        return real_token.strip()
    
    #登录
    def login(self,email,password):
        data={
        "commit":"Sign in",
        "utf8":"√",
        "authenticity_token":self.get_token(),
        "login":email,
        "password":password
        }
        #print(data)
        res=self.session.post(url=self.post_url,data=data,headers=self.headers,verify=False)
        #print('********响应头**********',res.headers)
        print(res.status_code)
        #print(res.text)

    def feed(self):
        result=self.session.get(self.logined_url)
        if result.status_code==200:
            print(result.text)
        else:
            print(result.status_code)

if __name__ == "__main__":
    logins=loginGithub()
    logins.login(email,password)
    logins.feed()



 