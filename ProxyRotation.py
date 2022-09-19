
from email import header
import random
import json
from typing_extensions import Self
import requests

class ProxyList():
    list = ['163.5.161.220:2133:monitor:vivabluem34',
        '163.5.161.221:2133:monitor:vivabluem34',
        '163.5.161.222:2133:monitor:vivabluem34',
        '163.5.161.223:2133:monitor:vivabluem34',
        '163.5.161.224:2133:monitor:vivabluem34',
        '163.5.161.225:2133:monitor:vivabluem34',
        '163.5.161.226:2133:monitor:vivabluem34',
        '163.5.161.227:2133:monitor:vivabluem34',
        '163.5.161.228:2133:monitor:vivabluem34',
        '163.5.161.229:2133:monitor:vivabluem34',
    ]
    used = {key:0 for key in list}
    def getRandom(list):
        proxies = random.choice(list)
        port = proxies.split(':')[1]
        user = proxies.split(':')[2]
        ip = proxies.split(':')[0]
        pw = proxies.split(':')[3]
        proxies = {
            'https':'http://%s:%s@%s:%s' % (user, pw, ip, port),
            'http':'http://%s:%s@%s:%s' % (user, pw, ip, port),
        }
        return proxies


    def randomAgent():
        list = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
                'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/105.0.5195.100 Mobile/15E148 Safari/604.1',
                'Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.79 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 10; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.79 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 10; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.79 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 10; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.79 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 10; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.79 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 10; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.79 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 10; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.79 Mobile Safari/537.36']

        return random.choice(list)
