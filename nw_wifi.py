#
import requests
import time
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:120.0) Gecko/20100101 Firefox/120.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en,en-GB;q=0.7,en-US;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://hotspot.internet-for-guests.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://hotspot.internet-for-guests.com/',
    # 'Cookie': 'LPSESS=2vu4q4qf55mhb1tuark016ts1n7bbmg7',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
}
params = {
    'auth': 'ticket',
    'pageID': 'page-0',
}

userpasses = [["neonwood2199", "ounrj", "b0:99:d7:bd:7d:3c"]]
data = {
    'auth': 'ticket',
    'lp-screen-size': '885:1512:1964:3024',
    'lp-input-username': f'{userpasses[0][0]}',
    'lp-input-password': f'{userpasses[0][1]}',
    'accept_tou': '1',
    'submit-login': 'Login',
}
def change_mac(mac):
    os.system("ifconfig eth0 down")
    os.system(f"sudo macchanger -m {mac} eth0")
    os.system("ifconfig eth0 up")
for i in userpasses:
    #change_mac(userpasses[i][2])
    time.sleep(3)
    r = requests.get("https://hotspot.internet-for-guests.com/", params=params, cookies={"LPSESS": "2vu4q4qf55mhb1tuark016ts1n7bbmg7"}, headers=headers, data=data)
    check = requests.get("https://hotspot.internet-for-guests.com/status")
    print(r.text, check.text)
    time.sleep(2)
    #change_mac("dc:a6:32:28:a3:77")

