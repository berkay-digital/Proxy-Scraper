import requests
import time
from termcolor import colored

timeout = "3000"
url = "https://api.proxyscrape.com/v3/free-proxy-list/get"
url2 = "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt"

querystring = {
    "request": "displayproxies",
    "protocol": "http",
    "timeout": f"{timeout}",
}

headers = {
    "accept": "text/plain, */*; q=0.01",
    "accept-language": "en-US,en;q=0.8",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

response = requests.request(
    "GET", url, headers=headers, params=querystring
)
response2 = requests.request("GET", url2, headers=headers)
print(response.text)
proxies = []
proxies.extend(response.text.split("\n"))
proxies.extend(response2.text.split("\n"))
print("Amount of proxies:", len(proxies))
time.sleep(3)


import urllib.request, socket

socket.setdefaulttimeout(3)


def is_bad_proxy(pip):
    try:
        proxy_handler = urllib.request.ProxyHandler({"http": pip})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [("User-agent", "Mozilla/5.0")]
        urllib.request.install_opener(opener)
        sock = urllib.request.urlopen("http://api.ipify.org/")
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as detail:
        return 1
    return 0


import concurrent.futures

working = []
badcount = 0
workingcount = 0

def check_proxy(proxy):
    global badcount, workingcount
    if is_bad_proxy(proxy):
        badcount += 1
        print(colored(f"{badcount} bad proxies", "red"))
    else:
        workingcount += 1
        print(colored(f"{workingcount} working proxies", "green"))
        working.append(proxy + "\n")



start_time = time.time()

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(check_proxy, proxies)
end_time = time.time()
print("Time taken: ", end_time - start_time, "seconds")
with open("proxies.txt", "w") as f:
    f.writelines(working)
