
import requests
import threading
import ProxyRotation
from Logging import log_message
import time
from discord_webhook import DiscordEmbed,DiscordWebhook

import io
import urllib.request
from PIL import Image
from discord_webhook import DiscordWebhook, DiscordEmbed


list = ProxyRotation.ProxyList.list
database = []
def rotateProxy():
    proxies = ProxyRotation.ProxyList.getRandom(list)
    return proxies

def request(proxies):
    headers = {
    'Host': 'www.asos.com',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'FPID=FPID2.2.XG3AJvFRyQklM4VfvT4V0pOx93xIK6JT4Myscu1ppmY%3D.1652805293; s_ecid=MCMID%7C64756085211676133321393763491374047020; featuresId=867dece1-f7e6-438c-a3c9-2af710d56e91; _cs_c=0; OptanonAlertBoxClosed=2022-09-10T15:19:02.035Z; _gcl_au=1.1.366325736.1662823142; bt_stdstatus=NOTSTUDENT; FPAU=1.1.366325736.1662823142; fita.sid.asos=4zal-cQ5NAbhSTo5mvFQXnl9mZ-guMff; optimizelyEndUserId=oeu1662924843688r0.6292511598865644; _fbp=fb.1.1662924848267.357825884; asos-b-sdv629=dup0qtf-35; _gid=GA1.2.91775281.1663062340; FPLC=wm%2BYBqvvOPQsDj%2Bu%2FMEsbeunblICZNrEtsc7Gv6rrIh9lJAd3caGPuxq%2BwzUEfmlomWqjP9DmgLkql%2BKWtvBJGRwijHB8X8O1mmlGiat8lAvzWijkI8JD%2B4IQruASg%3D%3D; asosAffiliate=affiliateId=12493; bt_affid=12493; gig_bootstrap_3_Gl66L3LpFTiwZ8jWQ9x_4MLyUUHPRmPtRni0hzJ9RH5WA2Ro6tUv47yNXtKn3HQ8=social_ver4; asos-cgd26=dc817a9b28d247efaed0626c5d1b41b7; asos-perx=dc817a9b28d247efaed0626c5d1b41b7|79f36c90ae9d4759a818cf495959a49a|32b8d9c9da564806b60a34375d8a419c; sd_client_id=0a39b1f5-85cb-44eb-97b1-8ed0e60fc58f; studentModalShown=true; stc-welcome-message=cappedPageCount=2&resolvedDeliveryCountry=IT&userTookActionOnWelcomeMessage=true; floor=1001; plp_columsCount=fourColumns; browseCountry=IT; browseCurrency=EUR; browseLanguage=it-IT; browseSizeSchema=IT; storeCode=IT; asos=PreferredSite=&currencyid=19&currencylabel=EUR&customerguid=dc817a9b28d247efaed0626c5d1b41b7&topcatid=1001&customerid=258187556; currency=19; geocountry=IT; bm_sz=8E4AAD1C869CBF23DA27F9598F792B6A~YAAQj/4SAhcx5vSCAQAAZQ9GOBGZz62ufOwSBdDWBZrE3JBnhQfm1PkUFsVhWD6qdufneahKZ8dn8PRalA4/oHxc4EQIqvYUcxdH8SYQ82N++MYl8ywXTkKlCRwsDbnIVu5B/puyt0V7IJLvawqp7NYT6S0ceAhZlnxxGs9Vu8J8udLkpiDa+dyKq7xVaLUDhE6SaD57koFYvXvmefYpXzviOkkpl2My3iMM77ZXoOFPSGt3NuA1pT0zyoCwAayWvCRBF8/JRtZTA4YS5k+lqXIFxsZZADFlR45noxuhIeiM~3424569~3551814; siteChromeVersion=au=11&com=11&de=11&dk=11&es=11&fr=11&it=11&nl=11&pl=11&roe=11&row=11&ru=11&se=11&us=11; keyStoreDataversion=dup0qtf-35; ak_bmsc=787ABFA15ECE9E80CBBC0B82A6FEFD9F~000000000000000000000000000000~YAAQj/4SAkUx5vSCAQAATx5GOBEhIy9jWoxRdH5dFQzQDaVDstLZRRiMp92oqTPHjPnP85nCLyfeUuhOSVqd1M+ZWoiIuPQBuxxgcfNmHr0KAO0Gy4UqBdUxu2H88zUAUVQM26Ra4AigU9XUogvZQh0co7f0Ff9L2ECn7YSYmp5p2IZy3rwaO6Vp5ru/mMIOSKyyJnm6jBC/4vuoRgiGjGW92qfnlSdbDA3HIJCjpwAepAYH3ON9cK8y8iQN3Sr1m28C0V205BZkXDq3ugS2jEBxu9VWgR28Al0m5sRfLM4T+SVlEnrFGM+t+p9gziZZvh/eE32FQN9CXbI2OfZaq08x8LwZ9t5pcTf9Y7uIqsVgSh1HVPPRKsoYAJpT0S3aHk2j1rT0Boo=; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C64756085211676133321393763491374047020%7CMCAAMLH-1663701263%7C6%7CMCAAMB-1663701263%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1663103663s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.3.0%7CMCCIDH%7C-1732102310; _s_fpv=true; s_cc=true; BagOrigin=EUW; BagId:IT:IT=be512022-317f-4027-bfea-c58b3e5898c5; asosbasket=basketitemcount=0&basketitemtotalretailprice=0; BagLastModified:IT:IT=1663096463799; _cs_mk_aa=0.6583389595471305_1663096464148; OptanonConsent=isIABGlobal=false&datestamp=Tue+Sep+13+2022+21%3A14%3A29+GMT%2B0200+(Ora+legale+dell%E2%80%99Europa+centrale)&version=202208.1.0&hosts=&consentId=5c0c2de8-c7d1-486d-b52d-2e9dbaa15724&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=IT; _cs_id=59438be7-6539-a3df-d420-019662b0c34a.1662823126.5.1663096469.1663096464.1628755191.1696987126947; _cs_s=2.0.0.1663098269054; _ga=GA1.2.150342912.1652805293; _abck=0242DBAC36712630BF6B6CBE4EBED466~0~YAAQhf4SApWaL/6CAQAA1FdKOAiPT9F6nkgFzEgEjaAgA6nFNc/9DgnLGzclr9ojtllJj0Q0crbHJt38Ehk2gvmC68Juhm4PCpfxc6A1H7Pa2kbylJt/2WBrCl++U+yVR5VfrDc/c0g9bPxiZT2fOfyRIxUo/79LvPQWZXCG3CiLRxICunWsZc5moRyj2HjTaM2a/s0gjtlx1svBWplu0tw1hf3Dx0I0GLhn5MhhfDFWSKWMoi2/saEIpeoaTdmTVWnIrxe/9MDOM1v+nbQPiAU/6iVmoY0dHbbf37hmdwSuF/diopQ/P78FPjNEcwpVaBSVOgxGstBVPB1S5K5xe2U6LGpdKfQ0Q8AgwxiucWq3Io3YFahy+d+vLh+5IRBXT+wZe8TGO5ERG5Dc6Vf8JWfMHw==~-1~||1-KIkJfguRsl-1-10-1000-2||~1663100227; RT="z=1&dm=asos.com&si=5e35f2f4-da2f-4774-932f-67a7f2108c32&ss=l80kowj8&sl=8&tt=7wr&bcn=%2F%2F684dd32e.akstat.io%2F&obo=1"; s_pers=%20s_vnum%3D1664575200903%2526vn%253D6%7C1664575200903%3B%20gpv_p6%3D%2520%7C1663098262914%3B%20eVar225%3D4%7C1663098268068%3B%20visitCount%3D6%7C1663098268072%3B%20s_invisit%3Dtrue%7C1663098269583%3B%20s_nr%3D1663096469584-Repeat%7C1694632469584%3B%20gpv_e47%3Dno%2520value%7C1663098269586%3B%20gpv_p10%3Ddesktop%2520it%257Ccategory%2520page%257C17184%2520refined%7C1663098269589%3B%20gpv_e231%3D6865f7bb-6924-4517-911b-ee12759441ff%7C1663098639249%3B; _ga_1JR0QCFRSY=GS1.1.1663096464.6.1.1663096839.60.0.0; s_sq=asoscomprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Ddesktop%252520it%25257Ccategory%252520page%25257C17184%252520refined%2526link%253DNovit%2525C3%2525A0%252520disponibile%252520da%2526region%253DmediumRefinements%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'asos-c-plat': 'web',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'asos-c-name': 'asos-web-product-listing-page',
    'accept': 'application/json, text/plain, */*',
    'sec-ch-ua-mobile': '?0',
    'asos-c-ver': '1.2.0-ebb0a8b4486b-6547',
    'asos-cid': '7b2751a0-5eb2-49c6-afe2-62cc66046a4f',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.asos.com/it/uomo/novita/novita-scarpe/cat/?cid=17184&currentpricerange=5-240&refine=brand:14269,2986,499|freshness_band:1',
    'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    params = {
        'CustomerGuid': 'dc817a9b28d247efaed0626c5d1b41b7',
        'brand': '14269,2986,499',
        'channel': 'desktop-web',
        'country': 'IT',
        'currency': 'EUR',
        'freshness_band': '1',
        'keyStoreDataversion': 'dup0qtf-35',
        'lang': 'it-IT',
        'limit': '72',
        'offset': '0',
        'rowlength': '4',
        'store': 'IT',
        #'tst-search-sponsored-products': 'true',
    }
    try:
       response = requests.get('https://www.asos.com/api/product/search/v2/categories/17184', params=params,  headers=headers, proxies = proxies)
    except Exception as e:
        print(e)
    return response

def webhook(pid, name, prezzo, image, url, brand):
    web = DiscordWebhook(url='https://discord.com/api/webhooks/1019353487672352768/EDBCqWW5WJSxcnbVYCXNRSMs3xh9NNUWuQ8LnTjuefBkXEehsaCVnXBBOX5ndIue5yxh') #connects with discord
    embed = DiscordEmbed(title = f"New product - {brand}", description = url)

    embed.add_embed_field(name = "Name", value = name, inline = False)
    embed.add_embed_field(name = "PID", value = pid, inline = False)
    embed.add_embed_field(name = "Price", value = str(prezzo), inline = False)
    web.add_embed(embed) #adds the newly created embed
    web.execute() #sends the webhook
def cycle():

    while True:
        proxies = rotateProxy()
        response = request(proxies)
       
        if response.status_code == 200:
            if response.headers['Cache-Control'] == 'no-cache, no-store':
                json = response.json()
               
                for prod in json['products']:
                    if prod['id']  not in database:
                        try:
                            name = prod['name']
                        except:
                            name = None
                        try:
                            price = prod['price']['current']['text']
                        except:
                            price = None
                        try:
                            brandName = prod['brandName']
                        except:
                            brandName = None
                        try:
                            url = 'https://www.asos.com/' + 'prd/' + str(prod['id'])
                        except:
                            url = None
                        try:
                            img = 'https://'+prod['imageUrl'] #img has a problem, prob a cdn
                        except:
                            img = None
                        
                        log_message('NEW ITEM','Monitored a new item')
                        webhook(prod['id'],name,price,img,url,brandName)
                        database.append(prod['id'])
                        
            
            else:
                log_message('ERROR','Response got cached')
        elif  response.status_code == 304:
            log_message('ERROR','Response got redirected')
        elif  response.status_code == 429 or  response.status_code == 403:
            log_message('ERROR','IP got banned')
        elif  response.status_code == 404:
            log_message('ERROR','NOT FOUND')
        else:
            log_message('ERROR','Request had an uncovered error')

        log_message('DONE','Done with the cycle')
        time.sleep(0.5)

def main():

    #make the request
    proxies = rotateProxy()
    response = request(proxies)
    
    if response.status_code == 200:
        if response.headers['Cache-Control'] == 'no-cache, no-store':
            json = response.json()
            for prod in json['products']:
                if prod['id'] not in database:
                    database.append(prod['id'])
            #start looping over the items
            cycle()
        else:
            log_message('ERROR','Response got cached')
    elif  response.status_code == 304:
        log_message('ERROR','Response got redirected')
    elif  response.status_code == 429 or  response.status_code == 403:
        log_message('ERROR','IP got banned')
    elif  response.status_code == 404:
        log_message('ERROR','NOT FOUND')
    else:
        log_message('ERROR','Request had an uncovered error')
    

        
    

if __name__ == '__main__':
    Thread = threading.Thread(target=main)
    Thread.name = f'- New Prod Monitoring'
    Thread.start()


        
    